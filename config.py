# Configuration file for the Windows-based household media manager

# Windows host settings
WINDOWS_HOST = {
    "host_name": "MY-WINDOWS-PC",
    "media_root": r"D:\\Media",
    "config_root": r"C:\\StreamingHouseholdManager",
    "preferred_provider_order": [
        "remux_media_server",
        "webdav_library",
        "torbox_cloud",
        "debrid_vault",
    ],
}

# Recommended legal self-hosted plan categories
PLAN_CATEGORIES = {
    "basic": {
        "name": "Basic Plan",
        "billing_model": "One-time setup, no monthly app fee",
        "recommended_app": "Jellyfin",
        "target_quality": ["HD", "FHD"],
        "primary_provider": "remux_media_server",
        "fallback_providers": ["webdav_library"],
        "household_limit_guidance": "1-2 simultaneous streams",
        "best_for": "Lowest-cost setup on a single Windows host",
        "hardware_profile": "Entry-level Windows PC with local storage",
    },
    "hd_fhd": {
        "name": "HD / FHD Plan",
        "billing_model": "No monthly app fee with Jellyfin, optional Plex subscription",
        "recommended_app": "Jellyfin",
        "alternate_app": "Plex",
        "target_quality": ["HD", "FHD"],
        "primary_provider": "remux_media_server",
        "fallback_providers": ["webdav_library", "torbox_cloud", "debrid_vault"],
        "household_limit_guidance": "2-3 simultaneous streams depending on bandwidth",
        "best_for": "Balanced quality and easier multi-household playback",
        "hardware_profile": "Mid-range Windows PC with stable upload bandwidth",
    },
    "4k": {
        "name": "4K Plan",
        "billing_model": "App cost optional, but requires stronger hardware and network",
        "recommended_app": "Plex",
        "alternate_app": "Jellyfin",
        "target_quality": ["4K", "HDR"],
        "primary_provider": "remux_media_server",
        "fallback_providers": ["webdav_library"],
        "household_limit_guidance": "1-2 simultaneous 4K direct-play streams",
        "best_for": "Highest quality playback across capable devices",
        "hardware_profile": "High-end Windows host, fast storage, gigabit-class network",
    },
}

# Dictionary to store household information
HOUSEHOLDS = {
    "household_1": {
        "name": "Living Room",
        "users": ["Mom", "Dad"],
        "max_streams": 2,
        "current_streams": 0,
        "status": "active",
        "plan_category": "4k",
        "allowed_providers": ["remux_media_server", "webdav_library", "torbox_cloud"],
        "current_sessions": [],
    },
    "household_2": {
        "name": "Bedroom",
        "users": ["Son"],
        "max_streams": 1,
        "current_streams": 0,
        "status": "active",
        "plan_category": "hd_fhd",
        "allowed_providers": ["remux_media_server", "debrid_vault"],
        "current_sessions": [],
    },
    "household_3": {
        "name": "Guest Room",
        "users": ["Guest"],
        "max_streams": 1,
        "current_streams": 0,
        "status": "inactive",
        "plan_category": "basic",
        "allowed_providers": ["webdav_library"],
        "current_sessions": [],
    },
}

# Provider settings for legal self-hosted or licensed library access
PROVIDERS = {
    "remux_media_server": {
        "name": "Remux Media Server",
        "service_type": "media_server",
        "access_method": "local_network",
        "library_path": r"D:\\Media\\RemuxLibrary",
        "status": "active",
        "priority": 1,
    },
    "webdav_library": {
        "name": "WebDAV Library",
        "service_type": "webdav",
        "access_method": "remote_library",
        "url": "https://your-webdav-endpoint.example/library",
        "status": "active",
        "priority": 2,
    },
    "torbox_cloud": {
        "name": "Torbox Cloud Library",
        "service_type": "cloud_library",
        "access_method": "remote_library",
        "account_label": "Torbox Pro Account Pool",
        "status": "active",
        "priority": 3,
    },
    "debrid_vault": {
        "name": "Debrid Vault",
        "service_type": "vault",
        "access_method": "remote_library",
        "vault_path": "/licensed-media",
        "status": "active",
        "priority": 4,
    },
}

# Log settings
LOG_FILE = "streaming_manager.log"
DEBUG_MODE = True
