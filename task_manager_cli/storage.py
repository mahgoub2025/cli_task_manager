"""
========================================
  storage.py — JSON Persistence Layer
========================================
Handles reading and writing tasks to a
local JSON file so data survives restarts.
"""

import json
import os
from models import Task

# Default file where tasks are saved (same folder as the script)
DEFAULT_FILE = "tasks.json"


def save_tasks(tasks: list[Task], filepath: str = DEFAULT_FILE) -> None:
    """
    Serialize the task list to JSON and write it to disk.

    Args:
        tasks    : List of Task objects to save.
        filepath : Path to the JSON file (default: tasks.json).
    """
    data = [task.to_dict() for task in tasks]   # convert objects → dicts
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)             # pretty-print with 2-space indent


def load_tasks(filepath: str = DEFAULT_FILE) -> list[Task]:
    """
    Load tasks from a JSON file and return a list of Task objects.
    If the file doesn't exist yet, return an empty list (first run).

    Args:
        filepath : Path to the JSON file (default: tasks.json).

    Returns:
        List of Task objects, or [] if the file is missing / empty.
    """
    if not os.path.exists(filepath):
        return []   # first time the app runs — no file yet, that's fine

    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            # File exists but is empty or corrupted — start fresh
            print("⚠️  Warning: tasks.json is corrupted. Starting with empty list.")
            return []

    tasks = [Task.from_dict(item) for item in data]

    # Sync the class ID counter so new tasks don't clash with loaded IDs
    if tasks:
        Task._id_counter = max(t.task_id for t in tasks) + 1

    return tasks
