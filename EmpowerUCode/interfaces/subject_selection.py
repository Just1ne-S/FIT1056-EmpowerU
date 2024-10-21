import tkinter as tk
from interfaces.Python.python_homepage import PythonHP
from interfaces.Information_Security.info_security_homepage import InfoSecurityHP 
from interfaces.Artificial_Intelligence.ai_homepage import AI_HP

class Selection(tk.Frame):
    def __init__(self,master,image_path_1,image_path_2,image_path_3,user):
        super().__init__(master=master)
        self.master = master
        self.image_path_1 = image_path_1
        self.image_path_2 = image_path_2
        self.image_path_3 = image_path_3
        self.user = user
        
        # Title for subject selection
        self.title = tk.Label(self,text="Subject Choice",font=("Arial Bold",20))
        self.title.grid(columnspan=3,row=0,padx=20,pady=10)

        # First button
        self.Python_imp = tk.PhotoImage(file=self.image_path_1)
        self.Python = tk.Button(self, image=self.Python_imp,width=250, height=250,command=self.PythonPage)
        self.Python.grid(row=1,column=0,padx=20,pady=10)

        # Second button
        self.IS_imp = tk.PhotoImage(file=self.image_path_2)
        self.ISecurity = tk.Button(self, image=self.IS_imp,width=250, height=250,command=self.IS)
        self.ISecurity.grid(row=1,column=1,padx=20,pady=10)

        # Third button
        self.AI_imp = tk.PhotoImage(file=self.image_path_3)
        self.AI = tk.Button(self, image=self.AI_imp,width=250, height=250,command=self.AI)
        self.AI.grid(row=1,column=2,padx=20,pady=10)

        # Log out button
        self.logout_btn = tk.Button(self,text="Log out",font=("Arial",12),command=self.logout,width=10)
        self.logout_btn.grid(column=1,row=2,padx=20,pady=10)

    def selection_show(self):
        self.place(relx=.5, rely=.5,anchor=tk.CENTER)
    
    def selection_forget(self):
        self.place_forget()  

    def logout(self):
        self.selection_forget()
        self.master.show_homepage()

    def PythonPage(self):
        self.selection_forget()
        python_hp = PythonHP(master=self.master,master_previous=self,user=self.user)
        python_hp.show_homepage()

    def IS(self):
        self.selection_forget()
        info_security_homepage =InfoSecurityHP(master=self.master,master_previous=self,user=self.user)
        info_security_homepage.show_homepage() 

    def AI(self):
        self.selection_forget()
        ai_homepage = AI_HP(master=self.master,master_previous=self,user=self.user)
        ai_homepage.show_homepage()

if __name__ == "__main__":
    pass

# import sys
# import tkinter as tk
# from tkinter import messagebox

# # Add paths for other modules
# sys.path.append("/Users/krishnaagarwal/Desktop/FIT1056-EmpowerU/EmpowerUCode/interfaces")

# # Import the course dashboard
# from course_dashboard import CourseDashboard

# class Selection(tk.Frame):
#     def __init__(self, master, image_path_1, image_path_2, image_path_3, progress_tracker):
#         super().__init__(master=master)
#         self.master = master
#         self.image_path_1 = image_path_1
#         self.image_path_2 = image_path_2
#         self.image_path_3 = image_path_3

#         # Track the user's progress across different courses
#         self.progress_tracker = progress_tracker

#         # Title for subject selection
#         self.title = tk.Label(self, text="Subject Choice", font=("Arial Bold", 20))
#         self.title.grid(columnspan=3, row=0, padx=20, pady=10)

#         # First button for Python
#         self.Python_imp = tk.PhotoImage(file=self.image_path_1)
#         self.Python = tk.Button(self, image=self.Python_imp, width=250, height=250, command=self.open_python_dashboard)
#         self.Python.grid(row=1, column=0, padx=20, pady=10)

#         # Second button for Information Security
#         self.IS_imp = tk.PhotoImage(file=self.image_path_2)
#         self.IS = tk.Button(self, image=self.IS_imp, width=250, height=250, command=self.open_infosec_dashboard)
#         self.IS.grid(row=1, column=1, padx=20, pady=10)

#         # Third button for AI
#         self.AI_imp = tk.PhotoImage(file=self.image_path_3)
#         self.AI = tk.Button(self, image=self.AI_imp, width=250, height=250, command=self.open_ai_dashboard)
#         self.AI.grid(row=1, column=2, padx=20, pady=10)

#         # Log out button
#         self.logout_btn = tk.Button(self, text="Log out", font=("Arial", 12), command=self.logout, width=10)
#         self.logout_btn.grid(column=1, row=2, padx=20, pady=10)

#     def selection_show(self):
#         self.place(relx=.5, rely=.5, anchor=tk.CENTER)

#     def selection_forget(self):
#         self.place_forget()

#     def logout(self):
#         """
#         Log out and return to the homepage.
#         """
#         self.selection_forget()
#         self.master.show_homepage()

#     def open_python_dashboard(self):
#         """
#         Opens the Python course dashboard.
#         """
#         self.selection_forget()
#         python_dashboard = CourseDashboard("Python", self.progress_tracker)
#         python_dashboard.mainloop()

#     def open_infosec_dashboard(self):
#         """
#         Opens the Information Security course dashboard.
#         """
#         self.selection_forget()
#         infosec_dashboard = CourseDashboard("Information Security", self.progress_tracker)
#         infosec_dashboard.mainloop()

#     def open_ai_dashboard(self):
#         """
#         Opens the AI course dashboard.
#         """
#         self.selection_forget()
#         ai_dashboard = CourseDashboard("AI", self.progress_tracker)
#         ai_dashboard.mainloop()

# if __name__ == "__main__":
#     pass
