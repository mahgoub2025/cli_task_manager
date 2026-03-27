"""
========================================
  test_tasks.py — Unit Tests
========================================
Run with:  python -m pytest test_tasks.py -v
or simply: python test_tasks.py
"""

import sys
import os
import json
import tempfile

# Make sure the app modules are importable when running from repo root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "task_manager_cli"))

from models import Task
from storage import save_tasks, load_tasks


# ── Reset ID counter before each test module runs ── #
def setup_module(_):
    Task._id_counter = 1


# ================================================================ #
#  Task MODEL TESTS                                                  #
# ================================================================ #

def test_task_creation():
    """A new task should have the correct defaults."""
    Task._id_counter = 1
    t = Task("Buy groceries")
    assert t.title   == "Buy groceries"
    assert t.done    is False
    assert t.task_id == 1
    print("  ✓ test_task_creation passed")


def test_task_strips_whitespace():
    """Leading/trailing spaces in the title should be stripped."""
    Task._id_counter = 1
    t = Task("  Clean desk  ")
    assert t.title == "Clean desk"
    print("  ✓ test_task_strips_whitespace passed")


def test_task_id_increments():
    """Each new task should get a unique, incrementing ID."""
    Task._id_counter = 1
    t1 = Task("Task one")
    t2 = Task("Task two")
    t3 = Task("Task three")
    assert t1.task_id == 1
    assert t2.task_id == 2
    assert t3.task_id == 3
    print("  ✓ test_task_id_increments passed")


def test_task_mark_done():
    """Setting done=True should persist on the object."""
    Task._id_counter = 1
    t = Task("Write report")
    assert t.done is False
    t.done = True
    assert t.done is True
    print("  ✓ test_task_mark_done passed")


def test_task_to_dict():
    """to_dict() should return a dict with all expected keys."""
    Task._id_counter = 1
    t = Task("Read book")
    d = t.to_dict()
    assert d["title"]   == "Read book"
    assert d["done"]    is False
    assert d["task_id"] == 1
    assert "created" in d
    print("  ✓ test_task_to_dict passed")


def test_task_from_dict():
    """from_dict() should reconstruct a Task accurately."""
    data = {"task_id": 99, "title": "From disk", "done": True, "created": "2025-01-01 09:00"}
    t = Task.from_dict(data)
    assert t.task_id == 99
    assert t.title   == "From disk"
    assert t.done    is True
    print("  ✓ test_task_from_dict passed")


# ================================================================ #
#  STORAGE TESTS                                                     #
# ================================================================ #

def test_save_and_load_roundtrip():
    """Tasks saved to a temp file should reload identically."""
    Task._id_counter = 1
    tasks = [Task("Alpha"), Task("Beta"), Task("Gamma")]
    tasks[1].done = True  # mark the second one done

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
        tmp_path = f.name

    try:
        save_tasks(tasks, tmp_path)
        loaded = load_tasks(tmp_path)

        assert len(loaded) == 3
        assert loaded[0].title   == "Alpha"
        assert loaded[1].done    is True
        assert loaded[2].task_id == 3
        print("  ✓ test_save_and_load_roundtrip passed")
    finally:
        os.unlink(tmp_path)  # clean up temp file


def test_load_missing_file():
    """Loading from a non-existent file should return an empty list."""
    result = load_tasks("/tmp/does_not_exist_xyz.json")
    assert result == []
    print("  ✓ test_load_missing_file passed")


def test_load_corrupted_file():
    """A corrupted JSON file should return an empty list with a warning."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
        f.write("{this is not valid json!!!}")
        tmp_path = f.name

    try:
        result = load_tasks(tmp_path)
        assert result == []
        print("  ✓ test_load_corrupted_file passed")
    finally:
        os.unlink(tmp_path)


def test_id_counter_synced_after_load():
    """After loading, Task._id_counter should be max_id + 1."""
    Task._id_counter = 1
    tasks = [Task("X"), Task("Y"), Task("Z")]  # IDs 1, 2, 3

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
        tmp_path = f.name

    try:
        save_tasks(tasks, tmp_path)
        Task._id_counter = 1  # reset to simulate fresh start
        load_tasks(tmp_path)
        assert Task._id_counter == 4  # next ID should be 4
        print("  ✓ test_id_counter_synced_after_load passed")
    finally:
        os.unlink(tmp_path)


# ================================================================ #
#  RUNNER (if called directly, not via pytest)                       #
# ================================================================ #

if __name__ == "__main__":
    print("\n  Running Task Manager Tests...\n")
    setup_module(None)

    test_task_creation()
    test_task_strips_whitespace()
    test_task_id_increments()
    test_task_mark_done()
    test_task_to_dict()
    test_task_from_dict()
    test_save_and_load_roundtrip()
    test_load_missing_file()
    test_load_corrupted_file()
    test_id_counter_synced_after_load()

    print("\n  ✅  All 10 tests passed!\n")
