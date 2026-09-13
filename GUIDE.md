# Streaming Household Manager - Beginner's Guide

Welcome! This guide explains how this code works, even if you have no IT background.

---

## 📚 What Is This Project?

This is a **management tool** for controlling streaming across multiple households. Think of it like a manager that:
- Keeps track of who's watching what
- Makes sure no household exceeds their stream limit
- Monitors the health of your services
- Records what happens (logging)

---

## 🏗️ How It's Organized

### File 1: `config.py` (Configuration)
**What it does:** Stores all the settings and information

Think of it like a **notebook** that contains:
- List of households (Living Room, Bedroom, Guest Room)
- How many people live in each household
- Maximum streams allowed per household
- Information about your streaming services

```python
HOUSEHOLDS = {
    "household_1": {
        "name": "Living Room",
        "users": ["Mom", "Dad"],
        "max_streams": 2,           # Can watch 2 things at once
        "current_streams": 1,       # Currently watching 1 thing
        "status": "active"
    }
}
```

**Why separate it?** If you need to change information, you don't have to touch the complicated code — just edit this file!

---

### File 2: `streaming_manager.py` (The Control Center)
**What it does:** Contains the logic and rules

This is like the **brain** of your system. It has a class called `StreamingManager` that can:

1. **Check Status** → `get_household_status("household_1")`
   - Tells you what's happening in a specific household
   - Shows available slots for new streams

2. **Start a Stream** → `start_stream("household_1", "Mom", "Netflix Show")`
   - Someone wants to watch something
   - Checks if there's room (within the limit)
   - Starts the stream if allowed

3. **Stop a Stream** → `stop_stream("household_1")`
   - Someone stops watching
   - Frees up a slot

4. **Check Services** → `check_service_health()`
   - Makes sure your aiostream, Torbox, etc. are working

5. **Keep Records** → `log_action()`
   - Records everything that happens (for troubleshooting later)

---

### File 3: `main.py` (The Demo)
**What it does:** Shows how to USE everything

This is like a **tutorial** that demonstrates:
1. Getting a summary of everything
2. Checking all households
3. Starting streams
4. Handling errors (like when max streams is reached)
5. Stopping streams
6. Checking services

**To run it:** Open terminal and type:
```bash
python main.py
```

You'll see the demo in action!

---

## 🔄 How It All Works Together

```
[config.py] ← Stores data
    ↓
[streaming_manager.py] ← Uses the data and applies logic
    ↓
[main.py] ← Calls streaming_manager and shows results
```

**Example Flow:**
1. `config.py` says "Household 1 can have max 2 streams"
2. User tries to start stream #3 in Household 1
3. `streaming_manager.py` checks: "2 already running, max is 2... REJECTED"
4. `main.py` shows: "Error: Max streams reached"

---

## 💡 Key Programming Concepts Explained

### 1. **Dictionary** (Like a phonebook)
```python
HOUSEHOLDS = {
    "household_1": { "name": "Living Room", ... },
    "household_2": { "name": "Bedroom", ... }
}
```
- "household_1" is the **key** (name/label)
- All the info about it is the **value** (the data)

### 2. **Function** (Like a recipe)
```python
def start_stream(self, household_id, user_name, content_title):
    # Do things here
    return result
```
- Takes in information (ingredients)
- Does something with it
- Gives back a result (the meal)

### 3. **Class** (Like a blueprint)
```python
class StreamingManager:
    def __init__(self):
        # Initialize
    def start_stream(self):
        # Start stream
    def stop_stream(self):
        # Stop stream
```
- Groups related functions together
- Has data and methods (functions) in one place

### 4. **If Statement** (Decision making)
```python
if household["current_streams"] >= household["max_streams"]:
    return {"error": "Max streams reached"}
```
- Checks a condition
- Does something if it's true
- Does something else if it's false

### 5. **Loop** (Repeat)
```python
for household_id in self.households:
    # Do something for each household
```
- Goes through a list one by one
- Does the same thing to each item

---

## 🎯 Real-World Example

**Scenario:** Mom wants to watch Netflix in the Living Room

1. **Call function:** `manager.start_stream("household_1", "Mom", "Netflix Show")`

2. **What happens inside:**
   ```
   Check: Does household_1 exist? YES
   Check: Is it active? YES
   Check: Current streams (1) < Max streams (2)? YES
   Action: Add 1 to current_streams (now it's 2)
   Log: "Stream started: Mom in Living Room - Netflix Show"
   Return: Success message
   ```

3. **Result:** Mom can watch! ✅

4. **Next scenario:** Dad also wants to watch
   1. Call: `manager.start_stream("household_1", "Dad", "Sports")`
   2. Current streams: 2, Max: 2
   3. Result: SUCCESS! ✅ (now 2 streams active)

5. **Another scenario:** Sister wants to watch
   1. Call: `manager.start_stream("household_1", "Sister", "Game")`
   2. Current streams: 2, Max: 2
   3. Check: 2 >= 2? YES
   4. Result: ERROR ❌ "Max streams reached"

---

## 🚀 How To Extend This

Once you understand these basics, you can:

1. **Add more households** in `config.py`
2. **Add more functions** in `streaming_manager.py` (like user management, billing, etc.)
3. **Connect to real services** (call the actual aiostream API, Torbox API, etc.)
4. **Create a web interface** so you can use it in your browser instead of command line
5. **Add a database** to permanently save records

---

## 📝 Summary

- **config.py** = Data/Settings
- **streaming_manager.py** = Logic/Rules
- **main.py** = Demo/Usage
- **Classes** = Blueprints for organizing code
- **Functions** = Reusable recipes
- **Dictionaries** = Data storage (keys and values)

That's the foundation! Everything in programming builds on these concepts. 🎉

---

## ❓ Questions?

Go to the repository issues and ask! The community is here to help.
