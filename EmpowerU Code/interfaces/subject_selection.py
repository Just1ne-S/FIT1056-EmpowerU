import tkinter as tk
from interfaces.python_homepage import PythonHP

class Selection(tk.Frame):
    def __init__(self,master,image_path_1,image_path_2,image_path_3):
        super().__init__(master=master)
        self.master = master
        self.image_path_1 = image_path_1
        self.image_path_2 = image_path_2
        self.image_path_3 = image_path_3
        
        # Title for subject selection
        self.title = tk.Label(self,text="Subject Choice",font=("Arial Bold",20))
        self.title.grid(columnspan=3,row=0,padx=20,pady=10)

        # First button
        self.Python_imp = tk.PhotoImage(file=self.image_path_1)
        self.Python = tk.Button(self, image=self.Python_imp,width=250, height=250,command=self.PythonPage)
        self.Python.grid(row=1,column=0,padx=20,pady=10)

        # Second button
        self.IS_imp = tk.PhotoImage(file=self.image_path_2)
        self.IS = tk.Button(self, image=self.IS_imp,width=250, height=250)
        self.IS.grid(row=1,column=1,padx=20,pady=10)

        # Third button
        self.AI_imp = tk.PhotoImage(file=self.image_path_3)
        self.AI = tk.Button(self, image=self.AI_imp,width=250, height=250)
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
        python_hp = PythonHP(master=self.master)
        python_hp.show_homepage()

if __name__ == "__main__":
    pass
