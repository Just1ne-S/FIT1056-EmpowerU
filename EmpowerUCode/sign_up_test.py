import pytest
import tkinter as tk
from interfaces.main_window import MW

root = MW(title="EmpowerU - Learning Application",width="1200",height="840")




def sign_up_test(firstname, lastname, phonenumber, username, password, confirm_password, code):
    root.sign_up_page.firstname_var.set(firstname)
    root.sign_up_page.lastname_var.set(lastname)
    root.sign_up_page.phonenumber_var.set(phonenumber)
    root.sign_up_page.username_var.set(username)
    root.sign_up_page.password_var.set(password)
    root.sign_up_page.confirm_password_var.set(confirm_password)
    root.sign_up_page.activate_var.set(code)
    # Return the result of the sign_up method
    return root.sign_up_page.sign_up()


@pytest.mark.parametrize("firstname,lastname,phonenumber,username,password,confirm_password,code,expected", [
    # Firstname tests
    ("Justin", "Siananda", "0408005595", "justine", "justin123", "justin123", "gif2", True),   # Valid input
    ("", "Siananda", "0408005595", "justine", "justin123", "justin123", "gif2", False),        # Firstname empty
    ("Jus tin", "Siananda", "0408005595", "justine", "justin123", "justin123", "gif2", False), # Firstname contains spaces
    ("Justin2", "Siananda", "0408005595", "justine", "justin123", "justin123", "gif2", False), # Firstname contains digits

    # Lastname tests
    ("Justin", "Siananda", "0408005595", "justRight", "justin123", "justin123", "gif2", True), # Valid input
    ("Justin", "", "0408005595", "justine", "justin123", "justin123", "gif2", False),          # Lastname empty
    ("Justin", "Sian anda", "0408005595", "justine", "justin123", "justin123", "gif2", False), # Lastname contains spaces
    ("Justin", "Siananda1", "0408005595", "justine", "justin123", "justin123", "gif2", False), # Lastname contains digits

    # Phonenumber tests
    ("Justin", "Siananda", "0408005595", "justDoing", "justin123", "justin123", "gif2", True), # Valid input
    ("Justin", "Siananda", "", "justine", "justin123", "justin123", "gif2", False),            # Phone number empty
    ("Justin", "Siananda", "04080 05595", "justine", "justin123", "justin123", "gif2", False), # Phone number contains spaces
    ("Justin", "Siananda", "abcdxyz123", "justine", "justin123", "justin123", "gif2", False),  # Phone number contains letters
    ("Justin", "Siananda", "12345", "justine", "justin123", "justin123", "gif2", False),       # Phone number not 10 digits

    # Username tests
    ("Justin", "Siananda", "0408005595", "justCool", "justin123", "justin123", "gif2", True),  # Valid input
    ("Justin", "Siananda", "0408005595", "", "justin123", "justin123", "gif2", False),         # Username empty
    ("Justin", "Siananda", "0408005595", "just ine", "justin123", "justin123", "gif2", False), # Username contains spaces

    # Password tests
    ("Justin", "Siananda", "0408005595", "justin123", "justin123", "justin123", "gif2", True), # Valid input
    ("Justin", "Siananda", "0408005595", "justine", "justin123", "different", "gif2", False),  # Passwords do not match
    ("Justin", "Siananda", "0408005595", "justine", "just in123", "just in123", "gif2", False),# Password contains spaces

    # Activation code tests
    ("Justin", "Siananda", "0408005595", "justine", "justin123", "justin123", None, False),    # Activation code is None
])

def test(firstname,lastname,phonenumber,username,password,confirm_password,code,expected):
    assert sign_up_test(firstname,lastname,phonenumber,username,password,confirm_password,code) == expected

