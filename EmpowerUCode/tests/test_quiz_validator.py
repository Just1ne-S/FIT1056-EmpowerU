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
