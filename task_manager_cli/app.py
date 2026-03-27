"""
========================================
  app.py — Core Application Logic
========================================
TaskManagerApp wires together the menu,
task operations, and storage layer.
"""

import os
from models import Task
from storage import save_tasks, load_tasks


# ── ANSI colour helpers (works on Linux/Mac; Windows 10+ Terminal) ── #
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def green(text):  return f"{GREEN}{text}{RESET}"
def red(text):    return f"{RED}{text}{RESET}"
def yellow(text): return f"{YELLOW}{text}{RESET}"
def cyan(text):   return f"{CYAN}{text}{RESET}"
def bold(text):   return f"{BOLD}{text}{RESET}"


class TaskManagerApp:
    """
    The main application class.
    Holds the task list and routes user input to the right operation.
    """

    def __init__(self):
        # Load any previously saved tasks from disk on startup
        self.tasks: list[Task] = load_tasks()

    # ================================================================ #
    #  DISPLAY HELPERS                                                   #
    # ================================================================ #

    def _clear(self):
        """Clear the terminal screen (cross-platform)."""
        os.system("cls" if os.name == "nt" else "clear")

    def _banner(self):
        """Print the app header."""
        print(bold(cyan("\n╔══════════════════════════════════════╗")))
        print(bold(cyan("║       📝  CLI TASK MANAGER           ║")))
        print(bold(cyan("╚══════════════════════════════════════╝")))
        print(f"  Tasks loaded: {len(self.tasks)}  |  "
              f"Done: {sum(1 for t in self.tasks if t.done)}  |  "
              f"Pending: {sum(1 for t in self.tasks if not t.done)}\n")

    def _menu(self):
        """Print the main menu options."""
        print(bold("  What would you like to do?"))
        print(f"  {cyan('[1]')} Add a task")
        print(f"  {cyan('[2]')} View all tasks")
        print(f"  {cyan('[3]')} Mark task as done")
        print(f"  {cyan('[4]')} Delete a task")
        print(f"  {cyan('[5]')} Filter tasks")
        print(f"  {red('[6]')} Quit\n")

    def _print_tasks(self, tasks: list[Task], heading: str = "All Tasks"):
        """Pretty-print a list of tasks."""
        print(bold(f"\n  ── {heading} ──"))
        if not tasks:
            print(yellow("  (no tasks to show)"))
            return
        for task in tasks:
            status = green("✓") if task.done else yellow("○")
            title  = task.title if not task.done else f"\033[9m{task.title}\033[0m"  # strikethrough if done
            print(f"  {status} #{task.task_id:02d}  {title}  "
                  f"{CYAN}({task.created}){RESET}")

    # ================================================================ #
    #  CORE OPERATIONS                                                   #
    # ================================================================ #

    def add_task(self):
        """Prompt the user for a title and create a new Task."""
        print(bold("\n  ── Add New Task ──"))
        title = input("  Enter task title (or leave blank to cancel): ").strip()
        if not title:
            print(yellow("  Cancelled — no title entered."))
            return
        task = Task(title)           # create the task object
        self.tasks.append(task)      # add to the in-memory list
        save_tasks(self.tasks)       # persist to disk immediately
        print(green(f"  ✓ Task #{task.task_id:02d} added: '{task.title}'"))

    def view_tasks(self):
        """Display all tasks."""
        self._print_tasks(self.tasks)

    def mark_done(self):
        """Mark a specific task as completed by its ID."""
        self._print_tasks(
            [t for t in self.tasks if not t.done],
            heading="Pending Tasks"
        )
        if not any(not t.done for t in self.tasks):
            print(green("  All tasks are already done! 🎉"))
            return

        raw = input("\n  Enter task ID to mark done (or 0 to cancel): ").strip()
        if raw == "0" or raw == "":
            print(yellow("  Cancelled."))
            return

        try:
            task_id = int(raw)
        except ValueError:
            print(red("  ✗ Please enter a valid number."))
            return

        # Find the task by ID
        target = next((t for t in self.tasks if t.task_id == task_id), None)
        if not target:
            print(red(f"  ✗ No task with ID #{task_id} found."))
            return
        if target.done:
            print(yellow(f"  Task #{task_id} is already marked as done."))
            return

        target.done = True           # flip the flag
        save_tasks(self.tasks)       # save change to disk
        print(green(f"  ✓ Task #{task_id} '{target.title}' marked as done!"))

    def delete_task(self):
        """Remove a task permanently by its ID."""
        self._print_tasks(self.tasks)
        if not self.tasks:
            return

        raw = input("\n  Enter task ID to delete (or 0 to cancel): ").strip()
        if raw == "0" or raw == "":
            print(yellow("  Cancelled."))
            return

        try:
            task_id = int(raw)
        except ValueError:
            print(red("  ✗ Please enter a valid number."))
            return

        target = next((t for t in self.tasks if t.task_id == task_id), None)
        if not target:
            print(red(f"  ✗ No task with ID #{task_id} found."))
            return

        # Confirm before deleting
        confirm = input(
            yellow(f"  Delete '{target.title}'? This cannot be undone. (y/n): ")
        ).strip().lower()
        if confirm != "y":
            print(yellow("  Cancelled."))
            return

        self.tasks.remove(target)    # remove from list
        save_tasks(self.tasks)       # reflect deletion on disk
        print(green(f"  ✓ Task #{task_id} deleted."))

    def filter_tasks(self):
        """Show tasks filtered by status."""
        print(bold("\n  ── Filter by Status ──"))
        print(f"  {cyan('[1]')} Show only pending tasks")
        print(f"  {cyan('[2]')} Show only completed tasks")
        choice = input("  Choice: ").strip()

        if choice == "1":
            self._print_tasks(
                [t for t in self.tasks if not t.done],
                heading="Pending Tasks"
            )
        elif choice == "2":
            self._print_tasks(
                [t for t in self.tasks if t.done],
                heading="Completed Tasks"
            )
        else:
            print(yellow("  Invalid choice — showing all tasks."))
            self._print_tasks(self.tasks)

    # ================================================================ #
    #  MAIN LOOP                                                         #
    # ================================================================ #

    def run(self):
        """
        The main application loop.
        Keeps running until the user chooses to quit.
        """
        while True:
            self._clear()
            self._banner()
            self._menu()

            choice = input("  Your choice: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_done()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                print(bold(cyan("\n  👋  Goodbye! Stay productive.\n")))
                break
            else:
                print(red("  ✗ Invalid option. Please choose 1–6."))

            # Pause so the user can read the output before the screen clears
            input(f"\n  {YELLOW}Press Enter to continue...{RESET}")
