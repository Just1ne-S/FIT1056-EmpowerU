import tkinter as tk

from interfaces.homepage import HomePage

class MW(tk.Tk):
    
    def __init__(self, title, width, height):   
        super().__init__()
        super().title(title)
        super().geometry(f"{width}x{height}")

        self.homepage = HomePage(master=self, image_path="./images/EmpowerU logo.png")
        self.show_homepage()

    def show_homepage(self):
        self.homepage.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_homepage(self):
        self.homepage.place_forget()

if __name__ == "__main__":
    pass
