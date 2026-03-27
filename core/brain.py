#!/usr/bin/env python3
"""
Jarves Brain - Core orchestrator
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path


class JarvesBrain:
    """Main AI assistant brain"""
    
    def __init__(self, config):
        self.config = config
        self.name = "Jarves"
        self.user_name = os.getenv("USER", "sir").capitalize()
        self.context = []
        
        # Initialize modules
        self._init_modules()
    
    def _init_modules(self):
        """Load all modules"""
        try:
            from modules.chat.chat_module import ChatModule
            from modules.tasks.task_module import TaskModule
            from modules.system.system_module import SystemModule
            from modules.voice.voice_module import VoiceModule
            
            self.chat = ChatModule(self)
            self.tasks = TaskModule(self)
            self.system = SystemModule(self)
            self.voice = VoiceModule(self)
            
            print(f"✓ All modules loaded successfully")
        except Exception as e:
            print(f"⚠ Some modules not available: {e}")
            self.chat = None
            self.tasks = None
            self.system = None
            self.voice = None
    
    def greet(self):
        """Welcome message"""
        hour = datetime.now().hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 17:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        
        return f"{greeting}, {self.user_name}. {self.name} at your service."
    
    def process_command(self, command):
        """Process natural language command"""
        command = command.lower().strip()
        
        # Task commands
        if any(word in command for word in ["task", "todo", "remind"]):
            return self._handle_task_command(command)
        
        # System commands
        if any(word in command for word in ["system", "status", "info", "check"]):
            return self._handle_system_command(command)
        
        # File commands
        if any(word in command for word in ["file", "folder", "organize", "clean"]):
            return self._handle_file_command(command)
        
        # Time/Date
        if any(word in command for word in ["time", "date", "day"]):
            return self._handle_time_command(command)
        
        # Default: chat response
        return self._get_ai_response(command)
    
    def _handle_task_command(self, command):
        """Handle task-related commands"""
        if self.tasks:
            if "add" in command or "create" in command:
                # Extract task text
                task_text = command.replace("add task", "").replace("create task", "").strip()
                if task_text:
                    return self.tasks.add_task(task_text)
                return "What task would you like me to add?"
            
            elif "list" in command or "show" in command:
                return self.tasks.list_tasks()
            
            elif "done" in command or "complete" in command:
                return self.tasks.complete_task()
            
            else:
                return self.tasks.list_tasks()
        return "Task module not available."
    
    def _handle_system_command(self, command):
        """Handle system commands"""
        if self.system:
            return self.system.get_status()
        return "System module not available."
    
    def _handle_file_command(self, command):
        """Handle file organization commands"""
        if "organize" in command or "clean" in command:
            return self._organize_files()
        return "I can organize your Downloads folder. Just say 'organize files'."
    
    def _handle_time_command(self, command):
        """Handle time/date queries"""
        now = datetime.now()
        if "time" in command:
            return f"The current time is {now.strftime('%I:%M %p')}."
        elif "date" in command:
            return f"Today is {now.strftime('%A, %B %d, %Y')}."
        return f"It's {now.strftime('%A, %B %d, %Y')} at {now.strftime('%I:%M %p')}."
    
    def _get_ai_response(self, command):
        """Get AI response from chat module"""
        if self.chat:
            return self.chat.chat(command)
        
        # Fallback if chat module not available
        return f"I'm {self.name}, your AI assistant. Chat module is initializing..."
    
    def _organize_files(self):
        """Organize Downloads folder"""
        downloads = Path.home() / "Downloads"
        organized = {"images": 0, "documents": 0, "archives": 0, "other": 0}
        
        # Create folders
        (downloads / "Images").mkdir(exist_ok=True)
        (downloads / "Documents").mkdir(exist_ok=True)
        (downloads / "Archives").mkdir(exist_ok=True)
        
        for file in downloads.iterdir():
            if file.is_file():
                ext = file.suffix.lower()
                if ext in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
                    file.rename(downloads / "Images" / file.name)
                    organized["images"] += 1
                elif ext in [".pdf", ".doc", ".docx", ".txt"]:
                    file.rename(downloads / "Documents" / file.name)
                    organized["documents"] += 1
                elif ext in [".zip", ".tar", ".gz", ".rar"]:
                    file.rename(downloads / "Archives" / file.name)
                    organized["archives"] += 1
        
        return f"Organized {sum(organized.values())} files: {organized['images']} images, {organized['documents']} documents, {organized['archives']} archives."
    
    def run_chat_mode(self):
        """Interactive chat mode"""
        print(f"\n{self.greet()}")
        print("Type 'exit' to quit, 'help' for commands.\n")
        
        while True:
            try:
                user_input = input(f"{self.user_name}: ").strip()
                
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print(f"{self.name}: Goodbye, {self.user_name}!")
                    break
                
                if user_input:
                    response = self.process_command(user_input)
                    print(f"{self.name}: {response}\n")
                    
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye!")
                break
            except EOFError:
                break
    
    def run_voice_mode(self):
        """Voice interaction mode"""
        if self.voice:
            self.voice.start_listening()
        else:
            print("Voice module not available. Install dependencies:")
            print("pip install speechrecognition pyttsx3 pyaudio")
    
    def run_web_mode(self):
        """Web dashboard mode"""
        print("Starting web dashboard...")
        print("Open http://localhost:5000 in your browser")
        # Would start Flask server here
    
    def handle_task(self, action, text):
        """CLI task handler"""
        if self.tasks:
            if action == "add":
                print(self.tasks.add_task(text))
            elif action == "list":
                print(self.tasks.list_tasks())
            elif action == "done":
                print(self.tasks.complete_task())
            elif action == "remove":
                print(self.tasks.remove_task())
    
    def handle_system(self, action):
        """CLI system handler"""
        if self.system:
            if action == "status":
                print(self.system.get_status())
            elif action == "info":
                print(self.system.get_info())
            elif action == "clean":
                print(self.system.clean_system())
