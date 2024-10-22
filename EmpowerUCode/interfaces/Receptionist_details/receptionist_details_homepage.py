import tkinter as tk
from tkinter import ttk
from interfaces.back_button import BackButton

class ReceptionistDetailsHP(tk.Frame):
    def __init__(self, receptionist, master, master_previous):
        super().__init__(master=master)
        self.receptionist = receptionist
        self.master = master
        self.master_previous = master_previous

        self.title = tk.Label(self,text="Receptionist Details",font=("Arial Bold",30,"underline"))
        self.title.grid(columnspan = 3, row = 0, padx = 20, pady = 500, sticky="n")

        self.details_table()

        self.view_credentials_label = tk.Label(self, text="Click here to view password and activation code",
                                               cursor = "hand1",font=("Arial Bold",10))
        self.view_credentials_label.grid(row=10, column=0, pady=10, padx=500, sticky="n")
        self.view_credentials_label.bind("<Button-1>", self.view_credentials)

        self.backbutton = BackButton(self.master,self,"Back to Selection Page")
        self.backbutton.back_button.config(command=self.back_selection)
    
    def details_table(self):
        columns = ("Fields", "Details")

        self.tree = ttk.Treeview(self.master, columns=columns, show="headings", height=14)

        self.tree.heading("Fields", text="Fields", anchor="e")
        self.tree.heading("Details", text="Details", anchor="w")

        self.tree.column("Fields", width=200, anchor="e")
        self.tree.column("Details", width=150, anchor="w")

        self.tree.insert("", "end", values=("user_id: ", self.receptionist.user_id))
        self.tree.insert("", "end")
        self.tree.insert("", "end", values=("First Name: ", self.receptionist.first_name))
        self.tree.insert("", "end")
        self.tree.insert("", "end", values=("Last Name: ", self.receptionist.last_name))
        self.tree.insert("", "end")
        self.tree.insert("", "end", values=("Contact No.: ", self.receptionist.contact_num))
        self.tree.insert("", "end")
        self.tree.insert("", "end", values=("Username: ", self.receptionist.username))
        self.tree.insert("", "end")
        self.tree.insert("", "end", values=("Password: ", "******"))
        self.tree.insert("", "end")
        self.tree.insert("", "end", values=("Activation Code: ", "****"))

        self.apply_header_style()


        self.tree.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        

    def apply_header_style(self):
        style = ttk.Style()
        style.configure("Treeview.Heading",
                        font=("Arial", 16, "bold")) 
        

    def view_credentials(self, event): 
        self.tree.item(self.tree.get_children()[10], values=("Password: ", self.receptionist.password))
        self.tree.item(self.tree.get_children()[12], values=("Activation Code: ", self.receptionist.code))
        self.view_credentials_label.config(text="Credentials revealed")
    
    def show_homepage(self):
        self.place(relx=.5,rely=.1,anchor=tk.CENTER)
        self.backbutton.place(relx=.08,rely=.95,anchor=tk.CENTER)
    
    def forget_homepage(self):
        self.place_forget()
        self.backbutton.forget_button()
        self.tree.place_forget()

    def back_selection(self):
        self.forget_homepage()
        self.master_previous.selection_show()
    
    
    
        
