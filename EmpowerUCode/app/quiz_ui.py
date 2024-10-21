import sys
import tkinter as tk
from tkinter import ttk, messagebox

from app.quiz_controller import QuizController
from interfaces.back_button import BackButton

class QuizUI(tk.Frame):
    def __init__(self,master,master_previous,back_button_text,quiz_file_path, is_interactive=True):
        super().__init__(master=master)
        self.master_previous = master_previous

        # Initialize the QuizController with the is_interactive flag
        self.quiz_controller = QuizController(quiz_file_path, is_interactive=is_interactive)

        self.back_button_quiz = BackButton(master=self.master,master_previous=self,text_input=back_button_text)
        self.back_button_quiz.back_button.config(command=self.back_to_homepage)

        # Create the frame for the quiz
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(pady=20)

        # Label to display the instructions
        self.instructions_label = tk.Label(self.content_frame, text="", wraplength=700, justify="left", font=("Arial", 10, "italic"))
        self.instructions_label.pack(pady=5)


        # Label to display the question
        self.question_label = tk.Label(self.content_frame, text="", wraplength=700, justify="left", font=("Arial", 12))
        self.question_label.pack(pady=10)

        # Frame for MCQ options (will change depending on question type)
        self.mcq_frame = tk.Frame(self.content_frame)
        self.mcq_frame.pack()

        # Text area for coding task
        self.coding_textarea = tk.Text(self.content_frame, height=10, width=60)

        # Listbox for drag-and-drop task
        self.drag_and_drop_listbox = tk.Listbox(self.content_frame, selectmode=tk.SINGLE)
        self.drag_and_drop_listbox.bind("<Button-1>", self.on_drag_start)
        self.drag_and_drop_listbox.bind("<ButtonRelease-1>", self.on_drag_stop)

        # Label for hints
        self.hint_label = tk.Label(self.content_frame, text="", wraplength=700, justify="left", font=("Arial", 10), fg="black")
        self.hint_label.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(self, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(pady=20)

        # Load the first question
        self.load_question()

    def load_question(self):
        """
        Loads the current question and updates the UI based on the question type.
        """
        current_question = self.quiz_controller.get_current_question()
        if current_question is None:
            self.finish_quiz()
            return

        # Set instructions if available
        instructions = current_question.get("Instructions", "Please answer the question.")
        self.instructions_label.config(text=instructions)

        self.question_label.config(text=current_question["Q"])
        self.hint_label.config(text="")  # Clear previous hint

        # Clear previous widgets
        for widget in self.mcq_frame.winfo_children():
            widget.destroy()
        self.coding_textarea.pack_forget()
        self.drag_and_drop_listbox.pack_forget()

        # Display question based on the type
        question_type = current_question['Type']

        if question_type == 'mcq':
            self.display_mcq(current_question)
        elif question_type == 'coding_task':
            self.display_coding_task(current_question)
        elif question_type == 'drag_and_drop':
            self.display_drag_and_drop(current_question)

    def display_mcq(self, question_data):
        """
        Displays the MCQ options as radio buttons.
        """
        self.selected_answer = tk.StringVar()

        for option in question_data['Options']:
            tk.Radiobutton(self.mcq_frame, text=option, variable=self.selected_answer, value=option).pack(anchor='w')

    def display_coding_task(self, question_data):
        """
        Displays a text area for coding tasks.
        """
        self.coding_textarea.pack()
        self.coding_textarea.delete("1.0", tk.END)
        self.coding_textarea.insert(tk.END, question_data.get("Instructions", ""))

    def display_drag_and_drop(self, question_data):
        """
        Displays a listbox for drag-and-drop tasks, allowing reordering.
        """
        self.drag_and_drop_listbox.pack(pady=10)
        self.drag_and_drop_listbox.delete(0, tk.END)

        # Set a fixed size for the ListBox with explicit colors
        self.drag_and_drop_listbox.config(height=len(question_data['Options']), width=40, bg="white", fg="black")

        # Insert options into the listbox
        for option in question_data['Options']:
            self.drag_and_drop_listbox.insert(tk.END, option)

    def on_drag_start(self, event):
        """
        Capture the index of the item being clicked (drag start).
        """
        self.drag_start_index = self.drag_and_drop_listbox.nearest(event.y)

    def on_drag_stop(self, event):
        """
        Reinsert the item at the new position (drag stop).
        """
        drag_end_index = self.drag_and_drop_listbox.nearest(event.y)

        if self.drag_start_index != drag_end_index:
            item_text = self.drag_and_drop_listbox.get(self.drag_start_index)
            self.drag_and_drop_listbox.delete(self.drag_start_index)
            self.drag_and_drop_listbox.insert(drag_end_index, item_text)

    def submit_answer(self):
        """
        Submits the user's answer based on the question type and provides progressive hints if necessary.
        """
        current_question = self.quiz_controller.get_current_question()
        question_type = current_question['Type']

        # Fetch user's answer based on the question type
        if question_type == 'mcq':
            # Extract the first character (the letter) before the closing parenthesis ')'
            user_answer = self.selected_answer.get().strip().split(")")[0].strip()
        elif question_type == 'coding_task':
            user_answer = self.coding_textarea.get("1.0", tk.END).strip()
        elif question_type == 'drag_and_drop':
            user_answer = ', '.join([self.drag_and_drop_listbox.get(i).split(")")[0].strip() for i in range(self.drag_and_drop_listbox.size())])

        # Validate the answer
        correct, hint = self.quiz_controller.validate_answer(user_answer, question_type)

        # # Debugging print statements
        # print(f"Debug: Answer submitted - {user_answer}")
        # print(f"Debug: Hint - {hint}")
        # print(f"Debug: is_interactive = {self.quiz_controller.is_interactive}")

        # Provide feedback to the user
        if correct:
            messagebox.showinfo("Correct", "Correct!")
            self.quiz_controller.increment_score()
            self.quiz_controller.next_question()
            self.load_question()  # Load the next question
        else:
            messagebox.showerror("Incorrect", "Incorrect!")
            # Display the next progressive hint if in interactive mode
            if self.quiz_controller.is_interactive and hint:
                self.hint_label.config(text=f"Hint: {hint}")
            else:
                self.hint_label.config(text="No hints available in test mode.")

    def back_button(self,rel_x,rel_y=.95):
        self.back_button_quiz.place(relx=rel_x,rely=rel_y,anchor=tk.CENTER)

    def hide_button_homepage(self):
        self.back_button_quiz.forget_button()

    def back_to_homepage(self):
        self.place_forget()
        self.hide_button_homepage()
        self.master_previous.show_homepage()

    def place_frame(self):
        self.place(relx=.5,rely=.5,anchor=tk.CENTER)

    def forget_frame(self):
        self.place_forget()

    def finish_quiz(self):
        """
        Finish the quiz and show the final score.
        """
        final_score, total_questions = self.quiz_controller.get_final_score()
        messagebox.showinfo("Quiz Completed", f"Your final score: {final_score}/{total_questions}")
        self.quiz_controller.reset_quiz()
        self.hide_button_homepage()
        self.forget_frame()
        self.master_previous.show_homepage()




# Running the GUI-based quiz
if __name__ == "__main__":
    pass
