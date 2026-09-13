# Streaming Household Manager

A Python-based management tool for controlling and monitoring streaming services across multiple households.

## 🎯 Features

- **Multi-Household Management** - Track streaming across different rooms/households
- **Stream Limit Control** - Set maximum concurrent streams per household
- **Service Monitoring** - Check health of your streaming services
- **Activity Logging** - Record all streaming actions
- **Simple to Understand** - Built for beginners with detailed comments

## 📂 Project Structure

```
streaming-household-manager/
├── config.py              # Configuration file with household data
├── streaming_manager.py   # Main logic and control functions
├── main.py               # Demo application
├── GUIDE.md              # Beginner's guide (START HERE!)
└── README.md             # This file
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/juneryguape19-blip/streaming-household-manager.git
cd streaming-household-manager
```

### 2. Run the Demo
```bash
python main.py
```

You'll see a demo showing:
- System summary
- Household status
- Starting/stopping streams
- Service health checks

### 3. Read the Guide
Open `GUIDE.md` to understand:
- How the code works
- What each file does
- Programming concepts explained simply
- Real-world examples

## 📖 Learning Path

1. **Start:** Read `GUIDE.md`
2. **Explore:** Look at `config.py` (the settings)
3. **Understand:** Read `streaming_manager.py` (the logic)
4. **Run:** Execute `main.py` (see it in action)
5. **Modify:** Change settings and run again to see different results

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
result = manager.start_stream("household_1", "Mom", "Movie Title")
print(result)
```

### Stop a Stream
```python
result = manager.stop_stream("household_1")
print(result)
```

### Get System Summary
```python
summary = manager.get_summary()
print(f"Active streams: {summary['total_active_streams']}")
```

## 🔧 Customization

Edit `config.py` to:
- Add/remove households
- Change household names
- Adjust max streams per household
- Add your actual service URLs and API keys
- Configure logging

## 📝 What's Included

- ✅ Configuration management
- ✅ Stream control (start/stop)
- ✅ Status monitoring
- ✅ Service health checks
- ✅ Activity logging
- ✅ Comprehensive documentation
- ✅ Working demo

## 🎓 Learning Programming

This project teaches:
- How to organize code (files and functions)
- How to use dictionaries to store data
- How to write functions that do specific tasks
- How to use classes to group related functions
- How to use if statements for decision making
- How to use loops to repeat actions

## 🔮 Future Enhancements

You could add:
- Web interface (Flask, Django)
- Database integration (SQLite, PostgreSQL)
- Real API integration (aiostream, Torbox)
- User authentication
- Advanced scheduling
- Analytics and reporting
- Email notifications

## 📚 Resources

- **Python Guide:** https://www.python.org/about/gettingstarted/
- **GitHub Guide:** https://guides.github.com/
- **Programming Basics:** https://www.codecademy.com/

## 🤝 Contributing

This is a learning project. Feel free to:
- Suggest improvements
- Report bugs
- Ask questions
- Create your own version

## 📄 License

This project is open source and available for learning purposes.

---

**Start with GUIDE.md to learn how everything works!** 🚀
