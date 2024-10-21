import tkinter as tk

from interfaces.homepage import HomePage
from interfaces.sign_up_page import SignUpPage
from interfaces.About_Us.about_us_button import AboutUsButton

class MW(tk.Tk):
    
    def __init__(self, title, width, height):   
        super().__init__()
        super().title(title)
        super().geometry(f"{width}x{height}")
        super().iconphoto(True,tk.PhotoImage(file="./images/EmpowerU Icon.png"))

        self.about_us_button = AboutUsButton(master=self)
        self.homepage = HomePage(master=self, image_path="./images/EmpowerU Logo.png",about_us_button=self.about_us_button)
        self.sign_up_page = SignUpPage(master=self)
        self.show_homepage()

    def show_homepage(self):
        self.sign_up_page.place_forget()
        self.homepage.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.about_us_button.show_button()

    def hide_homepage(self):
        self.about_us_button.hide_button()
        self.homepage.place_forget()

    def show_sign_up_page(self):
        self.homepage.place_forget()
        self.sign_up_page.place(relx=.5, rely=.5, anchor=tk.CENTER)

if __name__ == "__main__":
    pass
