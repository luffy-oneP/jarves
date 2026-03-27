#!/usr/bin/env python3
"""
Chat Module - Text-based interaction with Ollama AI
"""

import json
import requests
from datetime import datetime


class ChatModule:
    """Handle chat conversations with AI"""
    
    def __init__(self, brain):
        self.brain = brain
        self.history = []
        self.max_history = 10
        self.ollama_url = "http://localhost:11434"
        self.model = brain.config.get("ai_model", "llama3.2")
        
        # System prompt for Jarves personality
        self.system_prompt = """You are Jarves, a helpful AI assistant. You are:
- Friendly and professional
- Concise but informative
- Good at system administration, coding, and organization
- Running on a Kali Linux system

Keep responses brief and actionable. If you don't know something, say so."""
    
    def chat(self, message):
        """Process chat message"""
        # Add to history
        self.history.append({"role": "user", "content": message, "time": datetime.now()})
        
        # Get response from AI
        response = self._generate_response(message)
        
        # Add response to history
        self.history.append({"role": "assistant", "content": response, "time": datetime.now()})
        
        # Trim history
        if len(self.history) > self.max_history * 2:
            self.history = self.history[-self.max_history * 2:]
        
        return response
    
    def _generate_response(self, message):
        """Generate AI response using Ollama"""
        try:
            # Build conversation context
            conversation = f"{self.system_prompt}\n\n"
            
            # Add recent history for context
            for item in self.history[-6:]:  # Last 6 exchanges
                role = "User" if item["role"] == "user" else "Jarves"
                conversation += f"{role}: {item['content']}\n"
            
            conversation += f"User: {message}\nJarves:"
            
            # Call Ollama API
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": conversation,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_predict": 500
                    }
                },
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                ai_response = data.get("response", "").strip()
                if ai_response:
                    return ai_response
            
        except requests.exceptions.ConnectionError:
            return "⚠ Ollama is not running. Start it with: ollama serve"
        except Exception as e:
            print(f"AI Error: {e}")
        
        # Fallback to simple responses
        return self._fallback_response(message)
    
    def _fallback_response(self, message):
        """Simple fallback responses when AI is unavailable"""
        message = message.lower()
        
        responses = {
            "hello": f"Hello, {self.brain.user_name}! How can I help you today?",
            "hi": f"Hi there! What can I do for you?",
            "help": "I can help with:\n- Tasks: 'add task buy milk'\n- System: 'system status'\n- Files: 'organize files'\n- Chat: Ask me anything!",
            "time": f"It's {datetime.now().strftime('%I:%M %p')}.",
            "date": f"Today is {datetime.now().strftime('%A, %B %d, %Y')}.",
            "who are you": "I am Jarves, your personal AI assistant. I'm here to help you with tasks, system management, and answering questions.",
            "what can you do": "I can:\n- Manage your tasks and reminders\n- Check system status\n- Organize files\n- Answer questions using AI\n- Control your system with voice or text",
        }
        
        for key, value in responses.items():
            if key in message:
                return value
        
        return f"I'm not sure I understand '{message}'. Try 'help' to see what I can do, or ask me a question!"
    
    def get_history(self):
        """Get chat history"""
        return self.history
    
    def clear_history(self):
        """Clear chat history"""
        self.history = []
        return "Chat history cleared."
    
    def check_ollama(self):
        """Check if Ollama is running"""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get("models", [])
                model_names = [m["name"] for m in models]
                return f"✓ Ollama running. Available models: {', '.join(model_names)}"
            return "⚠ Ollama responded but status unclear"
        except:
            return "⚠ Ollama not running. Start with: ollama serve"
