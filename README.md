# 🤖 Jarves - Personal AI Assistant

> "Your own Jarvis, but make it real."

## Features

- 💬 **Chat Interface** - Text-based conversation
- 🎙️ **Voice Commands** - Speak to control
- 📋 **Task Management** - Organize your life
- ⚙️ **System Control** - Manage your computer
- 🧠 **AI Powered** - Local LLM integration (Ollama)

## Architecture

```
jarves/
├── core/           - Main brain & orchestrator
├── modules/        - Feature modules
│   ├── chat/       - Chat interface
│   ├── voice/      - Voice recognition/synthesis
│   ├── tasks/      - Task management
│   └── system/     - System commands
├── web/            - Web dashboard
├── config/         - Configuration files
├── logs/           - Activity logs
└── data/           - Persistent data
```

## Quick Start

```bash
cd ~/Projects/Code/jarves
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 jarves.py
```

## Commands

| Command | Action |
|---------|--------|
| `jarves chat` | Start chat mode |
| `jarves voice` | Start voice mode |
| `jarves task add "Buy milk"` | Add task |
| `jarves system status` | System info |

## Configuration

Edit `config/settings.yaml` to customize behavior.
