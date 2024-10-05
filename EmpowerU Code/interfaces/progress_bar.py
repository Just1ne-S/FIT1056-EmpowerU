import tkinter as tk
from tkinter import ttk

class ProgressBar(tk.Frame):
    def __init__(self):
        super().__init__()
        self.progress_value = tk.DoubleVar(master=self)
        self.progress_bar = ttk.Progressbar(self,variable=self.progress_value)
    
    def increase_bar(self):
        if self.progress_value.get() < 100:
            self.progress_value.set(self.progress_value.get() + 1)
            self.progress_bar.set(self.progress_value)
        else:
            pass

if __name__ == "__main__":
    pass
            
