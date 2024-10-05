import tkinter as tk
from tkinter import ttk

class ProgressBar(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.progress_value = tk.DoubleVar(value=0)  # Start from 0 for demonstration
        self.progress_bar = ttk.Progressbar(self.master, variable=self.progress_value, length=850, maximum=100)
        self.progress_bar.grid(row=1, padx=10, pady=10)

    def increase_bar(self):
        if self.progress_value.get() < 100:
            self.progress_value.set(self.progress_value.get() + 1)
        else:
            pass
        
if __name__ == "__main__":
    pass
