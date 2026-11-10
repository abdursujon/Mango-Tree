# Mango-Tree

A CLI task manager for developers who live in the terminal. Add, track and finish your tasks without leaving the command line, with no GUI to install.

## Contents

- [User Guide](#user-guide)
  - [Requirements](#requirements)
  - [Install](#install)
  - [Commands](#commands)
  - [Database location](#database-location)
- [Developer Guide](#developer-guide)
  - [Setup](#setup)
  - [Run the app](#run-the-app)
  - [Run the tests](#run-the-tests)
  - [Use a test database](#use-a-test-database)
  - [Project structure](#project-structure)

---

## User Guide

### Requirements

- Python 3.10 or newer
- git
- pipx (`pip install pipx` or `sudo apt install pipx`)

### Install

```bash
pipx install git+https://github.com/abdursujon/Mango-Tree.git@v0.0.1
```

### Commands

| Command | Description |
| --- | --- |
| `mango-tree add "water the plants"` | Add a task |
| `mango-tree add "water the plants" -o sujon` | Add a task with an owner |
| `mango-tree` | List all tasks |
| `mango-tree list -o sujon` | List tasks by owner |
| `mango-tree list -s done` | List tasks by state (`todo`, `in prog`, `done`) |
| `mango-tree start 1` | Set task 1 to `in prog` |
| `mango-tree finish 1` | Set task 1 to `done` |
| `mango-tree update 1 -o ali` | Change the owner of task 1 |
| `mango-tree update 1 -s "water the garden"` | Change the summary of task 1 |
| `mango-tree delete 1` | Delete task 1 |
| `mango-tree count` | Show the number of tasks |
| `mango-tree config` | Show the database path |
| `mango-tree version` | Show the app version |
| `mango-tree --help` | Show all commands |

### Database location

Tasks are saved in `~/mango_tree_db` by default. To store them somewhere else, set `MANGO_TREE_DB_DIR`:

```bash
export MANGO_TREE_DB_DIR=~/Documents/tasks
```

Add that line to `~/.bashrc` (or `~/.zshrc`) to keep it permanently.

---

## Developer Guide

### Setup

```bash
git clone https://github.com/abdursujon/Mango-Tree.git
cd Mango-Tree
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest
```

`pip install -e .` installs Typer and Rich, and links the `mango-tree` command to your local code, so changes take effect without reinstalling.

### Run the app

```bash
mango-tree
```

### Run the tests

```bash
pytest tests/mango_tree_tests
```

### Use a test database

Point the app at a throwaway folder so your real tasks are not touched. This only lasts for the current terminal.

```bash
export MANGO_TREE_DB_DIR=/tmp/mango_tree_test
mango-tree add "test task"
mango-tree
```

Switch back to the real database:

```bash
unset MANGO_TREE_DB_DIR
```

In pytest, give each test its own empty database:

```python
monkeypatch.setenv("MANGO_TREE_DB_DIR", str(tmp_path))
```

### Project structure

```
src/mango_tree/
├── db.py     # SQLite storage, the only file with SQL
├── api.py    # MangoTree dataclass, exceptions and MangoTreeService logic
└── cli.py    # Typer commands that call the API
tests/
└── mango_tree_tests/
```
