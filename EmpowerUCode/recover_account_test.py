import pytest
import tkinter as tk
from interfaces.main_window import MW
from app.compiled_adjust_lines import compiled_adjust_lines

root = MW(title="EmpowerU - Learning Application",width="1200",height="840")
homepage = root.homepage
homepage.recover_account()


def recover_test(firstname, lastname, username, password, confirm_password, code):
    compiled_adjust_lines()
    homepage.recovery.firstname_var.set(firstname)
    homepage.recovery.lastname_var.set(lastname)
    homepage.recovery.username_var.set(username)
    homepage.recovery.new_pass_var.set(password)
    homepage.recovery.confirm_pass_var.set(confirm_password)
    homepage.recovery.activate_var.set(code)
    # Return the result of the sign_up method
    return homepage.recovery.recover_account()

import pytest

# Data used for the existing account: Justin, Siananda, justin, justin123, gif1

@pytest.mark.parametrize("firstname,lastname,username,password,confirm_password,code,expected", [
    # Firstname tests
    ("Justin", "Siananda", "justin", "justin123", "justin123", "gif1", True),    # Valid input
    ("", "Siananda", "justin", "justin123", "justin123", "gif1", False),         # Firstname empty
    ("Jus tin", "Siananda", "justin", "justin123", "justin123", "gif1", False),  # Firstname contains spaces
    ("Justin2", "Siananda", "justin", "justin123", "justin123", "gif1", False),  # Firstname contains digits
    ("Justinee", "Siananda", "justin", "justin123", "justin123", "gif1", False), # Firstname doesn't match up

    # Lastname tests
    ("Justin", "Siananda", "justin", "justin123", "justin123", "gif1", True),    # Valid input
    ("Justin", "", "justin", "justin123", "justin123", "gif1", False),           # Lastname empty
    ("Justin", "Sian anda", "justin", "justin123", "justin123", "gif1", False),  # Lastname contains spaces
    ("Justin", "Siananda1", "justin", "justin123", "justin123", "gif1", False),  # Lastname contains digits
    ("Justin", "Sian", "justin", "justin123", "justin123", "gif1", False),  # Lastname doesn't match up

    # Username tests
    ("Justin", "Siananda", "justin", "justin123", "justin123", "gif1", True),    # Valid input
    ("Justin", "Siananda", "", "justin123", "justin123", "gif1", False),         # Username empty
    ("Justin", "Siananda", "just in", "justin123", "justin123", "gif1", False),  # Username contains spaces

    # Password tests
    ("Justin", "Siananda", "justin", "justin123", "justin123", "gif1", True),    # Valid input
    ("Justin", "Siananda", "justin", "justin123", "different", "gif1", False),   # Passwords do not match
    ("Justin", "Siananda", "justin", "just in123", "just in123", "gif1", False), # Password contains spaces

    # Activation code tests
    ("Justin", "Siananda", "justin", "justin123", "justin123", None, False),     # Activation code is None
    ("Justin", "Siananda", "justin", "justin123", "justin123", "wrong", False),  # Invalid activation code
])


def test(firstname,lastname,username,password,confirm_password,code,expected):
    assert recover_test(firstname,lastname,username,password,confirm_password,code) == expected