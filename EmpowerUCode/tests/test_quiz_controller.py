import pytest
from unittest.mock import patch
from app.quiz_controller import QuizController

# Fixture to initialize the QuizController with mock quiz data
@pytest.fixture
@patch('app.quiz_controller.parse_quiz_file')
def quiz_controller(mock_parse_quiz_file):
    mock_parse_quiz_file.return_value = [
        {
            "Q": "What is the capital of France?",
            "Type": "mcq",
            "Options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "Answer": "Paris",
            "Hints": ["It's a popular tourist destination.", "It's known for the Eiffel Tower."]
        },
        {
            "Q": "Arrange the following numbers in ascending order.",
            "Type": "drag_and_drop",
            "Options": [],
            "Answer": "1, 2, 3, 4",
            "Hints": ["The smallest number comes first."]
        }
    ]
    return QuizController("dummy_path.txt")

# Test initial state of the controller
def test_initial_state(quiz_controller):
    assert quiz_controller.current_question_index == 0
    assert quiz_controller.user_score == 0
    assert quiz_controller.total_questions == 2
    assert quiz_controller.hint_indices == [0, 0]
    assert quiz_controller.attempts_remaining == 1

# Test retrieving current question
def test_get_current_question(quiz_controller):
    assert quiz_controller.get_current_question()["Q"] == "What is the capital of France?"

# Parametrized test for validating different answers and checking hints
@pytest.mark.parametrize(
    "user_answer, question_type, question_index, expected_correct, expected_hint",
    [
        ("Paris", "mcq", 0, True, ""),  # Correct MCQ answer
        ("London", "mcq", 0, False, "It's a popular tourist destination."),  # Incorrect MCQ with hint
        ("1, 2, 3, 4", "drag_and_drop", 1, True, ""),  # Correct drag-and-drop answer
        ("4, 3, 2, 1", "drag_and_drop", 1, False, "The smallest number comes first.")  # Incorrect drag-and-drop with hint
    ]
)
def test_validate_answer(quiz_controller, user_answer, question_type, question_index, expected_correct, expected_hint):
    if question_index > 0:
        quiz_controller.next_question()  # Move to the second question if needed
    correct, hint = quiz_controller.validate_answer(user_answer, question_type)
    assert correct == expected_correct
    assert hint == expected_hint

# Test progressive hint generation
def test_get_progressive_hint(quiz_controller):
    # Incorrect first answer should return the first hint
    correct, hint = quiz_controller.validate_answer("London", "mcq")
    assert not correct  # Ensure the answer is incorrect
    assert hint == "It's a popular tourist destination."

    # Incorrect second answer should return the second hint
    correct, hint = quiz_controller.validate_answer("Berlin", "mcq")
    assert not correct
    assert hint == "It's known for the Eiffel Tower."

    # Exhausting hints
    correct, hint = quiz_controller.validate_answer("Berlin", "mcq")
    assert not correct
    assert hint == "No more hints available."

# Test moving to the next question
def test_next_question(quiz_controller):
    quiz_controller.next_question()
    assert quiz_controller.get_current_question()["Q"] == "Arrange the following numbers in ascending order."

# Test if there are more questions available
def test_has_more_questions(quiz_controller):
    assert quiz_controller.has_more_questions() is True
    quiz_controller.next_question()  # After the first question
    assert quiz_controller.has_more_questions() is True
    quiz_controller.next_question()  # After the second question
    assert quiz_controller.has_more_questions() is False

# Test score calculation
def test_get_final_score(quiz_controller):
    quiz_controller.increment_score()  # Simulate answering one question correctly
    assert quiz_controller.get_final_score() == (1, 2)

# Test score increment
def test_increment_score(quiz_controller):
    quiz_controller.increment_score()
    assert quiz_controller.user_score == 1

# Test quiz reset functionality
def test_reset_quiz(quiz_controller):
    quiz_controller.increment_score()
    quiz_controller.next_question()
    quiz_controller.reset_quiz()
    assert quiz_controller.current_question_index == 0
    assert quiz_controller.user_score == 0
    assert quiz_controller.hint_indices == [0, 0]
