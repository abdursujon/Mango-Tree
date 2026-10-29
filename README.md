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