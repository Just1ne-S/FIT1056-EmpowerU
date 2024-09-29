import tkinter as tk

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
        self.img_imp1 = tk.PhotoImage(file=self.image_path_1)
        self.img1 = tk.Button(self, image=self.img_imp1,width=250, height=250)
        self.img1.grid(row=1,column=0,padx=20,pady=10)

        # Second button
        self.img_imp2 = tk.PhotoImage(file=self.image_path_2)
        self.img2 = tk.Button(self, image=self.img_imp2,width=250, height=250)
        self.img2.grid(row=1,column=1,padx=20,pady=10)

        # Third button
        self.img_imp3 = tk.PhotoImage(file=self.image_path_3)
        self.img3 = tk.Button(self, image=self.img_imp3,width=250, height=250)
        self.img3.grid(row=1,column=2,padx=20,pady=10)

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

if __name__ == "__main__":
    pass
