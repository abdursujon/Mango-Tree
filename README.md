# Mango-Tree
Mango-Tree is a command line interface (CLI) which also consists of an application programming interface (API). Anyone can use this tool as a task logger instead of having to install a UI interface. 


# Installing Pytest 

```bash
python3 -m venv .venv
source .venv/bin/activate 
pip install pytest 
```
- Running a test 
```bash
cd directory_name 
pytest test_one.py
```
- Getting extra information about test failure 
```bash
cd directory_name 
pytest -v test_one.py 
pytest -vv test_one.py
```
- Turn off traceback 
```bash
cd directory_name 
pytest --tb=no test_one.py
```

- Run multiple test script at the same time 
```bash
pytest --tb=no
```

- Stop python creating pytest_cache
```bash
PYTHONDONTWRITEBYTECODE=1
```

# Topics to Cover

1. Assertions
2. Exceptions
3. Fixtures
4. Builtin fixtures
5. Parametrize
6. Markers
7. Test strategy
8. Configuration files
9. Coverage
10. Mocking
11. tox and CI
12. Testing scripts
13. Debugging
14. Plugins
15. Building plugins
16. Advanced parametrize

# SQLite CRUD Topics

1. Connect and close
2. Create table
3. Insert
4. Select one
5. Select all
6. Update
7. Delete one
8. Delete all
9. Count
10. Placeholders
11. Commit and rollback
12. Row factory
13. Context manager
14. Testing with tmp_path


## Install typer to turn python functions into terminal command 
```bash 
pip install typer 
```