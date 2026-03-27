#!/usr/bin/env python3
"""
Jarves Configuration
"""

import os
import yaml
from pathlib import Path


class Config:
    """Configuration manager"""
    
    def __init__(self):
        self.config_dir = Path(__file__).parent.parent / "config"
        self.data_dir = Path(__file__).parent.parent / "data"
        self.logs_dir = Path(__file__).parent.parent / "logs"
        
        # Create directories
        self.config_dir.mkdir(exist_ok=True)
        self.data_dir.mkdir(exist_ok=True)
        self.logs_dir.mkdir(exist_ok=True)
        
        # Default config
        self.settings = {
            "name": "Jarves",
            "user_name": os.getenv("USER", "sir").capitalize(),
            "ai_model": "llama3.2",
            "ollama_url": "http://localhost:11434",
            "voice_enabled": True,
            "wake_word": "hey jarves",
            "log_level": "INFO",
            "auto_organize": False,
        }
        
        self._load_config()
    
    def _load_config(self):
        """Load config from file"""
        config_file = self.config_dir / "settings.yaml"
        if config_file.exists():
            try:
                with open(config_file) as f:
                    loaded = yaml.safe_load(f)
                    if loaded:
                        self.settings.update(loaded)
            except Exception as e:
                print(f"Could not load config: {e}")
    
    def save_config(self):
        """Save config to file"""
        config_file = self.config_dir / "settings.yaml"
        with open(config_file, "w") as f:
            yaml.dump(self.settings, f, default_flow_style=False)
    
    def get(self, key, default=None):
        """Get config value"""
        return self.settings.get(key, default)
    
    def set(self, key, value):
        """Set config value"""
        self.settings[key] = value
        self.save_config()
