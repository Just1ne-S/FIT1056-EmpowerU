import tkinter as tk

class DisplayLabel(tk.Frame):
    def __init__(self,master,text_input,directory,role,rel_x,rel_y,font):
        super().__init__(master=master)
        self.master = master
        self.text_input = text_input
        self.directory = directory
        self.role = role
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.font = font
        if self.role == "Image":
            self.label_var = tk.PhotoImage(file=self.directory)
            self.label = tk.Label(master=self,image=self.label_var)
            self.label.pack()
        elif self.role == "Text":
            self.label = tk.Label(master=self,text=self.text_input,font=self.font)
            self.label.pack()
            

    def show_label(self):
        self.place(relx=self.rel_x,rely=self.rel_y,anchor=tk.CENTER)

    def forget_label(self):
        self.place_forget()
