# Prompt-Powered Kickstart: Building a Beginner's Toolkit for Python
### A Command-Line Task Manager — From Zero to Running Code

> **Moringa School Capstone | Beginner's Toolkit with GenAI**
> Author: [Your Name] | Date: March 2026

---

## Table of Contents

1. [Title & Objective](#1-title--objective)
2. [Quick Summary of the Technology](#2-quick-summary-of-the-technology)
3. [System Requirements](#3-system-requirements)
4. [Installation & Setup Instructions](#4-installation--setup-instructions)
5. [Minimal Working Example](#5-minimal-working-example)
6. [AI Prompt Journal](#6-ai-prompt-journal)
7. [Common Issues & Fixes](#7-common-issues--fixes)
8. [References](#8-references)

---

## 1. Title & Objective

**Title:** Getting Started with Python — Building a CLI Task Manager

**Technology chosen:** Python 3 (standard library + pytest for testing)

**Why Python?**

Honestly? I kept hearing "just learn Python" from every developer I talked to,
every YouTube video I clicked, every job posting I looked at. I started this
capstone wanting to finally find out what the fuss was about — not by reading a
textbook, but by actually building something I'd use myself.

A task manager felt right. It touches the things that matter in real programming:
handling user input, organising data into objects, reading and writing files, and
testing that your logic actually works. No fluff, no bloated framework to learn
first — just Python doing real work.

**End goal:**

A fully working command-line program that lets you:
- Add tasks with a title
- View all tasks in a formatted list
- Mark tasks as done
- Delete tasks (with a confirmation step so you don't accidentally nuke everything)
- Filter by pending or completed
- Save everything to a `tasks.json` file so nothing disappears when you close the terminal

---

## 2. Quick Summary of the Technology

### What is Python?

Python is a general-purpose, high-level programming language first released in 1991
by Guido van Rossum. It is designed to be readable — the syntax looks almost like
plain English — which makes it one of the most beginner-friendly languages in
existence, while also being powerful enough to run production systems at Google,
Instagram, and NASA.

### Where is Python used?

Practically everywhere:
- **Web backends** — Django, FastAPI, Flask power millions of websites
- **Data science & AI** — NumPy, Pandas, TensorFlow, PyTorch all live in Python
- **Automation & scripting** — if you want to rename 500 files or scrape a website, Python
- **Command-line tools** — exactly what we are building here
- **Education** — it is the most taught first programming language in universities worldwide

### One real-world example

Instagram's backend runs on Python (Django). At peak load it handles hundreds of
millions of users. The same language in this beginner guide powers one of the most
visited websites on earth.

### What is the standard library?

Python ships with a huge collection of built-in modules — code that is already
installed when you install Python and covers most common tasks without needing
to install anything extra. This project uses:

| Module | What it does in this project |
|--------|------------------------------|
| `json` | Saves and loads tasks to a `.json` file |
| `os`   | Clears the terminal screen, checks if files exist |
| `datetime` | Stamps tasks with the time they were created |

---

## 3. System Requirements

| Requirement | Details |
|-------------|---------|
| **Operating system** | Windows 10/11, macOS 12+, or any modern Linux distro |
| **Python version** | 3.10 or higher (we use `list[Task]` type hints that need 3.9+) |
| **Editor** | VS Code (recommended) — free, has excellent Python support |
| **Terminal** | Windows Terminal, macOS Terminal, or any Linux shell |
| **Git** | For cloning the repo (optional but recommended) |
| **pip** | Comes bundled with Python — used to install pytest |

**No external Python packages are needed to run the app itself.**
`pytest` is the only install, and it is only needed to run the test suite.

---

## 4. Installation & Setup Instructions

This section walks you through every single step from a brand-new computer to a
running program. No steps are skipped. Every command is shown exactly as you would
type it.

---

### Step 4.1 — Download and Install Python

#### On Windows

1. Open your browser and go to **https://python.org/downloads**
2. Click the big yellow **"Download Python 3.x.x"** button
3. Run the installer (`.exe` file you just downloaded)

   > ⚠️ **CRITICAL:** On the very first screen of the installer, tick the checkbox
   > **"Add Python to PATH"** before clicking Install Now.
   > If you miss this, your terminal won't find Python and you'll need to reinstall.

   ```
   ┌─────────────────────────────────────────────┐
   │  Install Python 3.x.x                       │
   │                                             │
   │  [●] Add Python to PATH      ← TICK THIS   │
   │                                             │
   │  [ Install Now ]                            │
   └─────────────────────────────────────────────┘
   ```

4. Let the installer finish, then click **Close**

📸 *Screenshot checkpoint: You should see "Setup was successful" on the last screen.*

#### On macOS

macOS may come with an old Python 2 — we need Python 3.

Option A — Download from python.org (same as Windows, download the `.pkg` file):
```
https://python.org/downloads
```

Option B — Use Homebrew (if you have it):
```bash
brew install python
```

#### On Linux (Ubuntu / Debian)

Python 3 is usually pre-installed. Check first:
```bash
python3 --version
```

If it is missing or below 3.10:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

### Step 4.2 — Verify Python Installed Correctly

Open a **brand new** terminal window (important — old windows won't see the updated PATH).

```bash
python --version
# expected output:  Python 3.x.x

python -m pip --version
# expected output:  pip 24.x.x from ...
```

> On macOS/Linux you may need `python3` instead of `python`:
> ```bash
> python3 --version
> ```

📸 *Screenshot checkpoint: Both commands return version numbers with no errors.*

If you see `'python' is not recognized as an internal or external command`:
- You forgot to tick "Add Python to PATH" during install
- Reinstall Python and tick that checkbox, OR
- Add it manually: see [Common Issues & Fixes → Issue 1](#7-common-issues--fixes)

---

### Step 4.3 — Install VS Code (Recommended Editor)

1. Go to **https://code.visualstudio.com**
2. Download the installer for your OS and run it
3. Open VS Code
4. Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on Mac) to open Extensions
5. Search for **"Python"** and install the extension by Microsoft

📸 *Screenshot checkpoint: VS Code opens and the Python extension shows as installed.*

---

### Step 4.4 — Install Git

Git lets you clone repos and track your own code changes.

**Windows:** Download from **https://git-scm.com/download/win** and run the installer.
Accept all defaults.

**macOS:**
```bash
xcode-select --install
# git comes with the Xcode command-line tools
```

**Linux:**
```bash
sudo apt install git
```

Verify:
```bash
git --version
# expected: git version 2.x.x
```

📸 *Screenshot checkpoint: `git --version` returns a version number.*

---

### Step 4.5 — Clone the Repository

```bash
# Navigate to wherever you keep your code projects
cd Documents   # or wherever you prefer

# Clone the repo
git clone https://github.com/YOUR_USERNAME/python_task_manager.git

# Move into the project folder
cd python_task_manager
```

You should now see this structure:
```
python_task_manager/
├── task_manager_cli/
│   ├── main.py
│   ├── app.py
│   ├── models.py
│   └── storage.py
├── test_tasks.py
├── requirements.txt
└── README.md
```

📸 *Screenshot checkpoint: Run `ls` (Mac/Linux) or `dir` (Windows) and see the files above.*

---

### Step 4.6 — Create a Virtual Environment (Best Practice)

A virtual environment is a self-contained folder where Python packages for this
project live, completely separate from your system Python. This is standard
professional practice — always use one.

```bash
# Make sure you are inside the project folder
# python_task_manager/

# Create the virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate
```

You'll know it worked because your terminal prompt changes to show `(venv)`:
```
(venv) C:\Users\YourName\Documents\python_task_manager>
```

📸 *Screenshot checkpoint: Your terminal prompt now starts with `(venv)`.*

---

### Step 4.7 — Install pytest

The app itself needs no external packages. We only install pytest to run the tests.

```bash
pip install -r requirements.txt
```

Expected output (condensed):
```
Collecting pytest>=7.0.0
  Downloading pytest-8.x.x-py3-none-any.whl
Installing collected packages: pytest
Successfully installed pytest-8.x.x
```

📸 *Screenshot checkpoint: Output ends with "Successfully installed pytest-x.x.x".*

---

### Step 4.8 — Run the Application

```bash
# Move into the CLI subfolder
cd task_manager_cli

# Start the app
python main.py
```

You should see:
```
╔══════════════════════════════════════╗
║       📝  CLI TASK MANAGER           ║
╚══════════════════════════════════════╝
  Tasks loaded: 0  |  Done: 0  |  Pending: 0

  What would you like to do?
  [1] Add a task
  [2] View all tasks
  [3] Mark task as done
  [4] Delete a task
  [5] Filter tasks
  [6] Quit

  Your choice:
```

📸 *Screenshot checkpoint: The menu above appears in your terminal.*

---

### Step 4.9 — Run the Tests

From the project root (one folder up from `task_manager_cli`):

```bash
# Go back up to the project root
cd ..

# Run tests directly
python test_tasks.py
```

Expected output:
```
  Running Task Manager Tests...

  ✓ test_task_creation passed
  ✓ test_task_strips_whitespace passed
  ✓ test_task_id_increments passed
  ✓ test_task_mark_done passed
  ✓ test_task_to_dict passed
  ✓ test_task_from_dict passed
  ✓ test_save_and_load_roundtrip passed
  ✓ test_load_missing_file passed
  ✓ test_load_corrupted_file passed
  ✓ test_id_counter_synced_after_load passed

  ✅  All 10 tests passed!
```

Or with pytest for a richer output:
```bash
pytest test_tasks.py -v
```

📸 *Screenshot checkpoint: All 10 tests show as passed.*
---

## 5. Minimal Working Example

### What the Example Does

The Task Manager is a menu-driven command-line app. When you run it, you get a
numbered menu. You type a number, press Enter, and the app does that thing.
Your tasks are saved to `tasks.json` in the `task_manager_cli/` folder
automatically every time you add, complete, or delete a task.

Here is a full walkthrough of each feature.

---

### Feature 1 — Adding a Task

Type `1` at the menu and press Enter.

```
  ── Add New Task ──
  Enter task title (or leave blank to cancel): Buy coffee beans
  ✓ Task #01 added: 'Buy coffee beans'
```

The task is immediately written to `tasks.json`:

```json
[
  {
    "task_id": 1,
    "title": "Buy coffee beans",
    "done": false,
    "created": "2026-03-27 09:15"
  }
]
```

---

### Feature 2 — Viewing All Tasks

Type `2` at the menu.

```
  ── All Tasks ──
  ○ #01  Buy coffee beans  (2026-03-27 09:15)
  ○ #02  Reply to emails   (2026-03-27 09:16)
  ✓ #03  Morning run       (2026-03-27 09:17)
```

`○` = pending, `✓` = done. Done tasks appear with strikethrough in most terminals.

---

### Feature 3 — Marking a Task Done

Type `3`. The app shows only your pending tasks, then asks for an ID.

```
  ── Pending Tasks ──
  ○ #01  Buy coffee beans  (2026-03-27 09:15)
  ○ #02  Reply to emails   (2026-03-27 09:16)

  Enter task ID to mark done (or 0 to cancel): 1
  ✓ Task #01 'Buy coffee beans' marked as done!
```

---

### Feature 4 — Deleting a Task

Type `4`. The app shows all tasks, asks for an ID, then asks for confirmation.

```
  Enter task ID to delete (or 0 to cancel): 2
  Delete 'Reply to emails'? This cannot be undone. (y/n): y
  ✓ Task #02 deleted.
```

---

### Feature 5 — Filtering Tasks

Type `5`.

```
  ── Filter by Status ──
  [1] Show only pending tasks
  [2] Show only completed tasks
  Choice: 2

  ── Completed Tasks ──
  ✓ #01  Buy coffee beans  (2026-03-27 09:15)
  ✓ #03  Morning run       (2026-03-27 09:17)
```

---

### The Code — Annotated Key Parts

#### models.py — The Task Class

```python
class Task:
    """One task = one object. ID is auto-assigned and increments."""

    _id_counter = 1   # shared across all Task instances

    def __init__(self, title: str):
        self.task_id = Task._id_counter   # give this task the next ID
        Task._id_counter += 1             # prepare ID for the next task
        self.title   = title.strip()      # clean up any accidental spaces
        self.done    = False              # every task starts as not done
        self.created = datetime.now().strftime("%Y-%m-%d %H:%M")
```

The `to_dict()` and `from_dict()` methods are the bridge between Python objects
and JSON. `to_dict()` converts a Task into a plain dictionary before saving;
`from_dict()` does the reverse when loading from disk — without triggering
`__init__` (which would mess up the ID counter).

#### storage.py — Saving and Loading

```python
def save_tasks(tasks, filepath="tasks.json"):
    data = [task.to_dict() for task in tasks]   # list of dicts
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)             # pretty JSON on disk
```

```python
def load_tasks(filepath="tasks.json"):
    if not os.path.exists(filepath):
        return []                                # first run — no file yet

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    tasks = [Task.from_dict(item) for item in data]

    # Sync the counter so new tasks get IDs that don't clash with loaded ones
    if tasks:
        Task._id_counter = max(t.task_id for t in tasks) + 1

    return tasks
```

#### app.py — The Main Loop

```python
def run(self):
    while True:                     # keep looping until the user quits
        self._clear()               # fresh screen each iteration
        self._banner()              # show stats header
        self._menu()                # show numbered options

        choice = input("  Your choice: ").strip()

        if choice == "1":
            self.add_task()
        elif choice == "2":
            self.view_tasks()
        # ... etc ...
        elif choice == "6":
            break                   # exit the loop → program ends

        input(f"\n  Press Enter to continue...")   # pause to read output
```

---

### Expected Output (Full Session)

```
╔══════════════════════════════════════╗
║       📝  CLI TASK MANAGER           ║
╚══════════════════════════════════════╝
  Tasks loaded: 3  |  Done: 1  |  Pending: 2

  What would you like to do?
  [1] Add a task
  [2] View all tasks
  [3] Mark task as done
  [4] Delete a task
  [5] Filter tasks
  [6] Quit

  Your choice: 2

  ── All Tasks ──
  ○ #01  Buy coffee beans  (2026-03-27 09:15)
  ○ #02  Reply to emails   (2026-03-27 09:16)
  ✓ #03  Morning run       (2026-03-27 09:17)

  Press Enter to continue...
```

---

## 6. AI Prompt Journal

This section documents the actual prompts I used during this project, what the AI
gave back, and — honestly — where it helped and where I had to push back or figure
things out myself.

I used three tools: **Claude (claude.ai)**, **ChatGPT**, and **GitHub Copilot**.

---

### Phase 1 — Understanding the Language

**Prompt 1 — Getting oriented**

> *Used on: Claude (claude.ai)*
>
> "I'm a complete beginner. I've heard Python is great for beginners.
> Can you explain what makes Python different from other languages, why
> it's popular, and give me one real-world example of it being used
> professionally? Keep it simple — I don't know any programming yet."

**AI response summary:**
Claude gave a clean explanation comparing Python's syntax to plain English,
mentioned Instagram as a real-world example, and explained that the standard
library means you don't have to install much to get started. It also suggested
I start with small scripts before jumping to projects.

**My evaluation:**
Exactly what I needed. It didn't try to teach me syntax in the first message —
it gave me enough context to feel confident continuing. 9/10.

---

**Prompt 2 — Understanding classes**

> *Used on: Claude (claude.ai)*
>
> "I want to build a task manager. Each task needs an ID, a title, whether
> it's done or not, and when it was created. I've heard Python has something
> called 'classes'. Can you explain what a class is using the task as an
> example? Show me the code and explain each line."

**AI response summary:**
Introduced the `__init__` method, `self`, and instance attributes using Task
as the example. Showed `datetime.now()` for the timestamp. The explanation of
`self` was the clearest I'd seen anywhere.

**My evaluation:**
This one prompt saved me probably two hours of reading. I came away understanding
*why* classes exist, not just what the syntax looks like. 10/10.

---

### Phase 2 — Building the App

**Prompt 3 — Designing the structure**

> *Used on: ChatGPT*
>
> "I want to build a Python CLI task manager. Help me plan the file structure
> before I write any code. The program should: add tasks, view them, mark them
> done, delete them, and save everything to a file. What files should I create
> and what should each one be responsible for?"

**AI response summary:**
Suggested separating concerns: `models.py` for the Task class, `storage.py`
for file operations, `app.py` for the menu logic, and `main.py` as the entry
point. It also warned me not to put everything in one file because it becomes
impossible to test later.

**My evaluation:**
This prompt taught me about separation of concerns without me even asking for it
directly. That lesson shaped the entire project. 10/10.

---

**Prompt 4 — JSON storage**

> *Used on: Claude (claude.ai)*
>
> "I want to save Python objects to a JSON file and load them back.
> The objects are Task instances with task_id, title, done, and created
> attributes. Show me how to convert them to dictionaries, write to a file
> with json.dump, and read them back with json.load. Also show me how to
> handle the case where the file doesn't exist yet."

**AI response summary:**
Provided the exact `to_dict()` / `from_dict()` pattern, explained `with open`
for safe file handling, and showed the `os.path.exists()` check. It also
mentioned the `try/except json.JSONDecodeError` guard for corrupted files —
which I hadn't thought about.

**My evaluation:**
The corrupted-file handling was a bonus I didn't ask for but immediately included.
The explanation of `with open` (context managers) was a foundational Python lesson
hidden inside an answer about file storage. 10/10.

---

**Prompt 5 — The ID counter problem**

> *Used on: Claude (claude.ai)*
>
> "I have a Task class with a class-level counter that auto-increments for each
> new task. The problem: when I load saved tasks from JSON and create new ones,
> the IDs restart at 1 and clash with existing tasks. How do I fix this?"

**AI response summary:**
Explained the difference between class attributes and instance attributes, and
showed me to sync `Task._id_counter` to `max(task_id) + 1` after loading.
Also explained why `from_dict` should use `cls.__new__(cls)` to bypass `__init__`
and avoid double-incrementing.

**My evaluation:**
This was the trickiest bug in the whole project. I would not have solved it
without help. The `__new__` explanation opened a rabbit hole of Python internals
I'm still reading about. 10/10 — though I had to re-read the answer three times.

---

**Prompt 6 — ANSI colours**

> *Used on: ChatGPT*
>
> "How do I add colour to Python terminal output using ANSI escape codes?
> I want green for completed tasks, yellow for pending, and red for errors.
> Show me a simple helper function approach."

**AI response summary:**
Provided the `\033[92m` / `\033[0m` pattern and suggested wrapping them in
tiny helper functions (`green()`, `red()`, `yellow()`) for cleaner call sites.
Warned that colours may not display on older Windows CMD but work fine in
Windows Terminal and all modern terminals.

**My evaluation:**
Worked first try. The warning about older Windows CMD saved me from a confusing
bug report later. 8/10 — I had to ask a follow-up to get the bold/reset right.

---

**Prompt 7 — Writing tests**

> *Used on: GitHub Copilot (inside VS Code)*
>
> "Write pytest tests for this Task class. Test: creation defaults, ID
> increment, title stripping, marking done, to_dict output, from_dict
> reconstruction, and JSON save/load roundtrip."

**AI response summary:**
Generated a solid test file covering all the above. Also suggested testing the
edge case of a missing file (returns empty list) and a corrupted file.

**My evaluation:**
Copilot's in-editor suggestions were useful for repetitive test boilerplate.
The corrupted-file test was again a bonus I didn't ask for. The ID counter
sync test was slightly wrong on first generation — it reset `_id_counter`
to 1 before loading but didn't verify it became 4. I fixed that manually.
7/10 — good base, needed human review.

---

**Prompt 8 — Refining the menu UX**

> *Used on: Claude (claude.ai)*
>
> "My CLI menu works but it's ugly. How do I make it feel more polished?
> I want a header with stats (total tasks, done count, pending count),
> a clear screen between interactions, and a 'press enter to continue'
> pause. Show me the pattern."

**AI response summary:**
Provided the `os.system("cls" if os.name == "nt" else "clear")` cross-platform
clear trick, the stats header pattern using `sum()` with conditions, and the
`input("Press Enter to continue...")` pause pattern.

**My evaluation:**
The `os.name == "nt"` check was something I'd have googled separately for an
hour. Having it all in one answer saved time and taught me about platform
detection. 9/10.

---

### Reflection — What AI Changed About Learning

Before this project my approach was: read a chapter → try to code → get stuck →
Google for 20 minutes → maybe find the answer. Now it is: get stuck → ask AI →
understand the concept → implement → test.

The difference in speed is significant. But more importantly, the AI explains
*why* in ways that search results rarely do. Stack Overflow gives you the fix;
the AI tells you why your original code was wrong.

Where AI fell short: when I asked vague questions, I got vague answers. Prompt 7
(the Copilot test generation) needed manual review because I hadn't been specific
enough about edge cases. The lesson was: the quality of the answer is almost
entirely determined by the quality of the question.

---

## 7. Common Issues & Fixes

### Issue 1 — `python` is not recognised

**Symptom:**
```
'python' is not recognized as an internal or external command
```

**Cause:**
Python was installed but the installer was not given permission to add it to
the system PATH, so the terminal cannot find it.

**Fix (Windows):**

Option A — Reinstall Python and tick "Add Python to PATH" this time.

Option B — Add it manually:
1. Press `Win + R`, type `sysdm.cpl`, press Enter
2. Click **Advanced** → **Environment Variables**
3. Under **User variables**, find and click **Path** → **Edit**
4. Click **New** and add:
   ```
   C:\Users\YourUsername\AppData\Local\Programs\Python\Python3xx\
   C:\Users\YourUsername\AppData\Local\Programs\Python\Python3xx\Scripts\
   ```
5. Click OK → OK → OK, then open a new terminal

**Fix (macOS/Linux):**
Add to `~/.zshrc` or `~/.bashrc`:
```bash
export PATH="$HOME/.local/bin:$PATH"
```
Then run: `source ~/.zshrc`

📎 Reference: https://stackoverflow.com/questions/13596505/python-command-not-working-in-command-prompt

---

### Issue 2 — `ModuleNotFoundError: No module named 'models'`

**Symptom:**
```
ModuleNotFoundError: No module named 'models'
```

**Cause:**
Running `python main.py` from the wrong directory. Python looks for `models.py`
in the current folder, not in a subfolder.

**Fix:**
Always run the app from inside the `task_manager_cli/` folder:
```bash
cd task_manager_cli
python main.py
```

---

### Issue 3 — Tasks disappear on restart

**Symptom:**
You add tasks, close the app, reopen it, and your tasks are gone.

**Cause:**
Running `main.py` from different directories creates `tasks.json` in different
locations. The second run can't find the file from the first run.

**Fix:**
Always `cd task_manager_cli` first, then `python main.py`. The JSON file lives
in `task_manager_cli/tasks.json` — stay consistent.

---

### Issue 4 — Colours not showing on Windows

**Symptom:**
Instead of coloured text you see `←[92msome text←[0m` (raw escape codes).

**Cause:**
Old `cmd.exe` doesn't understand ANSI escape codes.

**Fix:**
Use **Windows Terminal** (free from the Microsoft Store) or **VS Code's integrated
terminal** — both support ANSI colours. If you must use cmd.exe, add this to the
top of `app.py`:

```python
import os
os.system("")   # enables ANSI in cmd.exe on Windows 10+
```

📎 Reference: https://stackoverflow.com/questions/36760127/how-to-use-the-new-support-for-ansi-escape-codes-in-the-windows-10-console

---

### Issue 5 — `json.JSONDecodeError` on startup

**Symptom:**
```
⚠️  Warning: tasks.json is corrupted. Starting with empty list.
```

**Cause:**
The `tasks.json` file exists but is empty or was manually edited and broken.

**Fix:**
The app handles this gracefully and starts with an empty task list. If you want
to recover data, open `tasks.json` in VS Code and look for missing brackets or
commas. Valid JSON always starts with `[` and ends with `]`.

---

### Issue 6 — `pip install` fails with `externally-managed-environment`

**Symptom:**
```
error: externally-managed-environment
```

**Cause:**
On newer Linux/macOS, pip refuses to install packages system-wide to protect the
OS Python installation.

**Fix:**
Always use a virtual environment (Step 4.6):
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 8. References

### Official Documentation

| Resource | URL |
|----------|-----|
| Python Official Docs | https://docs.python.org/3/ |
| Python `json` module | https://docs.python.org/3/library/json.html |
| Python `datetime` module | https://docs.python.org/3/library/datetime.html |
| Python `os` module | https://docs.python.org/3/library/os.html |
| pytest documentation | https://docs.pytest.org/en/stable/ |

### Learning Resources

| Resource | URL | Why it helps |
|----------|-----|-------------|
| The Python Tutorial (official) | https://docs.python.org/3/tutorial/ | Best place to start after this guide |
| Real Python | https://realpython.com | Practical, project-based articles |
| CS50P (Harvard, free) | https://cs50.harvard.edu/python/ | Best free Python course for absolute beginners |
| Automate the Boring Stuff | https://automatetheboringstuff.com | Free book, very practical |
| W3Schools Python | https://w3schools.com/python | Quick reference for syntax |

### Video Tutorials

| Resource | URL |
|----------|-----|
| Python for Beginners (freeCodeCamp) | https://youtu.be/rfscVS0vtbw |
| Python OOP Tutorial (Corey Schafer) | https://youtu.be/ZDa-Z5JzLYM |
| Python Virtual Environments (Corey Schafer) | https://youtu.be/Kg1Yvry_Ydk |

### AI Tools Used

| Tool | URL | Used for |
|------|-----|---------|
| Claude | https://claude.ai | Architecture, explanations, debugging |
| ChatGPT | https://chat.openai.com | File structure planning, colour output |
| GitHub Copilot | https://github.com/features/copilot | In-editor test generation |

### Helpful StackOverflow Threads

- Python PATH on Windows: https://stackoverflow.com/questions/13596505
- ANSI colours in Windows Terminal: https://stackoverflow.com/questions/36760127
- `__new__` vs `__init__`: https://stackoverflow.com/questions/674304
- `json.JSONDecodeError` handling: https://stackoverflow.com/questions/20199126

---

*End of Toolkit Document*

> **Submitted for:** Moringa School — Beginner's Toolkit with GenAI Capstone
> **Technology:** Python 3 (Standard Library)
> **Project:** CLI Task Manager
> **GitHub:** https://github.com/YOUR_USERNAME/python_task_manager
