import pytest
import sys

sys.path.append("../app")
from file_handler import parse_quiz_file

# Parametrize the tests to cover various quiz file formats and outcomes

@pytest.mark.parametrize(
    "quiz_content, expected_length, expected_results",
    [
        (
            # Test case 1: Normal valid quiz with two questions
            """\
###QUESTION
What is Python?
###TYPE
mcq
###OPTIONS
A) A snake
B) A programming language
C) A fruit
###ANSWER
B
###HINT
Python is a popular programming language, It is widely used in web development and data science.

###QUESTION
Write a function that adds two numbers.
###TYPE
coding_task
###ANSWER
\"\"\"
def add_two_numbers(a, b):
    return a + b
\"\"\"
###HINT
Use the return statement, Add the two parameters together.
""",  # Quiz content
            2,  # Expected number of questions
            [
                {
                    "Q": "What is Python?",
                    "Answer": "B",
                    "Options": ["A) A snake", "B) A programming language", "C) A fruit"],
                    "Hints": [
                        "Python is a popular programming language",
                        "It is widely used in web development and data science."
                    ]
                },
                {
                    "Q": "Write a function that adds two numbers.",
                    "Answer": "def add_two_numbers(a, b):\n    return a + b",
                    "Hints": ["Use the return statement", "Add the two parameters together."]
                }
            ]  # Expected result
        ),
        (
            # Test case 2: Incomplete quiz with missing answer and options
            """\
###QUESTION
What is an incomplete question?
###TYPE
mcq
###HINT
This question is incomplete, Missing options and answer.
""",
            1,
            [
                {
                    "Q": "What is an incomplete question?",
                    "Options": [],
                    "Hints": ["This question is incomplete", "Missing options and answer."]
                }
            ]
        ),
        (
            # Test case 3: Empty quiz file
            "",
            0,
            []
        )
    ]
)
def test_parse_quiz_file_parametrize(tmp_path, quiz_content, expected_length, expected_results):
    """
    Test parsing a quiz file with different content using pytest.mark.parametrize.
    """
    quiz_file = tmp_path / "quiz_parametrize.txt"
    quiz_file.write_text(quiz_content)

    result = parse_quiz_file(quiz_file)

    assert len(result) == expected_length, f"There should be {expected_length} questions parsed."

    # Check if results match expected values
    for idx, expected in enumerate(expected_results):
        assert result[idx]["Q"] == expected["Q"], f"Question {idx + 1} should match."
        if "Answer" in expected:
            assert result[idx]["Answer"] == expected["Answer"], f"Answer for question {idx + 1} should match."
        if "Options" in expected:
            assert result[idx]["Options"] == expected["Options"], f"Options for question {idx + 1} should match."
        if "Hints" in expected:
            assert result[idx]["Hints"] == expected["Hints"], f"Hints for question {idx + 1} should match."


@pytest.mark.parametrize(
    "quiz_content, expected_length, expected_missing_answer",
    [
        (
            # Malformed answer test case
            """\
###QUESTION
What is 2 + 2?
###TYPE
coding_task
###ANSWER
\"\"\"
def add(a, b):
    return a + b  # Missing end of answer delimiter
""",
            1,
            True
        ),
        (
            # Missing answer section test case
            """\
###QUESTION
What is 3 + 3?
###TYPE
mcq
###OPTIONS
A) 5
B) 6
C) 7
""",
            1,
            True
        )
    ]
)
def test_parse_quiz_file_invalid_cases(tmp_path, quiz_content, expected_length, expected_missing_answer):
    """
    Test parsing a quiz file with invalid content or missing answer sections.
    """
    quiz_file = tmp_path / "quiz_invalid_cases.txt"
    quiz_file.write_text(quiz_content)

    result = parse_quiz_file(quiz_file)

    assert len(result) == expected_length, f"There should be {expected_length} question(s) parsed."

    if expected_missing_answer:
        assert "Answer" not in result[0], "Answer should not be captured due to format issues."
