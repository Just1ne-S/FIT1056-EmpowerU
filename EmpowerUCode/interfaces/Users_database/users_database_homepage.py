import tkinter as tk
from tkinter import ttk
from interfaces.back_button import BackButton

class UsersDatabaseHP(tk.Frame):
    def __init__(self, receptionist, path, master, master_previous):
        super().__init__(master=master)
        self.receptionist = receptionist
        self.path = path
        self.master = master
        self.master_previous = master_previous

        self.title = tk.Label(self,text="User Database",font=("Arial Bold",30,"underline"))
        self.title.grid(columnspan = 3, row = 0, padx = 20, pady = 20, sticky="n")

        self.user_database_table()

        self.backbutton = BackButton(self.master,self,"Back to Selection Page")
        self.backbutton.back_button.config(command=self.back_selection)

    def users_details(self):
        with open(self.path,'r') as frobj:
            users_list = []
            lines = frobj.readlines()
            for line in lines:
                data = line.strip().split(',')
                users_list.append([data[0],data[1],data[2],data[3],data[4],data[5],data[6]])
            return users_list

    def user_database_table(self):
        # Create a frame to hold the Treeview and Scrollbar
            self.frame = tk.Frame(master=self.master)

            # Define the columns for the Treeview
            columns = ("S_No.", "user_id", "Username", "First Name", "Last Name", "Contact No.")
            
            # Create the Treeview widget
            self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")

            # Configure the headings
            self.tree.heading("S_No.", text="S_No.", anchor="w")
            self.tree.heading("user_id", text="user_id", anchor="w")
            self.tree.heading("Username", text="Username", anchor="w")
            self.tree.heading("First Name", text="First Name", anchor="w")
            self.tree.heading("Last Name", text="Last Name", anchor="w")
            self.tree.heading("Contact No.", text="Contact No.", anchor="w")

            # Configure the column widths
            self.tree.column("S_No.", width=100, anchor="w")
            self.tree.column("user_id", width=100, anchor="w")
            self.tree.column("Username", width=200, anchor="w")
            self.tree.column("First Name", width=200, anchor="w")
            self.tree.column("Last Name", width=200, anchor="w")
            self.tree.column("Contact No.", width=300, anchor="w")

            # Create a vertical scrollbar for the Treeview
            self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
            self.tree.configure(yscroll=self.scrollbar.set)

            # Pack the Treeview and Scrollbar
            self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.tree.pack()
            # Add the frame to the master
            self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            self.label_frame = tk.Frame(master=self.master)

            text = "This page is used to view user details, that includes their user_id, first name, last name, username and contact number."

            self.label = tk.Label(master=self.label_frame,text=text,font=("Arial",13),wraplength=400)
            self.label.pack()

            self.label_frame.place(relx=.5,rely=.7,anchor=tk.CENTER)

            # Insert user details into the Treeview
            line_number = 1
            for user_data in self.users_details():
                self.tree.insert("", "end", values=(line_number, user_data[0], user_data[4], user_data[1], user_data[2], user_data[3]))
                line_number += 1

            # Apply the header style
            self.apply_header_style()

            


    def apply_header_style(self):
        style = ttk.Style()
        style.configure("Treeview.Heading",font=("Arial", 16, "bold")) 
    
    def show_homepage(self):
        self.place(relx=.5,rely=.1,anchor=tk.CENTER)
        self.user_database_table
        self.backbutton.place(relx=.08,rely=.95,anchor=tk.CENTER)
    
    def forget_homepage(self):
        self.place_forget()
        self.backbutton.forget_button()
        self.frame.place_forget()
        self.label_frame.place_forget()

    def back_selection(self):
        self.forget_homepage()
        self.master_previous.selection_show()
