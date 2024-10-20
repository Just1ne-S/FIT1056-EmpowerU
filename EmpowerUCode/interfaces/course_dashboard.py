import tkinter as tk
from tkinter import ttk, messagebox
import os

# Assuming these paths or their equivalents exist
TUTORIAL_FILE_PATHS = {
    "Python": "/Users/krishnaagarwal/Desktop/FIT1056-EmpowerU/EmpowerUCode/data/tutorials/python_tutorial.txt",
    "Information Security": "/Users/krishnaagarwal/Desktop/FIT1056-EmpowerU/EmpowerUCode/data/tutorials/infosec_tutorial.txt",
    "AI": "/Users/krishnaagarwal/Desktop/FIT1056-EmpowerU/EmpowerUCode/data/tutorials/ai_tutorial.txt"
}

QUIZ_FILE_PATHS = {
    "Python": "/Users/krishnaagarwal/Desktop/FIT1056-EmpowerU/EmpowerUCode/data/quizzes/python_quiz.txt",
    "Information Security": "/Users/krishnaagarwal/Desktop/FIT1056-EmpowerU/EmpowerUCode/data/quizzes/infosec_quiz.txt",
    "AI": "/Users/krishnaagarwal/Desktop/FIT1056-EmpowerU/EmpowerUCode/data/quizzes/ai_quiz.txt"
}

# Import your existing Tutorial and Quiz UI classes
from tutorial_ui import TutorialUI
from quiz_ui import QuizUI


class CourseDashboard(tk.Tk):
    def __init__(self, course_name, progress_tracker):
        super().__init__()

        self.course_name = course_name
        self.progress_tracker = progress_tracker

        self.title(f"{course_name} Dashboard")
        self.geometry("800x600")

        # Title label for the dashboard
        tk.Label(self, text=f"{course_name} Dashboard", font=("Arial", 16, "bold")).pack(pady=20)

        # Add Buttons for Interactive Tutorial, Quiz, and Progress
        self.tutorial_button = tk.Button(self, text="Interactive Tutorial", command=self.start_tutorial, width=30)
        self.tutorial_button.pack(pady=10)

        self.quiz_button = tk.Button(self, text="Take Quiz", command=self.start_quiz, width=30)
        self.quiz_button.pack(pady=10)

        # Progress bar
        tk.Label(self, text="Your Progress:", font=("Arial", 12)).pack(pady=10)
        self.progress = ttk.Progressbar(self, length=300, mode='determinate')
        self.progress.pack(pady=5)
        self.update_progress_bar()

        # Log Out or Back to Course Selection button
        self.back_button = tk.Button(self, text="Back to Course Selection", command=self.back_to_courses, width=30)
        self.back_button.pack(pady=20)

    def start_tutorial(self):
        """
        Launch the Tutorial UI for the selected course.
        """
        tutorial_file = TUTORIAL_FILE_PATHS.get(self.course_name)
        if os.path.exists(tutorial_file):
            self.destroy()  # Close dashboard
            app = TutorialUI(tutorial_file)
            app.mainloop()
        else:
            messagebox.showerror("Error", "Tutorial file not found.")

    def start_quiz(self):
        """
        Launch the Quiz UI for the selected course.
        """
        quiz_file = QUIZ_FILE_PATHS.get(self.course_name)
        if os.path.exists(quiz_file):
            self.destroy()  # Close dashboard
            app = QuizUI(quiz_file, is_interactive=False)  # Change is_interactive based on mode
            app.mainloop()
        else:
            messagebox.showerror("Error", "Quiz file not found.")

    def update_progress_bar(self):
        """
        Update the progress bar based on user progress.
        """
        # Progress tracking should be passed in as a percentage (0 to 100).
        course_progress = self.progress_tracker.get(self.course_name, 0)
        self.progress['value'] = course_progress

    def back_to_courses(self):
        """
        Returns the user to the course selection screen.
        """
        self.destroy()  # Close the dashboard
        # Logic to go back to the course selection screen should be here.


# Simulating a progress tracker (this should be fetched from persistent storage in reality)
progress_tracker = {
    "Python": 50,  # e.g., 50% completed in Python
    "Information Security": 75,
    "AI": 30
}

# Example usage:
if __name__ == "__main__":
    app = CourseDashboard("AI", progress_tracker)
    app.mainloop()
