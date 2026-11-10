# Mango-Tree
Mango-Tree is a CLI task manager for developers who live in the terminal. Add, track and finish your tasks without leaving the command line, with no GUI to install.

# User Guide 
## Requirements
- Python 3.10 or newer
- git
- pipx (`pip install pipx` or `sudo apt install pipx`)

## Install
```bash
pipx install git+https://github.com/abdursujon/Mango-Tree.git@v0.0.1
```

## Commands
```bash
mango-tree add "water the plants"           # add a task
mango-tree add "water the plants" -o sujon  # add a task with an owner
mango-tree                                  # list all tasks
mango-tree list -o sujon                    # list tasks by owner
mango-tree list -s done                     # list tasks by state (todo, in prog, done)
mango-tree start 1                          # set task 1 to in prog
mango-tree finish 1                         # set task 1 to done
mango-tree update 1 -o ali                  # change the owner of task 1
mango-tree update 1 -s "water the garden"   # change the summary of task 1
mango-tree delete 1                         # delete task 1
mango-tree count                            # number of tasks
mango-tree config                           # path to the database
mango-tree version                          # app version
mango-tree --help                           # show all commands
```

Tasks are saved in `~/mango_tree_db`. To store them somewhere else, set `MANGO_TREE_DB_DIR`:
```bash
export MANGO_TREE_DB_DIR=~/your_directory_name
```
For example, to store tasks in ~/Documents/tasks:
```bash
export MANGO_TREE_DB_DIR=~/Documents/tasks
```
Add above line to `~/.bashrc` (or `~/.zshrc`) to keep it permanently.

# Developer Guide
## Setup
```bash
git clone https://github.com/abdursujon/Mango-Tree.git
cd Mango-Tree
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest
```
`pip install -e .` installs Typer and Rich, and links the `mango-tree` command to your local code, so changes take effect without reinstalling.

## Run the app
```bash
mango-tree
```

## Run the tests
```bash
pytest tests/mango_tree_tests
```

## Use a test database while developing
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

## Project structure
```
src/mango_tree/
    db.py     # SQLite storage, the only file with SQL
    api.py    # MangoTree dataclass, exceptions and MangoTreeService logic
    cli.py    # Typer commands that call the API
tests/
    mango_tree_tests/
```
