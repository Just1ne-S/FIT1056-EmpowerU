import tkinter as tk 
from interfaces.Users_database.users_database_homepage import UsersDatabaseHP
from interfaces.Receptionist_details.receptionist_details_homepage import ReceptionistDetailsHP

class ReceptionistHomepage(tk.Frame):
    def __init__(self, master, image_path_1, image_path_2, path_1, path_2, receptionist):
        super().__init__(master=master)
        self.master = master 
        self.image_path_1 = image_path_1
        self.image_path_2 = image_path_2
        self.path_1 = path_1
        self.path_2 = path_2
        self.receptionist = receptionist

        # Title for receptionist's selection
        self.title = tk.Label(self,text=f"Welcome {receptionist.first_name} {receptionist.last_name}!",font=("Arial Bold",30))
        self.title.grid(columnspan = 3, row = 0, padx = 20, pady = 10)

        # Description
        description="This is the admin/reception interface.\nYou as a admin/receptionist are authorized to view the details of all users that uses EmpowerU."
        self.description_label = tk.Label(self, text=description, wraplength=400.,font=("Arial",13))
        self.description_label.grid(columnspan = 3, row = 2, padx = 20, pady = 10)

        # First button
        self.receptionist_details_img = tk.PhotoImage(file=self.image_path_1)
        self.receptionist_details = tk.Button(self, image=self.receptionist_details_img, width=250, height=250, command=self.receptionist_details_page)
        self.receptionist_details.grid(row=1,column=0,padx=20,pady=10)

        # Second button
        self.users_details_page_img = tk.PhotoImage(file=self.image_path_2)
        self.users_details = tk.Button(self, image = self.users_details_page_img, width=250, height=250, command=self.users_details_page)
        self.users_details.grid(row=1,column=1,padx=20,pady=10)

        # Log out button
        self.logout_btn = tk.Button(self,text="Log out",font=("Arial",12),command=self.logout,width=10)
        self.logout_btn.grid(row=3,columnspan=2,padx=20,pady=10)

    def selection_show(self):
        self.place(relx=.5, rely=.5,anchor=tk.CENTER)
    
    def receptionist_details_page(self):
        self.place_forget()
        receptionist_details_HP = ReceptionistDetailsHP(self.receptionist, master=self.master,master_previous=self)
        receptionist_details_HP.show_homepage()
    
    def users_details_page(self):
        self.place_forget()
        users_database_HP = UsersDatabaseHP(self.receptionist, self.path_2, master=self.master,master_previous=self)
        users_database_HP.show_homepage()
    
    def forget_homepage(self):
        self.place_forget()
        self.backbutton.forget_button()
        self.tree.place_forget()

    def logout(self):
        self.place_forget()
        self.master.show_homepage()

        
