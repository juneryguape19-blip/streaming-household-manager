# Streaming Household Manager - Beginner's Guide

Welcome! This guide explains the updated project as a **Windows-based multi-household media manager** with built-in plan categories.

---

## 📚 What Is This Project?

This project keeps playback organized across households from one Windows machine. It is designed to:
- Track which household is using which stream slot
- Assign each household to a recommended plan tier
- Pick an allowed provider for each household
- Prefer a local remux media server before remote libraries
- Keep a simple session history while the app is running

---

## 🏗️ How It's Organized

### File 1: `config.py`
Stores the settings for:
- Your Windows host
- Plan categories
- Household stream limits
- Allowed providers per household
- Provider connection details and priority

### File 2: `streaming_manager.py`
This is the control center. It can:
1. Read the configuration
2. Show the Basic, HD/FHD, and 4K plan recommendations
3. Choose the best provider for a household
4. Start and stop playback sessions
5. Check provider readiness
6. Summarize the overall system

### File 3: `main.py`
A simple demo that shows:
1. System summary
2. Plan categories
3. Household status
4. Provider health
5. Starting streams
6. Handling stream limit errors
7. Stopping streams

---

## 🧭 Plan Categories

### Basic Plan
- Recommended app: `Jellyfin`
- Target quality: HD / FHD
- Best for: one-time setup with no monthly app fee

### HD / FHD Plan
- Recommended app: `Jellyfin`
- Alternate app: `Plex`
- Target quality: HD / FHD
- Best for: balanced quality and easier multi-household sharing

### 4K Plan
- Recommended app: `Plex`
- Alternate app: `Jellyfin`
- Target quality: 4K / HDR
- Best for: premium direct-play quality on capable devices

---

## 🔄 How It Works Together

```text
[config.py] settings + plan categories
    ↓
[streaming_manager.py] household rules + provider selection
    ↓
[main.py] demo output
```

---

## 🎯 Example Flow

1. Household 1 is assigned to the `4k` plan.
2. The manager checks whether the household is active.
3. The manager checks whether the household still has an available slot.
4. The manager picks the best active provider from the household's allowed list.
5. The manager stores a session entry with the household's plan category.

---

## 💡 Key Concepts

### Plan Category
Each plan stores:
- recommended app
- target quality
- primary provider
- fallback providers
- hardware guidance

### Household Rules
Each household has:
- a name
- users
- a maximum number of streams
- a plan category
- a list of allowed providers
- a list of current sessions

### Provider Priority
The Windows host configuration defines the preferred order:
1. `remux_media_server`
2. `webdav_library`
3. `torbox_cloud`
4. `debrid_vault`

The manager uses that order unless you request a specific provider.

---

## 🚀 What To Customize First

Open `/home/runner/work/streaming-household-manager/streaming-household-manager/config.py` and update:
- `WINDOWS_HOST`
- `PLAN_CATEGORIES`
- your library paths
- your endpoint URLs
- the households you want to manage
- the allowed providers for each household

---

## 📝 Summary

- `config.py` = settings and plan tiers
- `streaming_manager.py` = rules and state changes
- `main.py` = example usage

Once you are comfortable with this version, the next practical step is adding a simple API or web UI.
