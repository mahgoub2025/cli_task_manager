# 📝 CLI Task Manager
### Prompt-Powered Kickstart: A Beginner's journal for Python

> Capstone Project — built with Python's standard library,
> documented with GenAI, tested with pytest.

---

## 📁 Project Structure

```
cli_task_manager/                  ← open THIS folder in VS Code
│
├── task_manager_cli/              ← the application package
│   ├── __init__.py
│   ├── main.py                    ← entry point  →  python main.py
│   ├── app.py                     ← menu loop + all operations
│   ├── models.py                  ← Task class (data model)
│   └── storage.py                 ← JSON save / load
│
├── tests/                         ← test suite
│   ├── __init__.py
│   └── test_tasks.py              ← 10 unit tests
│
├── docs/
│   └── TOOLKIT_GUIDE.md           ← full capstone document (969 lines)
│
├── .vscode/
│   ├── extensions.json            ← recommended VS Code extensions
│   └── launch.json                ← F5 = run app  |  F5 (tests) = pytest
│
├── .gitignore                     ← excludes venv, __pycache__, tasks.json
├── pytest.ini                     ← tells pytest where to find tests
├── requirements.txt               ← only pytest (app uses stdlib only)
└── README.md                      ← you are here
```

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/cli_task_manager.git
cd cli_task_manager
```

### 2. Open in VS Code
```bash
code .
```
VS Code will prompt you to install the recommended extensions — click **Install All**.

### 3. Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the app

**Option A — terminal:**
```bash
cd task_manager_cli
python main.py
```

**Option B — VS Code:**
Press `F5` and select **"Run Task Manager"** from the dropdown.

### 6. Run the tests

**Option A — terminal (from project root):**
```bash
pytest -v
```

Expected output:
```
tests/test_tasks.py::test_task_creation                  PASSED
tests/test_tasks.py::test_task_strips_whitespace         PASSED
tests/test_tasks.py::test_task_id_increments             PASSED
tests/test_tasks.py::test_task_mark_done                 PASSED
tests/test_tasks.py::test_task_to_dict                   PASSED
tests/test_tasks.py::test_task_from_dict                 PASSED
tests/test_tasks.py::test_save_and_load_roundtrip        PASSED
tests/test_tasks.py::test_load_missing_file              PASSED
tests/test_tasks.py::test_load_corrupted_file            PASSED
tests/test_tasks.py::test_id_counter_synced_after_load   PASSED

10 passed in 0.xxs
```

---

## 🌿 Push to GitHub (First Time)

### Step 1 — Create a new repo on GitHub
1. Go to https://github.com/new
2. Name it `cli_task_manager`
3. Set it to **Public** (or Private)
4. **Do NOT** tick "Add a README" — we already have one
5. Click **Create repository**

### Step 2 — Initialise git locally
```bash
git init
git add .
git commit -m "Initial commit: CLI Task Manager capstone"
```

### Step 3 — Link and push
```bash
git remote add origin https://github.com/YOUR_USERNAME/cli_task_manager.git
git branch -M main
git push -u origin main
```

### Step 4 — Verify
Go to `https://github.com/YOUR_USERNAME/cli_task_manager` — all files visible.

### Making future changes
```bash
git add .
git commit -m "describe what you changed"
git push
```

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | Add task | Enter a title — saved to disk instantly |
| 2 | View all tasks | Formatted list with status + timestamp |
| 3 | Mark done | Pick a task ID to complete it |
| 4 | Delete task | Remove with a confirmation prompt |
| 5 | Filter tasks | Show only pending or completed |
| 6 | Persistent storage | Survives restarts via tasks.json |

---

## 📋 Requirements

- Python 3.10+
- No external libraries for the app
- pytest only for running tests
- Works on Windows, macOS, and Linux

---

## 📖 Full Documentation

See `docs/TOOLKIT_GUIDE.md` for the complete capstone document including
setup screenshots, AI prompt journal, common errors, and all references.

---

## 📄 License

MIT — free to use, fork, and learn from.
