Use this command to run the test, without headless mode:
pytest tests/test_book.py

Use this command to run the test, in headless mode
pytest tests/test_book.py --mode="headless"

The framework consists of three modules:
conftest.py: which the ClassSetUp method as a class-scope fixture. The module has the code to select headless mode or not as well as to execute the first three steps (i.e. the searching part)
test_book.py: when this code is executed with the command above, pytest runs first the ClassSetUp fixture before any methods in test_book.py are executed
util.py: has the code to take a screenshot

Also added are the json files, an allure report and a screenshot of a failed test.
