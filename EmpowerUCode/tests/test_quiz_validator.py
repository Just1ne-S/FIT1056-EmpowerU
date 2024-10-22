import pytest
from quiz_validator import QuizValidator


@pytest.mark.parametrize(
    "selected_answer, correct_answer, expected_result",
    [
        # Equivalence class: Matching correct answers
        # Boundary value: Normal case with exact match
        ("B", "B", True),  # Test when selected answer is correct

        # Equivalence class: Incorrect answers
        ("A", "B", False),  # Test when selected answer is incorrect

        # Equivalence class: Case insensitive inputs
        # Boundary value: Testing case insensitivity
        ("b", "B", True),  # Test case insensitivity

        # Equivalence class: Whitespace variations
        # Boundary value: Leading/trailing whitespace, but logically same answer
        ("  B  ", "B", True),  # Test with extra whitespaces

        # Equivalence class: Minor format differences (leading/trailing spaces)
        # MC/DC: Test both conditions (strip and lower) independently affect the result
        (" C", "C ", True),  # Test with leading and trailing whitespaces on both sides

        # Equivalence class: Fully incorrect answers
        ("d", "D", True),  # Test with case and whitespace normalization
    ]
)
def test_validate_mcq(selected_answer, correct_answer, expected_result):
    """
    Test validate_mcq for multiple cases using equivalence class partitioning,
    boundary value analysis, and MC/DC coverage.
    """
    assert QuizValidator.validate_mcq(selected_answer, correct_answer) == expected_result


# Test cases for validate_coding_task method
@pytest.mark.parametrize(
    "user_code, correct_code, expected_result",
    [
        # Equivalence class: Identical code
        # Boundary value: Exact match
        (
                """def add_two_numbers(a, b):
        return a + b""",
                """def add_two_numbers(a, b):
        return a + b""",
                True
        ),

        # Equivalence class: Same logic, different formatting
        # Boundary value: Extra spaces/new lines
        (
                """def add_two_numbers(a, b):
    
        return a + b
                """,
                """def add_two_numbers(a, b):\n    return a + b""",
                True
        ),

        # Equivalence class: Different logic (incorrect logic)
        (
                """def add_two_numbers(a, b):
        return a - b""",
                """def add_two_numbers(a, b):
        return a + b""",
                False
        ),

        # Equivalence class: Same logic, but different formatting (indentation)
        # Boundary value: Formatting differences
        (
                """def add_two_numbers(a, b):
            return a + b
                """,
                """def add_two_numbers(a, b):\n    return a + b""",
                True
        ),

        # Equivalence class: Function name mismatch (logic is same, name differs)
        # MC/DC: Test function name affects the outcome
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
    """
    Test validate_coding_task for multiple cases using equivalence class partitioning,
    boundary value analysis, and MC/DC coverage.
    """
    result = QuizValidator.validate_coding_task(user_code, correct_code)
    assert result == expected_result


@pytest.mark.parametrize(
    "user_order, correct_order, expected_result",
    [
        # Equivalence class: Correct order
        ("1, 2, 3, 4", "1, 2, 3, 4", True),

        # Equivalence class: One element out of order
        ("1, 3, 2, 4", "1, 2, 3, 4", False),

        # Equivalence class: Completely incorrect order
        ("4, 3, 2, 1", "1, 2, 3, 4", False),

        # Equivalence class: Correct order but extra spaces
        # Boundary value: Extra spaces but logically correct
        ("1,  2, 3,   4", "1,2,3,4", True),

        # Equivalence class: More items in user input than expected
        ("1, 2, 3, 4, 5", "1, 2, 3, 4", False),

        # Equivalence class: Fewer items in user input than expected
        ("1, 2", "1, 2, 3, 4", False),

        # Equivalence class: Correct set but incorrect order for one element
        # MC/DC: The order of elements affects the final decision
        ("1, 2, 4, 3", "1, 2, 3, 4", False),
    ]
)
def test_validate_drag_and_drop(user_order, correct_order, expected_result):
    """
    Test validate_drag_and_drop for multiple cases using equivalence class partitioning,
    boundary value analysis, and MC/DC coverage.
    """
    result = QuizValidator.validate_drag_and_drop(user_order, correct_order)
    assert result == expected_result
