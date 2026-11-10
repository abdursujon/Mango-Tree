
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
--- 

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