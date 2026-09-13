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

# Dictionary to store household information
HOUSEHOLDS = {
    "household_1": {
        "name": "Living Room",
        "users": ["Mom", "Dad"],
        "max_streams": 2,
        "current_streams": 0,
        "status": "active",
        "allowed_providers": ["remux_media_server", "webdav_library", "torbox_cloud"],
        "current_sessions": [],
    },
    "household_2": {
        "name": "Bedroom",
        "users": ["Son"],
        "max_streams": 1,
        "current_streams": 0,
        "status": "active",
        "allowed_providers": ["remux_media_server", "debrid_vault"],
        "current_sessions": [],
    },
    "household_3": {
        "name": "Guest Room",
        "users": ["Guest"],
        "max_streams": 1,
        "current_streams": 0,
        "status": "inactive",
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
