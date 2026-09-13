# Streaming Household Manager - Beginner's Guide

Welcome! This guide explains the updated project as a **Windows-based multi-household media manager**.

---

## 📚 What Is This Project?

This project keeps playback organized across households from one Windows machine. It is designed to:
- Track which household is using which stream slot
- Pick an allowed provider for each household
- Prefer a local remux media server before remote libraries
- Keep a simple session history while the app is running

---

## 🏗️ How It's Organized

### File 1: `config.py`
Stores the settings for:
- Your Windows host
- Household stream limits
- Allowed providers per household
- Provider connection details and priority

### File 2: `streaming_manager.py`
This is the control center. It can:
1. Read the configuration
2. Choose the best provider for a household
3. Start and stop playback sessions
4. Check provider readiness
5. Summarize the overall system

### File 3: `main.py`
A simple demo that shows:
1. System summary
2. Household status
3. Provider health
4. Starting streams
5. Handling stream limit errors
6. Stopping streams

---

## 🔄 How It Works Together

```text
[config.py] settings
    ↓
[streaming_manager.py] household rules + provider selection
    ↓
[main.py] demo output
```

---

## 🎯 Example Flow

1. Household 1 requests playback.
2. The manager checks whether the household is active.
3. The manager checks whether the household still has an available slot.
4. The manager picks the best active provider from the household's allowed list.
5. The manager stores a session entry and updates the current stream count.

---

## 💡 Key Concepts

### Household Rules
Each household has:
- a name
- users
- a maximum number of streams
- a list of allowed providers
- a list of current sessions

### Provider Priority
The Windows host configuration defines the preferred order:
1. `remux_media_server`
2. `webdav_library`
3. `torbox_cloud`
4. `debrid_vault`

The manager uses that order unless you request a specific provider.

### Session Tracking
Each started stream creates a session record with:
- session ID
- user
- content title
- provider used
- start time

---

## 🚀 What To Customize First

Open `/home/runner/work/streaming-household-manager/streaming-household-manager/config.py` and update:
- `WINDOWS_HOST`
- your library paths
- your endpoint URLs
- the households you want to manage
- the allowed providers for each household

---

## 📝 Summary

- `config.py` = settings
- `streaming_manager.py` = rules and state changes
- `main.py` = example usage

Once you are comfortable with this version, the next practical step is adding a simple API or web UI.
