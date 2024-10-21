import tkinter as tk

class BackButton(tk.Frame):
    def __init__(self,master,master_previous,text_input):
        super().__init__(master=master)
        self.master = master
        self.master_previous = master_previous

        self.back_button = tk.Button(master=self,text=text_input)
        self.back_button.pack()
        
    def forget_button(self):
        self.place_forget()

