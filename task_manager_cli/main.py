#!/usr/bin/env python3
"""
========================================
  CLI Task Manager — Entry Point
  Prompt-Powered Kickstart Capstone
========================================
Run this file to start the Task Manager.
Usage: python main.py
"""

from app import TaskManagerApp

if __name__ == "__main__":
    app = TaskManagerApp()
    app.run()
