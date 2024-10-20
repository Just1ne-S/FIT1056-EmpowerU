import tkinter as tk
from tkinter import ttk

class ProgressBar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Variable to track progress
        self.progress_value = tk.DoubleVar(value=0)  # Start from 0 for demonstration

        # Create a progress bar widget
        self.progress_bar = ttk.Progressbar(self.master, variable=self.progress_value, length=850, maximum=100)
        self.progress_bar.grid(row=1, padx=10, pady=10)

    def set_progress(self, value):
        """
        Set the progress bar to a specific value.
        :param value: A float between 0 and 100 representing the progress percentage.
        """
        if 0 <= value <= 100:
            self.progress_value.set(value)
        else:
            raise ValueError("Progress value must be between 0 and 100.")

    def increase_progress(self, increment=1):
        """
        Increase the progress bar by a specific value.
        :param increment: How much to increase the progress bar. Default is 1%.
        """
        new_value = self.progress_value.get() + increment
        if new_value <= 100:
            self.progress_value.set(new_value)
        else:
            self.progress_value.set(100)  # Cap at 100

    def reset_progress(self):
        """
        Reset the progress bar to 0%.
        """
        self.progress_value.set(0)

if __name__ == "__main__":
    pass
