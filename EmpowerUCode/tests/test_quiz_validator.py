import pytest
import sys

sys.path.append("../app")
from quiz_validator import QuizValidator


@pytest.mark.parametrize(
    "selected_answer, correct_answer, expected_result",
    [
        ("B", "B", True),  # Test when selected answer is correct
        ("A", "B", False),  # Test when selected answer is incorrect
        ("b", "B", True),  # Test case insensitivity
        ("  B  ", "B", True),  # Test with extra whitespaces
        (" C", "C ", True),  # Test with leading and trailing whitespaces on both sides
        ("d", "D", True),  # Test with case and whitespace normalization
    ]
)
def test_validate_mcq(selected_answer, correct_answer, expected_result):
    """
    Test validate_mcq for multiple cases using pytest.mark.parametrize.
    """
    assert QuizValidator.validate_mcq(selected_answer, correct_answer) == expected_result


@pytest.mark.parametrize(
    "user_code, correct_code, expected_result",
    [
        # Test case where the code is exactly the same
        (
                """def add(a, b):
        return a + b""",
                """def add(a, b):
        return a + b""",
                True
        ),
        # Test case where there are different amounts of whitespace but the code is logically the same
        (
                """def add(a, b):  
        return a + b  
    """,
                """def add(a, b):
        return a + b""",
                True
        ),
        # Test case where user code has extra newlines
        (
                """def add(a, b):
    
        return a + b
    """,
                """def add(a, b):
        return a + b""",
                True
        ),
        # Test case where the code is logically different
        (
                """def subtract(a, b):
        return a - b""",
                """def add(a, b):
        return a + b""",
                False
        ),
        # Test case where the code has a different function name but same logic
        (
                """def sum_two_numbers(a, b):
        return a + b""",
                """def add(a, b):
        return a + b""",
                False
        )
    ]
)
def test_validate_coding_task(user_code, correct_code, expected_result):
    assert QuizValidator.validate_coding_task(user_code, correct_code) == expected_result
