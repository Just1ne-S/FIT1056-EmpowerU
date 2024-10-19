import tkinter as tk

class Recovery(tk.Frame):
    def __init__(self,master):
        super().__init__(master=master)
        self.master = master
        self.constant = 3
        self.assign = None

        # Recover Account  title 
        self.recover_label = tk.Label(master=self, text="Recover Account", font=("Arial Bold", 20))
        self.recover_label.grid(row=0, columnspan=2, padx=10, pady=10)

        # first name input 
        self.firstname_label = tk.Label(master=self, text="First Name:")
        self.firstname_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.firstname_var = tk.StringVar(master=self)
        self.firstname_entry = tk.Entry(master=self, textvariable=self.firstname_var)
        self.firstname_entry.grid(row=1, column=1, padx=10, pady=1, sticky=tk.W)

        # last name input 
        self.lastname_label = tk.Label(master=self, text="Last Name:")
        self.lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.lastname_var = tk.StringVar(master=self)
        self.lastname_entry = tk.Entry(master=self, textvariable=self.lastname_var)
        self.lastname_entry.grid(row=2, column=1, padx=10, pady=1, sticky=tk.W)

        # username label widget 
        self.username_label = tk.Label(master=self, text="Username:")
        self.username_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        self.username_var = tk.StringVar(master=self)
        self.username_entry = tk.Entry(master=self, textvariable=self.username_var)
        self.username_entry.grid(row=3, column=1, padx=10, pady=1, sticky=tk.W)

        # Activation code label
        self.activate_label = tk.Label(master=self,text="Activation Code:")
        self.activate_label.grid(row=4,column=0,padx=10,pady=10,sticky=tk.E)

        # Activation code entry
        self.activate_var = tk.StringVar(master=self)
        self.activate_entry = tk.Entry(master=self,textvariable=self.activate_var)
        self.activate_entry.grid(row=4,column=1,padx=10,pady=10,sticky=tk.W)

        # Label for new password
        self.new_pass_label = tk.Label(master=self,text="New Password:")
        self.new_pass_label.grid(row=5,column=0,padx=10,pady=10,sticky=tk.E)

        # Entry for new password
        self.new_pass_var = tk.StringVar(master=self)
        self.new_pass_entry = tk.Entry(master=self,textvariable=self.new_pass_var,show="●")
        self.new_pass_entry.grid(row=5,column=1,padx=10,pady=10,sticky=tk.W)

        # Label to confirm password
        self.confirm_pass_label = tk.Label(master=self,text="Confirm New Password:")
        self.confirm_pass_label.grid(row=6,column=0,padx=10,pady=10,sticky=tk.E)

        # Entry to confirm password
        self.confirm_pass_var = tk.StringVar(master=self)
        self.confirm_pass_entry = tk.Entry(master=self,textvariable=self.confirm_pass_var,show="●")
        self.confirm_pass_entry.grid(row=6,column=1,padx=10,pady=10,sticky=tk.W)

        # Alert variable and label widget - displays alert messages where necessary
        self.alert_var = tk.StringVar(master=self)
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var,fg="red")
        self.alert_label.grid(row=7, columnspan=2, padx=10, pady=10)

        # Button to recover account
        self.recover_button = tk.Button(master=self,text="Recover Account",command=self.recover_account)
        self.recover_button.grid(row=8,columnspan=2,padx=10,pady=10)

        # Button to go home 
        self.home_button = tk.Button(master=self, text="Back to Sign In", command=self.forget_recover)
        self.home_button.grid(row=9, columnspan=2, padx=10, pady=10)


    def recover_account(self):
        firstname = self.firstname_var.get()
        lastname = self.lastname_var.get()
        username = self.username_var.get()
        new_pass = self.new_pass_var.get()
        confirm_pass = self.confirm_pass_var.get()
        code = self.activate_var.get()
        lines = self.assign_role(firstname,lastname,username,new_pass,code)

        if not firstname or not lastname or not username or not confirm_pass or not new_pass or not code:
            self.alert_var.set("Error! All fields must be filled in.")
        elif firstname.isalpha() == False:
            self.alert_var.set("First name must be all letters.")
        elif lastname.isalpha() == False:
            self.alert_var.set("Last name must be all letters.")
        elif new_pass != confirm_pass:
            self.alert_var.set("Passwords do not match.")
        elif self.assign == None:
            self.alert_var.set("Information is Incorrect.")
        else:
            self.recover_button.config(state="disabled")    
            self.replace_info(lines,self.assign)
            self.alert_label.config(fg="green")
            self.timer()

    def assign_role(self,firstname,lastname,username_input,new_pass,code):
        login_info_user = open("./data/user_login_info.txt","r")
        login_info_receptionist = open("./data/receptionist_login_info.txt","r")
        lines_user = login_info_user.readlines()
        lines_receptionist = login_info_receptionist.readlines()
        for index,line in enumerate(lines_user):
            user_id,first_name,last_name,contact_num,username,password,activation_code = line.strip().split(",")
            if firstname == first_name and lastname == last_name and username_input == username and activation_code == code:
                self.assign = "User"
                lines_user[index] = f"{user_id},{first_name},{last_name},{contact_num},{username},{new_pass},{code}\n"
                return lines_user
        for index,line in enumerate(lines_receptionist):
            user_id,first_name,last_name,contact_num,username,password,activation_code = line.strip().split(",")
            if firstname == first_name and lastname == last_name and username_input == username and activation_code == code:
                self.assign = "Receptionist"
                lines_user[index] = f"{user_id},{first_name},{last_name},{contact_num},{username},{new_pass},{code}\n"
                return lines_receptionist
            
        
    def replace_info(self,lines,role):
        if role == "User":
            login_info_user_write = open("./data/user_login_info.txt","w")
            for line in lines:
                login_info_user_write.write(line)
        elif role == "Receptionist":
            login_info_recep_write = open("./data/user_login_info.txt","w")
            for line in lines:
                login_info_recep_write.write(line)
        
    def clear_entry(self):
        self.firstname_entry.delete(0,tk.END)
        self.lastname_entry.delete(0,tk.END)
        self.username_entry.delete(0,tk.END)
        self.new_pass_entry.delete(0,tk.END)
        self.confirm_pass_entry.delete(0,tk.END)
        self.activate_entry.delete(0,tk.END)
        self.alert_var.set("")
        self.alert_label.config(fg="red")


    def timer(self):
        self.alert_var.set(f"Account Recovered Successfully! Returning to Sign In page in {self.constant}.")
        self.constant -= 1
        if self.constant > -1:
            self.after(1000,self.timer)
        else:
            self.recover_button.config(state="normal")  
            self.constant = 3
            self.clear_entry()
            self.forget_recover()
            self.recover_button.config(command=self.recover_account)
            self.master.show_homepage()

    def show_recover(self):
        self.place(relx=.5,rely=.5,anchor=tk.CENTER)

    def forget_recover(self):
        self.place_forget()
        self.master.show_homepage()