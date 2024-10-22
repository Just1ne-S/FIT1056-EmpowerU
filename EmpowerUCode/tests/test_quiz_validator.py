import pytest
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



# Test cases for validate_coding_task method
@pytest.mark.parametrize(
    "user_code, correct_code, expected_result",
    [
        # Test case 1: Exact match of user code and correct code
        (
            """def add_two_numbers(a, b):
    return a + b""",
            """def add_two_numbers(a, b):
    return a + b""",
            True
        ),
        # Test case 2: User code with extra spaces and different formatting
        (
            """def add_two_numbers(a, b):

    return a + b
            """,
            """def add_two_numbers(a, b):\n    return a + b""",
            True
        ),
        # Test case 3: Code that doesn't match
        (
            """def add_two_numbers(a, b):
    return a - b""",
            """def add_two_numbers(a, b):
    return a + b""",
            False
        ),
        # Test case 4: Code with different indentation but same logic
        (
            """def add_two_numbers(a, b):
        return a + b
            """,
            """def add_two_numbers(a, b):\n    return a + b""",
            True
        ),
        # Test case 5: Mismatch in function name
        (
            """def sum_two_numbers(a, b):
    return a + b""",
            """def add_two_numbers(a, b):
    return a + b""",
            False
        )
    ]
)
def test_validate_coding_task(user_code, correct_code, expected_result):
    result = QuizValidator.validate_coding_task(user_code, correct_code)
    assert result == expected_result


@pytest.mark.parametrize(
    "user_order, correct_order, expected_result",
    [
        # Test case 1: Exact match in order
        ("1, 2, 3, 4", "1, 2, 3, 4", True),

        # Test case 2: Partial match (one element out of order)
        ("1, 3, 2, 4", "1, 2, 3, 4", False),

        # Test case 3: Completely incorrect order
        ("4, 3, 2, 1", "1, 2, 3, 4", False),

        # Test case 4: Extra spaces in user input but order matches
        ("1,  2, 3,   4", "1,2,3,4", True),

        # Test case 5: Different lengths (more items in user input)
        ("1, 2, 3, 4, 5", "1, 2, 3, 4", False),

        # Test case 6: Different lengths (fewer items in user input)
        ("1, 2", "1, 2, 3, 4", False),

        # Test case 7: Order matches, but one element is different
        ("1, 2, 4, 3", "1, 2, 3, 4", False),
    ]
)
def test_validate_drag_and_drop(user_order, correct_order, expected_result):
    result = QuizValidator.validate_drag_and_drop(user_order, correct_order)
    assert result == expected_result

