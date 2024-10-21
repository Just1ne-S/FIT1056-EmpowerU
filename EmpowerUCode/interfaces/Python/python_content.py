import tkinter as tk
from interfaces.back_button import BackButton

class PythonContent(tk.Frame):
    def __init__(self, master, master_previous, topic_index):
        super().__init__(master=master)
        self.master = master
        self.master_previous = master_previous
        self.topic_index = topic_index + 1
        
        with open(f"./data/Python/python_topic_{self.topic_index}.txt", "r") as rf:
            rf = rf.readlines()
        
        for i in range(len(rf)):
            if rf[i].startswith("##"):
                self.label = tk.Label(master=self, text=rf[i][2:].strip("\n"), font=("Arial Bold", 12))
                self.label.grid(row=i, column=0, padx=10, pady=1, sticky=tk.NW)
            elif rf[i].startswith("#"):
                self.label = tk.Label(master=self, text=rf[i][1:].strip("\n"), font=("Arial Bold", 14))
                self.label.grid(row=i, column=0, padx=10, pady=1, sticky=tk.NW) 
            else:
                self.label = tk.Label(master=self, text=rf[i].strip("\n"), font=("Arial", 11))
                self.label.grid(row=i, column=0, padx=10, pady=1, sticky=tk.NW)  
        
        self.backbutton = BackButton(self.master, self, "Back to Python HomePage")
        self.backbutton.back_button.config(command=self.hide_content)
        
    def show_content(self):
        self.place(relx=0, rely=.01, anchor=tk.NW)
        self.backbutton.place(relx=.08,rely=.95,anchor=tk.CENTER)

    def hide_content(self):
        self.place_forget()
        self.master_previous.show_homepage()
        self.backbutton.forget_button()
