"""Core logic for a Windows-based multi-household media manager."""

from __future__ import annotations

import copy
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

from config import DEBUG_MODE, HOUSEHOLDS, LOG_FILE, PROVIDERS, WINDOWS_HOST


class StreamingManager:
    """Manage household stream limits and provider-backed playback sessions."""

    def __init__(self) -> None:
        self.windows_host = copy.deepcopy(WINDOWS_HOST)
        self.households = copy.deepcopy(HOUSEHOLDS)
        self.providers = copy.deepcopy(PROVIDERS)
        self.session_counter = 0
        self._configure_logging()

    def _configure_logging(self) -> None:
        if not logging.getLogger().handlers:
            logging.basicConfig(
                filename=LOG_FILE,
                level=logging.DEBUG if DEBUG_MODE else logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
            )

    def _next_session_id(self) -> str:
        self.session_counter += 1
        return f"session_{self.session_counter:03d}"

    def _provider_rank(self, provider_id: str) -> int:
        preferred_order = self.windows_host.get("preferred_provider_order", [])
        if provider_id in preferred_order:
            return preferred_order.index(provider_id)
        return self.providers.get(provider_id, {}).get("priority", len(preferred_order) + 99)

    def _is_configured(self, provider: Dict[str, Any]) -> bool:
        url = provider.get("url")
        if url and "your-" in url:
            return False

        paths = [provider.get("library_path"), provider.get("vault_path")]
        if any(path for path in paths):
            return True

        return bool(provider.get("account_label") or provider.get("url"))

    def log_action(self, action: str) -> None:
        logging.info(action)

    def list_providers(self) -> Dict[str, Dict[str, Any]]:
        return copy.deepcopy(self.providers)

    def get_household_status(self, household_id: str) -> Dict[str, Any]:
        household = self.households.get(household_id)
        if not household:
            return {"error": f"Household '{household_id}' not found"}

        status = copy.deepcopy(household)
        status["streams_available"] = max(0, status["max_streams"] - status["current_streams"])
        status["recommended_provider_order"] = sorted(
            status.get("allowed_providers", []),
            key=self._provider_rank,
        )
        return status

    def get_all_households(self) -> Dict[str, Dict[str, Any]]:
        return {
            household_id: self.get_household_status(household_id)
            for household_id in self.households
        }

    def _select_provider(self, household_id: str, preferred_provider: Optional[str] = None) -> Optional[str]:
        household = self.households[household_id]
        allowed = household.get("allowed_providers", [])

        if preferred_provider:
            provider = self.providers.get(preferred_provider)
            if preferred_provider in allowed and provider and provider.get("status") == "active":
                return preferred_provider

        for provider_id in sorted(allowed, key=self._provider_rank):
            provider = self.providers.get(provider_id)
            if provider and provider.get("status") == "active":
                return provider_id

        return None

    def start_stream(
        self,
        household_id: str,
        user_name: str,
        content_title: str,
        preferred_provider: Optional[str] = None,
    ) -> Dict[str, Any]:
        household = self.households.get(household_id)
        if not household:
            return {"error": f"Household '{household_id}' not found"}

        if household.get("status") != "active":
            return {"error": f"Household '{household['name']}' is not active"}

        if household["current_streams"] >= household["max_streams"]:
            return {"error": f"Max streams reached for {household['name']}"}

        provider_id = self._select_provider(household_id, preferred_provider)
        if not provider_id:
            return {"error": f"No active provider available for {household['name']}"}

        provider = self.providers[provider_id]
        session_id = self._next_session_id()
        session = {
            "session_id": session_id,
            "user": user_name,
            "content_title": content_title,
            "provider_id": provider_id,
            "provider_name": provider["name"],
            "started_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "status": "playing",
        }

        household.setdefault("current_sessions", []).append(session)
        household["current_streams"] += 1

        self.log_action(
            f"Stream started: {user_name} in {household['name']} using {provider['name']} for {content_title}"
        )

        return {
            "message": f"Started '{content_title}' for {user_name} using {provider['name']}",
            "session_id": session_id,
            "provider_id": provider_id,
            "household": household["name"],
        }

    def stop_stream(self, household_id: str, session_id: Optional[str] = None) -> Dict[str, Any]:
        household = self.households.get(household_id)
        if not household:
            return {"error": f"Household '{household_id}' not found"}

        sessions: List[Dict[str, Any]] = household.get("current_sessions", [])
        if not sessions:
            return {"error": f"No active sessions found for {household['name']}"}

        session_index = -1
        if session_id:
            for index, session in enumerate(sessions):
                if session["session_id"] == session_id:
                    session_index = index
                    break
            if session_index == -1:
                return {"error": f"Session '{session_id}' not found in {household['name']}"}

        session = sessions.pop(session_index)
        household["current_streams"] = max(0, household["current_streams"] - 1)

        self.log_action(
            f"Stream stopped: {session['user']} in {household['name']} for {session['content_title']}"
        )

        return {
            "message": f"Stopped '{session['content_title']}' for {session['user']}",
            "session_id": session["session_id"],
            "household": household["name"],
        }

    def check_service_health(self) -> Dict[str, Dict[str, Any]]:
        health_report: Dict[str, Dict[str, Any]] = {}

        for provider_id, provider in self.providers.items():
            configured = self._is_configured(provider)
            raw_status = provider.get("status", "inactive")
            if raw_status != "active":
                status = "inactive"
            elif configured:
                status = "ready"
            else:
                status = "needs_configuration"

            health_report[provider_id] = {
                "name": provider["name"],
                "status": status,
                "configured": configured,
                "access_method": provider.get("access_method", "unknown"),
                "service_type": provider.get("service_type", "unknown"),
            }

        return health_report

    def get_summary(self) -> Dict[str, Any]:
        total_active_streams = sum(
            household["current_streams"] for household in self.households.values()
        )
        total_capacity = sum(household["max_streams"] for household in self.households.values())
        active_households = sum(
            1 for household in self.households.values() if household.get("status") == "active"
        )
        active_providers = sum(
            1 for provider in self.providers.values() if provider.get("status") == "active"
        )

        return {
            "windows_host": self.windows_host.get("host_name"),
            "media_root": self.windows_host.get("media_root"),
            "total_households": len(self.households),
            "active_households": active_households,
            "total_active_streams": total_active_streams,
            "total_capacity": total_capacity,
            "available_slots": max(0, total_capacity - total_active_streams),
            "active_providers": active_providers,
        }
