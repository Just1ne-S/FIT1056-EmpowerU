import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
sys.path.append("/Users/krishnaagarwal/Desktop/FIT1056-EmpowerU/EmpowerUCode/app")
from file_handler import parse_tutorial_file  # Assuming this is the parser function

class TutorialUI(tk.Tk):
    def __init__(self, tutorial_file_path):
        super().__init__()

        # Set window title and size
        self.title("Tutorial Application")
        self.geometry("800x600")

        # Parse the tutorial file
        self.tutorial_data = parse_tutorial_file(tutorial_file_path)
        self.current_section_index = 0

        # Create a frame to hold content
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Title Label
        self.title_label = tk.Label(self.content_frame, text="", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Section Title Label
        self.section_title_label = tk.Label(self.content_frame, text="", font=("Arial", 14))
        self.section_title_label.pack(pady=10)

        # Section Content Label (text wrapping)
        self.content_label = tk.Label(self.content_frame, text="", wraplength=700, justify="left", font=("Arial", 12))
        self.content_label.pack(pady=10)

        # Navigation Buttons
        self.prev_button = tk.Button(self, text="Previous", command=self.prev_section, state="disabled")
        self.prev_button.pack(side="left", padx=20, pady=20)

        self.next_button = tk.Button(self, text="Next", command=self.next_section)
        self.next_button.pack(side="right", padx=20, pady=20)

        # Load the first section
        self.load_section()

    def load_section(self):
        """
        Loads the current section content into the UI.
        """
        tutorial = self.tutorial_data[0]  # Assuming a single tutorial file
        section = tutorial["sections"][self.current_section_index]

        # Update UI with title, section title, and content
        self.title_label.config(text=tutorial["title"])
        self.section_title_label.config(text=section["section_title"])
        self.content_label.config(text=section["content"])

        # Disable/Enable buttons based on section index
        if self.current_section_index == 0:
            self.prev_button.config(state="disabled")
        else:
            self.prev_button.config(state="normal")

        if self.current_section_index == len(tutorial["sections"]) - 1:
            self.next_button.config(text="Finish", command=self.finish_tutorial)
        else:
            self.next_button.config(text="Next", command=self.next_section)

    def next_section(self):
        """
        Go to the next section.
        """
        if self.current_section_index < len(self.tutorial_data[0]["sections"]) - 1:
            self.current_section_index += 1
            self.load_section()

    def prev_section(self):
        """
        Go to the previous section.
        """
        if self.current_section_index > 0:
            self.current_section_index -= 1
            self.load_section()

    def finish_tutorial(self):
        """
        Finish the tutorial and display a completion message.
        """
        messagebox.showinfo("Tutorial Completed", "You have finished the tutorial!")
        self.destroy()

    def update_progress(self, increment):
        """
        Increment the progress in the progress tracker and update the bar.
        """
        new_progress = min(self.progress_tracker.get(self.course_name, 0) + increment, 100)
        self.progress_tracker[self.course_name] = new_progress
        messagebox.showinfo("Progress", f"Progress for {self.course_name} is now {new_progress}%")


# Running the Tutorial UI
if __name__ == "__main__":
    tutorial_file_path = "/Users/krishnaagarwal/Documents/FIT1056-EmpowerU/EmpowerU/data/tutorials/ai_tutorial.txt"  # Replace with the actual file path
    app = TutorialUI(tutorial_file_path)
    app.mainloop()
