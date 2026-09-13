# Streaming Household Manager

A Python-based Windows household media manager for coordinating playback across multiple households using self-hosted or licensed library sources.

## 🎯 Features

- **Central Windows Host** - Keep provider settings and media paths on one machine
- **Multi-Household Management** - Track limits and sessions per household
- **Provider Routing** - Prefer your remux media server first, then fall back to WebDAV or cloud libraries
- **Session Tracking** - Record which user started which title and through which provider
- **Service Monitoring** - Check whether configured providers are active and ready
- **Beginner Friendly** - Simple Python files with detailed examples

## 📂 Project Structure

```text
streaming-household-manager/
├── config.py              # Windows host, household, and provider settings
├── streaming_manager.py   # Main logic and control functions
├── main.py                # Demo application
├── GUIDE.md               # Beginner's guide
└── README.md              # This file
```

## 🚀 Quick Start

### 1. Run the Demo
```bash
python main.py
```

### 2. Customize the Configuration
Edit `/home/runner/work/streaming-household-manager/streaming-household-manager/config.py` to:
- Set your Windows host name and media paths
- Choose the preferred provider order
- Add or remove households
- Control allowed providers per household
- Replace placeholder library endpoints with your own licensed or self-hosted sources

## 💻 Usage Examples

### Check Household Status
```python
from streaming_manager import StreamingManager

manager = StreamingManager()
status = manager.get_household_status("household_1")
print(status)
```

### Start a Stream
```python
result = manager.start_stream("household_1", "Mom", "Licensed Movie Night")
print(result)
```

### Prefer a Specific Provider
```python
result = manager.start_stream(
    "household_1",
    "Dad",
    "Concert Recording",
    preferred_provider="webdav_library",
)
print(result)
```

### Stop a Stream
```python
result = manager.stop_stream("household_1")
print(result)
```

## 🔧 Included Providers

The default configuration models these provider types:
- `remux_media_server`
- `webdav_library`
- `torbox_cloud`
- `debrid_vault`

They are treated as configurable library backends, not direct peer-to-peer playback engines.

## 📚 What This Project Teaches

- How to separate configuration from application logic
- How to manage state for multiple households
- How to select between multiple backends with a simple priority order
- How to log and summarize application activity

## 🔮 Next Steps

You could extend this project with:
- A small Flask or FastAPI control panel
- Persistent storage for sessions
- Real provider API integrations
- Windows service packaging
- Household-specific access policies
