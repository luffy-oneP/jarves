# 🤖 Jarves Commands

## Quick Start

```bash
# Setup (first time only)
cd ~/Projects/Code/jarves
./setup.sh

# Activate environment
source venv/bin/activate

# Run Jarves
python3 jarves.py
```

## Commands

### Chat Mode (Default)
```bash
python3 jarves.py
# or
python3 jarves.py --mode chat
```

### Voice Mode
```bash
python3 jarves.py --mode voice
```

### Task Management
```bash
# Add task
python3 jarves.py task add "Buy groceries"

# List tasks
python3 jarves.py task list

# Complete task
python3 jarves.py task done

# Remove task
python3 jarves.py task remove
```

### System Commands
```bash
# System status
python3 jarves.py system status

# System info
python3 jarves.py system info

# Clean system
python3 jarves.py system clean
```

## Chat Examples

Once in chat mode, try:

| You Say | Jarves Does |
|---------|-------------|
| "add task buy milk" | Adds to task list |
| "show tasks" | Lists all tasks |
| "system status" | Shows CPU, memory, disk |
| "organize files" | Organizes Downloads folder |
| "what time is it" | Tells current time |
| "help" | Shows help message |

## Voice Commands

Say the wake word: **"Hey Jarves"**

Then commands like:
- "Add task call mom"
- "What's the system status"
- "Organize my files"
- "What time is it"

## Project Structure

```
jarves/
├── jarves.py           # Main entry point
├── core/
│   ├── brain.py        # AI brain
│   └── config.py       # Configuration
├── modules/
│   ├── chat/           # Text chat
│   ├── voice/          # Voice recognition
│   ├── tasks/          # Task management
│   └── system/         # System control
├── config/
│   └── settings.yaml   # Your settings
├── data/
│   └── tasks.json      # Saved tasks
└── logs/
    └── jarves.log      # Activity log
```

## Customization

Edit `config/settings.yaml`:
- Change `user_name` to your name
- Set `ai_model` (requires Ollama)
- Enable/disable features

## Troubleshooting

**Voice not working?**
```bash
sudo apt install portaudio19-dev
pip install PyAudio
```

**AI not responding?**
- Make sure Ollama is running: `ollama serve`
- Check if model is downloaded: `ollama list`

**Permission denied?**
```bash
chmod +x jarves.py setup.sh
```
