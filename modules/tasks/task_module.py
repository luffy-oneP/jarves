#!/usr/bin/env python3
"""
Task Module - Task management and reminders
"""

import json
import os
from datetime import datetime
from pathlib import Path


class TaskModule:
    """Manage tasks and reminders"""
    
    def __init__(self, brain):
        self.brain = brain
        self.tasks_file = Path(__file__).parent.parent.parent / "data" / "tasks.json"
        self.tasks = []
        self._load_tasks()
    
    def _load_tasks(self):
        """Load tasks from file"""
        if self.tasks_file.exists():
            try:
                with open(self.tasks_file) as f:
                    self.tasks = json.load(f)
            except:
                self.tasks = []
        else:
            self.tasks = []
    
    def _save_tasks(self):
        """Save tasks to file"""
        self.tasks_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.tasks_file, "w") as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, text, priority="normal"):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "text": text,
            "created": datetime.now().isoformat(),
            "completed": False,
            "priority": priority
        }
        self.tasks.append(task)
        self._save_tasks()
        return f"✓ Added task: {text}"
    
    def list_tasks(self, show_completed=False):
        """List all tasks"""
        if not self.tasks:
            return "No tasks found. Add one with: add task [description]"
        
        pending = [t for t in self.tasks if not t["completed"]]
        completed = [t for t in self.tasks if t["completed"]]
        
        result = []
        result.append(f"📋 Tasks ({len(pending)} pending, {len(completed)} completed):")
        result.append("")
        
        if pending:
            result.append("Pending:")
            for task in pending:
                priority_emoji = {"high": "🔴", "normal": "🟡", "low": "🟢"}.get(task["priority"], "⚪")
                result.append(f"  {priority_emoji} [{task['id']}] {task['text']}")
        
        if show_completed and completed:
            result.append("")
            result.append("Completed:")
            for task in completed:
                result.append(f"  ✓ [{task['id']}] {task['text']}")
        
        return "\n".join(result)
    
    def complete_task(self, task_id=None):
        """Mark task as completed"""
        if task_id is None:
            # Complete most recent pending task
            for task in reversed(self.tasks):
                if not task["completed"]:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().isoformat()
                    self._save_tasks()
                    return f"✓ Completed: {task['text']}"
            return "No pending tasks to complete."
        
        # Complete specific task
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat()
                self._save_tasks()
                return f"✓ Completed: {task['text']}"
        return f"Task {task_id} not found."
    
    def remove_task(self, task_id=None):
        """Remove a task"""
        if task_id is None:
            return "Please specify task ID to remove."
        
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed = self.tasks.pop(i)
                self._save_tasks()
                return f"✓ Removed: {removed['text']}"
        return f"Task {task_id} not found."
    
    def get_pending_count(self):
        """Get number of pending tasks"""
        return len([t for t in self.tasks if not t["completed"]])
