# 🚀 Jarves - 3D Personal AI Assistant

<blockquote>"Your own Jarvis, but make it real — now in sleek 3D mode."</blockquote>

---

## ✨ What’s New: Modern 3D Look-and-Feel

- 🎛️ Futuristic gradient UI, real-time feedback, crisp atomized controls
- 🚀 Modular plugin-style architecture with visual 3D nodes
- 🛡️ Secure local AI inference (Ollama-compatible) in isolated sandbox
- 🗂️ Integrated task + voice + system automation, all synchronized

---

## 🧠 Core Architecture (3D mental map)

```text
                 ┌─────────────┐
                 │  jarves.py  │
                 │  entrypoint │
                 └──────┬──────┘
                        │
       ┌────────────────┴────────────────┐
       │                                 │
  ┌────┴────┐                       ┌────┴─────┐
  │  core/   │                       │ config/  │
  │ engine   │                       │ settings │
  └────┬────┘                       └──────────┘
       │
┌──────┴───────────┐
│   modules/       │
│ ┌──────────────┐ │
│ │ chat/        │ │
│ │ voice/       │ │
│ │ tasks/       │ │
│ │ system/      │ │
│ └──────────────┘ │
└──────────────────┘
```

---

## ⚡ Quick Start (One-liner)

```bash
git clone https://github.com/<your>/<repo>.git && cd jarves && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python3 jarves.py
```

### Or step-by-step

1. `cd /path/to/jarves`
2. `python3 -m venv .venv`
3. `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python3 jarves.py`

---

## 🛠️ Commands

| Command                                   | Purpose               |
| ----------------------------------------- | --------------------- |
| `python3 jarves.py --mode chat`           | Start chat UI         |
| `python3 jarves.py --mode voice`          | Start voice interface |
| `python3 jarves.py --task add "Buy milk"` | Add a task            |
| `python3 jarves.py --system status`       | System diagnostics    |

---

## ⚙️ Customize Configuration

- `config/settings.yaml` for runtime behavior
- `config/llm.yaml` (if present) for model endpoint and GPU/CPU profile

## 📦 Development

- `core/brain.py` – orchestrator and command router
- `modules/*` – feature modules (chat / voice / tasks / system)
- `jarves.py` – CLI + startup

---

## 💡 Pro tips

- Use `python3 -m pip install --upgrade pip` before first install.
- Add `alias jarves='python3 /path/to/jarves/jarves.py'` for easy access.
- Persist logs in `logs/` and snapshots in `data/` for long-term AI memory.
