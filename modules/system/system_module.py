#!/usr/bin/env python3
"""
System Module - System monitoring and control
"""

import os
import psutil
import subprocess
import shutil
from datetime import datetime
from pathlib import Path


class SystemModule:
    """System monitoring and control"""
    
    def __init__(self, brain):
        self.brain = brain
    
    def get_status(self):
        """Get system status"""
        # CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        
        # Memory
        memory = psutil.virtual_memory()
        
        # Disk
        disk = psutil.disk_usage("/")
        
        # Network
        net_io = psutil.net_io_counters()
        
        # Uptime
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        
        status = f"""📊 System Status

🖥️  CPU: {cpu_percent}% ({cpu_count} cores)
💾 Memory: {self._format_bytes(memory.used)} / {self._format_bytes(memory.total)} ({memory.percent}%)
💿 Disk: {self._format_bytes(disk.used)} / {self._format_bytes(disk.total)} ({disk.percent}%)
🌐 Network: ↓{self._format_bytes(net_io.bytes_recv)} ↑{self._format_bytes(net_io.bytes_sent)}
⏱️  Uptime: {str(uptime).split('.')[0]}

🔋 Battery: {self._get_battery_status()}
🌡️  Temperature: {self._get_temperature()}
"""
        return status
    
    def get_info(self):
        """Get detailed system info"""
        info = f"""🔍 System Information

OS: {os.uname().sysname} {os.uname().release}
Hostname: {os.uname().nodename}
Architecture: {os.uname().machine}
Python: {os.sys.version.split()[0]}
User: {os.getenv('USER')}
Home: {os.getenv('HOME')}
Shell: {os.getenv('SHELL', 'unknown')}
"""
        return info
    
    def clean_system(self):
        """Clean temporary files"""
        cleaned = 0
        
        # Clean temp directories
        temp_dirs = ['/tmp', '/var/tmp']
        for temp_dir in temp_dirs:
            if os.path.exists(temp_dir):
                try:
                    for item in Path(temp_dir).iterdir():
                        if item.is_file():
                            item.unlink()
                            cleaned += 1
                except:
                    pass
        
        # Clean user cache
        cache_dir = Path.home() / ".cache"
        if cache_dir.exists():
            try:
                # Be careful - only clean old files
                pass
            except:
                pass
        
        return f"✓ Cleaned {cleaned} temporary files"
    
    def _format_bytes(self, bytes):
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024:
                return f"{bytes:.1f} {unit}"
            bytes /= 1024
        return f"{bytes:.1f} PB"
    
    def _get_battery_status(self):
        """Get battery status"""
        try:
            battery = psutil.sensors_battery()
            if battery:
                plugged = "⚡ Plugged in" if battery.power_plugged else "🔋 Battery"
                return f"{plugged} ({battery.percent}%)"
            return "No battery detected"
        except:
            return "Unknown"
    
    def _get_temperature(self):
        """Get CPU temperature"""
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                for name, entries in temps.items():
                    for entry in entries:
                        if entry.current:
                            return f"{entry.current:.1f}°C"
            return "N/A"
        except:
            return "N/A"
    
    def run_command(self, command):
        """Run a system command safely"""
        # Whitelist of safe commands
        allowed = ['ls', 'pwd', 'whoami', 'date', 'uptime', 'df', 'free']
        
        cmd_parts = command.split()
        if cmd_parts[0] not in allowed:
            return f"Command '{cmd_parts[0]}' not allowed for security"
        
        try:
            result = subprocess.run(cmd_parts, capture_output=True, text=True, timeout=10)
            return result.stdout or result.stderr
        except Exception as e:
            return f"Error: {e}"
