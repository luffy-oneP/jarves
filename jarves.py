#!/usr/bin/env python3
"""
Jarves - Personal AI Assistant
Main entry point
"""

import sys
import argparse
from pathlib import Path

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent / "modules"))

from core.brain import JarvesBrain
from core.config import Config


def main():
    parser = argparse.ArgumentParser(description="Jarves - Your Personal AI Assistant")
    parser.add_argument("--mode", choices=["chat", "voice", "web"], default="chat",
                       help="Interaction mode")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Task commands
    task_parser = subparsers.add_parser("task", help="Task management")
    task_parser.add_argument("action", choices=["add", "list", "done", "remove"])
    task_parser.add_argument("text", nargs="?", help="Task description")
    
    # System commands
    sys_parser = subparsers.add_parser("system", help="System commands")
    sys_parser.add_argument("action", choices=["status", "info", "clean"])
    
    args = parser.parse_args()
    
    # Initialize Jarves
    config = Config()
    jarves = JarvesBrain(config)
    
    print("""
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║     🤖 JARVES ACTIVATED              ║
    ║                                       ║
    ║     "At your service, sir."           ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    """)
    
    if args.command == "task":
        jarves.handle_task(args.action, args.text)
    elif args.command == "system":
        jarves.handle_system(args.action)
    elif args.mode == "chat":
        jarves.run_chat_mode()
    elif args.mode == "voice":
        jarves.run_voice_mode()
    elif args.mode == "web":
        jarves.run_web_mode()
    else:
        jarves.run_chat_mode()


if __name__ == "__main__":
    main()
