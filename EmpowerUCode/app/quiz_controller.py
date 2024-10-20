from file_handler import parse_quiz_file
from quiz_validator import QuizValidator


class QuizController:
    def __init__(self, quiz_file_path, is_interactive=False):
        """
        Initializes the QuizController with a path to the quiz file and mode (interactive/test-like).
        :param quiz_file_path: Path to the .txt quiz file
        :param is_interactive: If True, the quiz is in interactive mode with hints; otherwise, it's a test-like mode.
        """
        self.quiz_data = parse_quiz_file(quiz_file_path)
        self.is_interactive = is_interactive  # If True, hints are shown and retries are allowed
        self.current_question_index = 0
        self.user_score = 0
        self.total_questions = len(self.quiz_data)
        self.hint_indices = [0] * self.total_questions  # Store hint indices for each question
        self.attempts_remaining = 1 if not is_interactive else float('inf')  # One attempt for test mode


    def get_current_question(self):
        """Returns the current question data."""
        if self.current_question_index < self.total_questions:
            return self.quiz_data[self.current_question_index]
        else:
            return None

    def validate_answer(self, user_answer, question_type):
        """
        Validates the user's answer based on the question type.
        :param user_answer: The answer provided by the user.
        :param question_type: The type of question (mcq, coding_task, drag_and_drop).
        :return: Tuple (boolean indicating correct/incorrect, hint if interactive and incorrect).
        """
        question = self.quiz_data[self.current_question_index]
        correct_answer = question["Answer"]


        if question_type == "mcq":
            correct = QuizValidator.validate_mcq(user_answer, correct_answer)
        elif question_type == "coding_task":
            correct = QuizValidator.validate_coding_task(user_answer, correct_answer)
        elif question_type == "drag_and_drop":
            correct = QuizValidator.validate_drag_and_drop(user_answer, correct_answer)
        else:
            correct = False

        # Provide progressive hint if incorrect and interactive
        if not correct and self.is_interactive:
            hint = self.get_progressive_hint()
        else:
            hint = ""

        return correct, hint

    def get_progressive_hint(self):
        """
        Returns the next hint from the list of hints for the current question.
        Only increments the hint index if there are more hints available.
        """
        question = self.quiz_data[self.current_question_index]
        hints = question.get("Hints", [])

        # Check if there are any hints left to show
        current_hint_index = self.hint_indices[self.current_question_index]

        # Only proceed if there are more hints to show
        if hints and current_hint_index < len(hints):
            hint = hints[current_hint_index]
            self.hint_indices[self.current_question_index] += 1  # Move to the next hint for this question
            return hint
        else:
            return "No more hints available."

    def next_question(self):
        """Moves to the next question."""
        self.current_question_index += 1
        if self.current_question_index < self.total_questions:
            return self.quiz_data[self.current_question_index]
        else:
            return None

    def has_more_questions(self):
        """Checks if there are more questions in the quiz."""
        return self.current_question_index < self.total_questions

    def get_final_score(self):
        """Returns the user's final score."""
        return self.user_score, self.total_questions

    def increment_score(self):
        """Increments the user's score."""
        self.user_score += 1

    def reset_quiz(self):
        """Resets the quiz state."""
        self.current_question_index = 0
        self.user_score = 0
        self.hint_indices = [0] * self.total_questions
