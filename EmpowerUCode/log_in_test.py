import pytest 
import tkinter as tk 
from interfaces.main_window import MW
from app.compiled_adjust_lines import compiled_adjust_lines

compiled_adjust_lines()
root = MW(title="EmpowerU - Learning Application", width="1200", height="840")

def login_test(username, password):
    root.homepage.username_var.set(username)
    root.homepage.password_var.set(password)

    return root.homepage.login()



@pytest.mark.parametrize("username, password, expected", [
    ("justin", "justin", True),
    ("anyone", "anyone", False),
    ("jane", "1234", False),
    ("", "12345", False),
    ("jack", "", False),
])

def test_login(username, password, expected):
    assert login_test(username, password) == expected 
