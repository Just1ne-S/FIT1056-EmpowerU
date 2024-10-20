import tkinter as tk
from interfaces.progress_bar import ProgressBar

class PythonHP(tk.Frame):
    def __init__(self,master):
        super().__init__(master=master)
        self.master = master
        self.title = tk.Label(self,text="Learn Python: Your Coding Journey Begins Here",font=("Arial Bold",16))
        self.title.grid(row=0,padx=10,pady=10)
        self.progress = ProgressBar(self)
        self.button = tk.Button(self,text="Increase Progress",command=self.progress.increase_bar)
        self.button.grid(row=2,padx=10,pady=10,sticky=tk.NSEW)
    
    def show_homepage(self):
        self.place(relx=.5,rely=.1,anchor=tk.CENTER)

if __name__ == "__main__":
    pass