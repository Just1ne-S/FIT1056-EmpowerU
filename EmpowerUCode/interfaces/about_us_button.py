import tkinter as tk

class AboutUsButton(tk.Frame):
    def __init__(self,master):
        super().__init__(master=master)
        self.path = "./images/AboutUs.png"

        self.button_var = tk.PhotoImage(file=self.path)
        self.button = tk.Button(master=self,image=self.button_var,width=65,height=55)
        self.button.pack()

    def show_button(self):
        self.place(relx=.95,rely=.93,anchor=tk.CENTER)
    
    def hide_button(self):
        self.place_forget()