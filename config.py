# Configuration file for streaming households
# This file stores settings for your streaming service

# Dictionary to store household information
HOUSEHOLDS = {
    "household_1": {
        "name": "Living Room",
        "users": ["Mom", "Dad"],
        "max_streams": 2,
        "current_streams": 1,
        "status": "active"
    },
    "household_2": {
        "name": "Bedroom",
        "users": ["Son"],
        "max_streams": 1,
        "current_streams": 0,
        "status": "active"
    },
    "household_3": {
        "name": "Guest Room",
        "users": ["Guest"],
        "max_streams": 1,
        "current_streams": 0,
        "status": "inactive"
    }
}

# Streaming service settings
STREAMING_SERVICES = {
    "aiostream": {
        "url": "http://your-aiostream-instance.com",
        "api_key": "YOUR_API_KEY_HERE",
        "status": "active"
    },
    "torbox": {
        "service_type": "debrid",
        "active_plans": 3,
        "status": "active"
    }
}

# Log settings
LOG_FILE = "streaming_manager.log"
DEBUG_MODE = True
