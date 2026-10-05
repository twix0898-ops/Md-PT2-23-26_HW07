test_results = [
    {"name": "login_test", "status": "passed", "duration": 2.1},
    {"name": "payment_test", "status": "failed", "duration": 3.5},
    {"name": "logout_test", "status": "passed", "duration": 1.2}
]

def is_successful(test):
    return test["status"] == "passed"

successful_tests = list(filter(is_successful, test_results))
names = [test["name"] for test in successful_tests]

print("Успешные тесты:", names)

tests = [
    {"name": "complex_test", "duration": 5.2},
    {"name": "simple_test", "duration": 1.1},
    {"name": "medium_test", "duration": 3.4}
]

sorted_tests = sorted(tests, key=lambda test: test["duration"])

print("Тесты по времени выполнения:", sorted_tests)