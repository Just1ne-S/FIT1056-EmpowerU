import tkinter as tk 
import os 

class SignUpPage(tk.Frame):
    def __init__(self, master, path="./data/user_login_info.txt"):
        super().__init__(master=master)
        self.master = master 
        self.path = path 
        self.constant = 3

        # sign up title 
        self.signup_label = tk.Label(master=self, text="Sign Up", font=("Arial Bold", 20))
        self.signup_label.grid(row=1, columnspan=2, padx=10, pady=10)

        # first name input 
        self.firstname_label = tk.Label(master=self, text="First Name:")
        self.firstname_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.firstname_var = tk.StringVar(master=self)
        self.firstname_entry = tk.Entry(master=self, textvariable=self.firstname_var)
        self.firstname_entry.grid(row=2, column=1, padx=10, pady=1, sticky=tk.W)

        # last name input 
        self.lastname_label = tk.Label(master=self, text="Last Name:")
        self.lastname_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        self.lastname_var = tk.StringVar(master=self)
        self.lastname_entry = tk.Entry(master=self, textvariable=self.lastname_var)
        self.lastname_entry.grid(row=3, column=1, padx=10, pady=1, sticky=tk.W)

        # phone number input 
        self.phonenumber_label = tk.Label(master=self, text="Phone Number:")
        self.phonenumber_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.E)

        self.phonenumber_var = tk.StringVar(master=self)
        self.phonenumber_entry = tk.Entry(master=self, textvariable=self.phonenumber_var)
        self.phonenumber_entry.grid(row=4, column=1, padx=10, pady=1, sticky=tk.W)

        # username label widget 
        self.username_label = tk.Label(master=self, text="Username:")
        self.username_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.E)

        self.username_var = tk.StringVar(master=self)
        self.username_entry = tk.Entry(master=self, textvariable=self.username_var)
        self.username_entry.grid(row=5, column=1, padx=10, pady=1, sticky=tk.W)

        # Password label widget
        self.password_label = tk.Label(master=self, text="Enter a password:")
        self.password_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.E)

        # Password variable and entry widget
        self.password_var = tk.StringVar(master=self)
        self.password_entry = tk.Entry(master=self, textvariable=self.password_var, show="●")
        self.password_entry.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

        # Password label widget
        self.confirm_password_label = tk.Label(master=self, text="Confirm Password:")
        self.confirm_password_label.grid(row=7, column=0, padx=10, pady=10, sticky=tk.E)

        # Confirm Password variable and entry widget
        self.confirm_password_var = tk.StringVar(master=self)
        self.confirm_password_entry = tk.Entry(master=self, textvariable=self.confirm_password_var, show="●")
        self.confirm_password_entry.grid(row=7, column=1, padx=10, pady=10, sticky=tk.W)

        # Activation code label
        self.activate_label = tk.Label(master=self,text="Activation Code:")
        self.activate_label.grid(row=8,column=0,padx=10,pady=10,sticky=tk.E)

        # Activation code entry
        self.activate_var = tk.StringVar(master=self)
        self.activate_entry = tk.Entry(master=self,textvariable=self.activate_var)
        self.activate_entry.grid(row=8,column=1,padx=10,pady=10,sticky=tk.W)

        # Alert variable and label widget - displays alert messages where necessary
        self.alert_var = tk.StringVar(master=self)
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var,fg="red")
        self.alert_label.grid(row=9, columnspan=2, padx=10, pady=10)

        # Button to sign up
        self.signup_button = tk.Button(master=self, text="Sign Up", command=self.sign_up)
        self.signup_button.grid(row=10, columnspan=2, padx=10, pady=10)

        #Button to go home 
        self.home_button = tk.Button(master=self, text="Back to Sign In", command=self.master.show_homepage)
        self.home_button.grid(row=11, columnspan=2, padx=10, pady=10)

    def sign_up(self):
        firstname = self.firstname_var.get()
        lastname = self.lastname_var.get()
        phonenumber = self.phonenumber_var.get()
        username = self.username_var.get()
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if not firstname or not lastname or not phonenumber or not username or not password or not confirm_password:
            self.alert_var.set("Error! All fields must be filled in.")
        elif password != confirm_password:
            self.alert_var.set("Passwords do not match.")
        elif self.username_taken(username):
            self.alert_var.set("That username is taken.")
        elif len(phonenumber) != 10:
            self.alert_var.set("Invalid Phone number.")
        else:
            self.new_user(firstname, lastname, phonenumber, username, password)
            self.alert_label.config(fg="green")
            self.timer()
        
    def username_taken(self, username):

        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                for line in file:
                    entered_usernames = line.split(",")[4]
                    if entered_usernames == username:
                        return True
        return False 
    
    def clear_entry(self):
        self.firstname_entry.delete(0,tk.END)
        self.lastname_entry.delete(0,tk.END)
        self.phonenumber_entry.delete(0,tk.END)
        self.username_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)
        self.confirm_password_entry.delete(0,tk.END)
        self.alert_var.set("")
        self.alert_label.config(fg="red")

    def timer(self):
        self.alert_var.set(f"Successful Login! Returning to Sign In page in {self.constant}.")
        self.constant -= 1
        if self.constant > -1:
            self.after(1000,self.timer)
        else:
            self.constant = 3
            self.clear_entry()
            self.master.show_homepage()
        
    def new_user(self, firstname, lastname, phonenumber, username, password):
        with open(self.path,"r+") as file:
            lines = file.readlines()
            user_id = int(lines[-1][0]) + 1
            file.write(f"\n{user_id},{firstname},{lastname},{phonenumber},{username},{password}")
