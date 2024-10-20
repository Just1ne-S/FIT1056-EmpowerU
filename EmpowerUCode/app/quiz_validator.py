class QuizValidator:
    """A class to validate quiz answers for different question types."""

    @staticmethod
    def validate_mcq(selected_answer, correct_answer):
        """
        Validate a multiple-choice question.
        :param selected_answer: The answer selected by the user
        :param correct_answer: The correct answer
        :return: True if correct, False otherwise
        """
        return selected_answer.strip().lower() == correct_answer.strip().lower()

    @staticmethod
    def validate_coding_task(user_code, correct_code):
        """
        Validate a coding task by comparing the user's code with the correct code.
        :param user_code: Code submitted by the user
        :param correct_code: The correct code
        :return: True if the code matches the correct code (ignores formatting differences), False otherwise
        """
        # Normalize the user's code and correct code by removing extra spaces and line breaks
        normalized_user_code = "\n".join([line.strip() for line in user_code.splitlines() if line.strip()])
        normalized_correct_code = "\n".join([line.strip() for line in correct_code.splitlines() if line.strip()])

        # Compare the normalized code
        return normalized_user_code == normalized_correct_code

    def validate_drag_and_drop(user_order, correct_order):
        """
        Validate a drag-and-drop question by comparing the order of elements.
        :param user_order: String input of elements in the order selected by the user
        :param correct_order: String representing the correct order (e.g., "1, 4, 2, 3")
        :return: True if the order matches, False otherwise
        """
        user_order_list = [x.strip() for x in user_order.split(",")]
        correct_order_list = [x.strip() for x in correct_order.split(",")]
        return user_order_list == correct_order_list

    @staticmethod
    def provide_hint(question_data):
        """
        Provide a hint based on the question type.
        :param question_data: Dictionary containing question information (including the 'Hint' field)
        :return: The relevant hint if available, otherwise a default message
        """
        return question_data.get('Hint', "No hint available.")