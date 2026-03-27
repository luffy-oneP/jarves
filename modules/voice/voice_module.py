#!/usr/bin/env python3
"""
Voice Module - Speech recognition and synthesis
"""

import os
import sys
import subprocess
from pathlib import Path


class VoiceModule:
    """Handle voice commands and responses"""
    
    def __init__(self, brain):
        self.brain = brain
        self.recognizer = None
        self.microphone = None
        self.tts_engine = None
        self._init_voice()
    
    def _init_voice(self):
        """Initialize voice recognition"""
        try:
            import speech_recognition as sr
            import pyttsx3
            
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            self.tts_engine = pyttsx3.init()
            
            # Configure TTS
            self.tts_engine.setProperty('rate', 150)
            self.tts_engine.setProperty('volume', 0.9)
            
            # Calibrate for ambient noise
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
            
            print("✓ Voice module initialized")
        except ImportError as e:
            print(f"⚠ Voice dependencies not installed: {e}")
            print("  Run: pip install SpeechRecognition pyttsx3 PyAudio")
    
    def speak(self, text):
        """Text to speech"""
        if self.tts_engine:
            print(f"🗣️  Jarves: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        else:
            print(f"🗣️  Jarves: {text}")
    
    def listen(self, timeout=5):
        """Listen for voice command"""
        if not self.recognizer or not self.microphone:
            return None
        
        try:
            print("🎤 Listening...")
            with self.microphone as source:
                audio = self.recognizer.listen(source, timeout=timeout)
            
            print("🔄 Processing...")
            text = self.recognizer.recognize_google(audio)
            print(f"👤 You said: {text}")
            return text
            
        except Exception as e:
            print(f"⚠ Could not understand: {e}")
            return None
    
    def start_listening(self):
        """Start voice interaction loop"""
        self.speak(f"Hello {self.brain.user_name}. I'm listening for commands.")
        
        while True:
            try:
                command = self.listen()
                
                if command:
                    if any(word in command.lower() for word in ["exit", "quit", "bye", "goodbye"]):
                        self.speak("Goodbye!")
                        break
                    
                    # Process command
                    response = self.brain.process_command(command)
                    self.speak(response)
                
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break
    
    def is_available(self):
        """Check if voice is available"""
        return self.recognizer is not None and self.tts_engine is not None
