import tkinter as tk

from app.Receptionist import Receptionist
from app.User import User
from interfaces.subject_selection import Selection
from interfaces.recover_account import Recovery
from interfaces.about_us import about_us 


class HomePage(tk.Frame):

    def __init__(self,master,image_path):
        super().__init__(master=master)
        self.master = master
        self.image_path = image_path
        self.path_1 = "./data/receptionist_login_info.txt"
        self.path_2 = "./data/user_login_info.txt"

        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self, image=self.logo_photoimage, width=400, height=270)
        self.logo_label.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        self.login_title = tk.Label(master=self,text="Welcome to EmpowerU",font=("Arial Bold", 20))
        self.login_title.grid(row=1, columnspan=2, padx=10, pady=10)

         # Username label widget
        self.username_label = tk.Label(master=self, text="Username:")
        self.username_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        # Username variable and entry widget
        self.username_var = tk.StringVar(master=self)
        self.username_entry = tk.Entry(master=self, textvariable=self.username_var)
        self.username_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # Password label widget
        self.password_label = tk.Label(master=self, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        # Password variable and entry widget
        self.password_var = tk.StringVar(master=self)
        self.password_entry = tk.Entry(master=self, textvariable=self.password_var, show="●")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Alert variable and label widget - displays alert messages where necessary
        self.alert_var = tk.StringVar(master=self)
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var,fg="red")
        self.alert_label.grid(row=4, columnspan=2, padx=10, pady=10)

        # Button to login
        self.login_button = tk.Button(master=self, text="Login", command=self.login)
        self.login_button.grid(row=5, columnspan=2, padx=10, pady=10)

        # Button for sign up 
        self.signup_button = tk.Button(master=self, text="Sign Up", command=self.master.show_sign_up_page)
        self.signup_button.grid(row=6, columnspan=2, padx=10, pady=10)

        # Button to recover account
        self.recover_button = tk.Button(master=self,text="Recover Account",command=self.recover_account)
        self.recover_button.grid(row=7,columnspan=2,padx=10,pady=10)

        # Button to shut down
        self.shutdown_button = tk.Button(master=self, text="Shut down", command=master.destroy)
        self.shutdown_button.grid(row=8, columnspan=2, padx=10, pady=10)

        # Button to display about us 
        self.about_us_button = tk.Button(master=self, text="About Us", command=self.show_about_us_info)
        self.about_us_button.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NW)

        # Label to display the About Us
        self.about_us_label = tk.Label(master=self, text="", justify="left", wraplength=500)
        self.about_us_label.grid(row=9, columnspan=2, padx=10, pady=10)
        self.about_us_label.grid_remove()

        # Close button to hide About Us (initially hidden)
        self.close_button = tk.Button(master=self, text="Close", command=self.hide_about_us)
        self.close_button.grid(row=10, columnspan=2, padx=10, pady=10)
        self.close_button.grid_remove()

    def show_about_us_info(self):
        self.hide_login_display()
        about_us(self.about_us_label, self.close_button)

    def hide_about_us(self):
        self.about_us_label.grid_remove()
        self.close_button.grid_remove()
        self.show_login_display()

    def hide_login_display(self):
        self.username_label.grid_remove()
        self.username_entry.grid_remove()
        self.password_label.grid_remove()
        self.password_entry.grid_remove()
        self.login_button.grid_remove()
        self.signup_button.grid_remove()
        self.recover_button.grid_remove()
        self.alert_label.grid_remove()

    def show_login_display(self):
        self.username_label.grid()
        self.username_entry.grid()
        self.password_label.grid()
        self.password_entry.grid()
        self.login_button.grid()
        self.signup_button.grid()
        self.recover_button.grid()
        self.alert_label.grid()

    def login(self):
        receptionist_login = Receptionist.authenticate(self.username_var.get(), self.password_var.get(),self.path_1)
        user_login = User.authenticate(self.username_var.get(), self.password_var.get(),self.path_2)
        if isinstance(receptionist_login,Receptionist):
            self.master.hide_homepage()
        elif isinstance(user_login,User):   
            self.master.hide_homepage()
            self.selection = Selection(master=self.master,\
                                       image_path_1="./images/Python Logo.png",\
                                       image_path_2="./images/Information Security logo.png",\
                                       image_path_3="./images/AI Logo.png",\
                                       user=user_login)
            self.selection.selection_show()
        else:
            self.alert_var.set("Login unsucessful.")

        self.username_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)
    
    def recover_account(self):
        self.master.hide_homepage()
        recovery = Recovery(self.master)
        recovery.show_recover()

        
if __name__ == "__main__":
    pass
