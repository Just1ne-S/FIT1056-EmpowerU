def parse_quiz_file(file_path):
    """
    Parses a quiz file and returns a list of questions with details.

    The file should contain sections in this order:
    - ###QUESTION: The question text
    - ###TYPE: The type of the question (e.g., 'mcq', 'coding_task')
    - ###OPTIONS: Possible options for multiple-choice questions
    - ###ANSWER: The correct answer
    - ###HINT: Hints for the question, separated by commas

    Parameters:
    file_path (str): Path to the quiz file.

    Returns:
    List[Dict]: A list of dictionaries where each dictionary contains:
        - "Q": The question text
        - "Type": The question type
        - "Options": Answer options (if applicable)
        - "Answer": The correct answer (if present)
        - "Hints": List of hints for the question.
    """

    quiz_data = []
    current_question = {}
    capture_answer = False
    multiline_answer = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line_num, line in enumerate(lines, 1):
        line = line.rstrip()  # Removes trailing spaces and newlines (no explicit \n)

        # Handle capturing the correct answer
        if line.startswith("###ANSWER"):
            # print(f"Debug: Answer section started at line {line_num}")
            capture_answer = True  # Start capturing answer lines
            multiline_answer = []  # Reset answer buffer
            continue

        if capture_answer:
            if line.startswith("###") and not line.startswith("###ANSWER"):
                capture_answer = False
                current_question["Answer"] = "\n".join(multiline_answer).strip()
                # print(f"Debug: Captured multi-line answer: {current_question['Answer']}")
            elif line == '"""':
                continue
            else:
                multiline_answer.append(line)
                continue

        # Start a new question
        if line.startswith("###QUESTION"):
            if current_question:  # Save the previous question
                quiz_data.append(current_question)
                # print(f"Debug: Saving question: {current_question}")
            current_question = {"Q": lines[line_num].strip(), "Hints": [], "Options": []}  # Ensure 'Options' is always initialized
            # print(f"Debug: New question started at line {line_num}, question: {current_question['Q']}")

        # Parse the question type
        elif line.startswith("###TYPE"):
            current_question["Type"] = lines[line_num].strip()
            # print(f"Debug: Question type: {current_question['Type']}")

        # Capture options for MCQ or Drag-and-Drop questions
        elif line.startswith("###OPTIONS"):
            # print(f"Debug: Options section started at line {line_num}")
            current_question["Options"] = []

        # Capture options (A), B), C), D)) for MCQs
        elif line.startswith("A)") or line.startswith("B)") or line.startswith("C)") or line.startswith("D)"):
            current_question["Options"].append(line)
            # print(f"Debug: Captured option: {line}")

        # Capture hints for progressive hinting
        elif line.startswith("###HINT"):
            hints = [hint.strip() for hint in lines[line_num].split(",")]
            current_question["Hints"] = hints
            # print(f"Debug: Captured hints: {current_question['Hints']}")

    # Add the last question if present
    if current_question:
        # print(f"Debug: Saving last question: {current_question}")
        quiz_data.append(current_question)

    return quiz_data



