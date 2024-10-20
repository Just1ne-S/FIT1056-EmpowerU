import os


def read_file(file_path):
    """
    Read the content of a file.
    :param file_path: Path to the file
    :return: File content as a string
    :raises: FileNotFoundError, IOError
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        with open(file_path, 'r') as file:
            return file.read()

    except FileNotFoundError as fnf_error:
        raise fnf_error
    except IOError as io_error:
        raise io_error


def write_file(file_path, content):
    """
    Write content to a file.
    :param file_path: Path to the file
    :param content: Content to write into the file
    :raises: IOError
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as io_error:
        raise io_error


# def parse_quiz_file(file_path):
#     """
#     Parses a quiz file using defined delimiters and returns a list of questions.
#     :param file_path: Path to the quiz file
#     :return: List of dictionaries containing questions, answers, and other attributes including progressive hints.
#     """
#     quiz_data = []
#     current_question = {}
#     inside_multiline_answer = False
#     multiline_answer = []
#
#     with open(file_path, "r") as file:
#         lines = file.readlines()
#
#     for line_num, line in enumerate(lines, 1):
#         line = line.strip()
#
#         # Handle multi-line answers (for coding tasks)
#         if inside_multiline_answer:
#             if line == '"""':  # End of multi-line answer
#                 current_question["Answer"] = "\n".join(multiline_answer).strip()
#                 inside_multiline_answer = False
#                 multiline_answer = []
#             else:
#                 multiline_answer.append(line)
#             continue
#
#         # Start a new question
#         if line.startswith("###QUESTION"):
#             if current_question:  # Save the previous question
#                 quiz_data.append(current_question)
#             current_question = {"Q": lines[line_num].strip(), "Hints": []}  # Initialize with an empty hints list
#
#         # Parse the question type
#         elif line.startswith("###TYPE"):
#             current_question["Type"] = lines[line_num].strip()
#
#         # Parse options for MCQ or Drag-and-Drop questions
#         elif line.startswith("###OPTIONS"):
#             current_question["Options"] = []
#
#         # Capture options (A), B), C), D)) for MCQs
#         elif line.startswith("A)") or line.startswith("B)") or line.startswith("C)") or line.startswith("D)"):
#             current_question["Options"].append(line)
#
#         # Capture instructions for coding tasks
#         elif line.startswith("###INSTRUCTIONS"):
#             current_question["Instructions"] = lines[line_num].strip()
#
#         # Capture the correct answer
#         elif line.startswith("###ANSWER"):
#             if lines[line_num].startswith('"""'):  # Start multi-line answer for coding tasks
#                 inside_multiline_answer = True
#             else:
#                 current_question["Answer"] = lines[line_num].strip()
#
#         # Capture hints for progressive hinting
#         elif line.startswith("###HINT"):
#             hints = [hint.strip() for hint in lines[line_num].split(",")]  # Split by commas and remove leading/trailing spaces
#             current_question["Hints"] = hints
#
#     # Add the last question if present
#     if current_question:
#         quiz_data.append(current_question)
#
#     return quiz_data

def parse_quiz_file(file_path):
    """
    Parses a quiz file using defined delimiters and returns a list of questions.
    :param file_path: Path to the quiz file
    :return: List of dictionaries containing questions, answers, and other attributes including progressive hints.
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


def parse_tutorial_file(file_path):
    """
    Parses a tutorial file and returns a structured dictionary of sections and content.
    :param file_path: Path to the tutorial file
    :return: List of dictionaries containing section titles and their respective content.
    """
    tutorial_data = []
    current_section = {}
    intro_section = {"section_title": "Introduction", "content": ""}  # To handle intro

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        # print(f"Processing line {line_num}: {line}")  # Debugging statement

        # Handle the tutorial title (single title per file)
        if line.startswith("# "):
            tutorial_data.append({"title": line[2:], "sections": []})
            # print(f"Tutorial title set: {line[2:]}")  # Debugging statement

        # Handle section titles
        elif line.startswith("## "):
            # Append intro section if it has content and no other sections exist yet
            if intro_section["content"] and not tutorial_data[-1]["sections"]:
                # print(f"Appending intro section: {intro_section}")
                tutorial_data[-1]["sections"].append(intro_section)

            # Append the previous section if it exists
            if current_section and "section_title" in current_section:
                # print(f"Appending section: {current_section}")  # Debugging statement
                tutorial_data[-1]["sections"].append(current_section)

            # Start a new section
            current_section = {"section_title": line[3:], "content": ""}
            # print(f"New section: {current_section}")  # Debugging statement

        # Handle content within sections or introduction (inside triple quotes)
        elif line.startswith('"""') or line.endswith('"""'):
            content_line = line.strip('"""')
            if current_section:
                current_section["content"] += content_line + "\n"
            else:
                intro_section["content"] += content_line + "\n"
            # print(f"Content added: {current_section['content'] if current_section else intro_section['content']}")  # Debugging statement

        else:
            # Add to section content or intro content
            if current_section:
                current_section["content"] += line + "\n"
                # print(f"Line added to content: {line}")
            else:
                intro_section["content"] += line + "\n"
                # print(f"Line added to intro content: {line}")

    # Append the last section to the tutorial data
    if current_section and "section_title" in current_section:
        # print(f"Appending last section: {current_section}")
        tutorial_data[-1]["sections"].append(current_section)

    # Ensure that the introduction is added if it exists and no sections are added
    if intro_section["content"] and not tutorial_data[-1]["sections"]:
        # print(f"Appending intro section at the end: {intro_section}")
        tutorial_data[-1]["sections"].append(intro_section)

    return tutorial_data
