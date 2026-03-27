"""
========================================
  models.py — Task Data Model
========================================
Defines the Task class which represents
a single task item in the manager.
"""

from datetime import datetime


class Task:
    """
    Represents a single task.

    Attributes:
        task_id  (int)  : Unique identifier, auto-assigned.
        title    (str)  : Short description of the task.
        done     (bool) : Whether the task is completed.
        created  (str)  : Timestamp when the task was created.
    """

    # Class-level counter so every task gets a unique ID
    _id_counter = 1

    def __init__(self, title: str):
        self.task_id = Task._id_counter        # assign next available ID
        Task._id_counter += 1                  # increment for the next task
        self.title   = title.strip()           # remove accidental whitespace
        self.done    = False                   # all tasks start as not done
        self.created = datetime.now().strftime("%Y-%m-%d %H:%M")  # human date

    # ------------------------------------------------------------------ #
    # Serialisation helpers — used when saving/loading from JSON          #
    # ------------------------------------------------------------------ #

    def to_dict(self) -> dict:
        """Convert this task to a plain dictionary (for JSON storage)."""
        return {
            "task_id": self.task_id,
            "title":   self.title,
            "done":    self.done,
            "created": self.created,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """
        Re-create a Task object from a dictionary loaded from JSON.
        We bypass __init__ so we don't auto-increment the counter
        for tasks that already have an ID stored on disk.
        """
        task          = cls.__new__(cls)   # create instance without calling __init__
        task.task_id  = data["task_id"]
        task.title    = data["title"]
        task.done     = data["done"]
        task.created  = data["created"]
        return task

    def __repr__(self) -> str:
        status = "✓" if self.done else "○"
        return f"[{status}] #{self.task_id:02d} {self.title}  ({self.created})"
