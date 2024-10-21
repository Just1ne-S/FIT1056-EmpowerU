import tkinter as tk
from interfaces.progress_bar import ProgressBar
from interfaces.content_buttons import ContentButton
from interfaces.back_button import BackButton
from interfaces.display_label import DisplayLabel
from interfaces.Information_Security.info_security_content import InfoSecurityContent

class InfoSecurityHP(tk.Frame):
    def __init__(self,master,master_previous,user):
        super().__init__(master=master)
        self.master = master
        self.master_previous = master_previous
        self.path_1 = "1.Introduction to Information Security"
        self.path_2 = "2.Types of Threats"
        self.path_3 = "3.Cryptography Basics"
        self.path_4 = "4.Network Security Fundamentals"
        self.path_5 = "5.Authentication and Access Control"
        self.path_6 = "6.Security Policies and Best Practices"
        self.path_7 = "7.Ethical and Legal\n\
Considerations in Information Security"
        self.path_8 = "8.Conclusion"
        self.user = user
        self.user_id = self.user.user_id
        self.pressed_list = []
        self.content_buttons = ContentButton(self.master,self.path_1,self.path_2,self.path_3,self.path_4,self.path_5,self.path_6,self.path_7,self.path_8)
        self.button_list = [self.content_buttons.topic_1,self.content_buttons.topic_2,self.content_buttons.topic_3,self.content_buttons.topic_4,self.content_buttons.topic_5,self.content_buttons.topic_6,self.content_buttons.topic_7,self.content_buttons.topic_8] 
        with open("./data/Information_Security/information_security_progress.txt","r") as rf:
                self.lines = rf.readlines()
                self.lines = [line.strip() for line in self.lines]
                for user_index,line in enumerate(self.lines):
                    user_id,bool1,bool2,bool3,bool4,bool5,bool6,bool7,bool8 = line.split(",")
                    if self.user_id == user_id: 
                       self.pressed_list = [bool1,bool2,bool3,bool4,bool5,bool6,bool7,bool8]
                       self.user_index = user_index

        for i in range(len(self.pressed_list)):
            if self.pressed_list[i] == "False":
                self.button_list[i].config(state="normal")

        self.title = tk.Label(master=self,text="Information Security Hub: Safeguarding Your Digital World",font=("Arial Bold",16))
        self.title.grid(row=0,columnspan=2,padx=10,pady=10)
        self.progress = 0
        
        self.progressbar = ProgressBar(self)
        self.progressbar.progress_bar.grid(row=1,columnspan=2,padx=10,pady=10)

        count = self.pressed_list.count("False")
        self.progress = 100/8*count
        self.progressbar.progress_value.set(self.progress)

        for i in range(len(self.button_list)-1):
            self.button_list[i].config(command=lambda index=i: self.activate_button(index+1))
        try:
            self.img = DisplayLabel(master=self.master,text_input=None,directory="./images/Information Security Logo.png",role="Image",rel_x=.2,rel_y=.4,font=None)
        except tk.TclError:
            print("Make sure that all files are present in the images folder.")
        self.backbutton = BackButton(self.master,self,"Back to Selection Page")
        self.backbutton.back_button.config(command=self.back_selection)

        self.label = DisplayLabel(master=self.master,text_input=
"Welcome to Your Information Security Journey!\n\
\n\
Embark on a path to understanding-\n\
the essentials of safeguarding data.\n\
\n\
Explore each concept step-by-step and learn how to-\n\
protect yourself and others in the digital world.\n\
\n\
Every challenge is an opportunity to strengthen-\n\
your skills and enhance your knowledge!"
                ,directory=None,role="Text",rel_x=.2,rel_y=.7,font=("Arial Bold",12))  
        self.content_buttons.topic_8.config(command=self.check_eighth_button)
        
        
                
    def activate_button(self,index):
        self.button_list[index].config(state="normal")
        self.pressed_list[index] = "False"
        self.show_content(index-1)
        count = self.pressed_list.count("False")
        self.progress = 100/8*count
        self.progressbar.progress_value.set(self.progress)
        try:
            wf = open("./data/Information_Security/information_security_progress.txt","w")
            new_line = [self.user_id] + self.pressed_list
            new_line = ",".join(map(str,new_line))
            self.lines[self.user_index] = new_line
            for line in self.lines:
                wf.write(f"{line}\n")
        except FileNotFoundError:
            print("Make sure that you have the file python_progress.txt in the data folder")

    
    def check_eighth_button(self):
        self.pressed_list[0] = "False"   
        count = self.pressed_list.count("False")
        self.progress = 100/8*count
        self.progressbar.progress_value.set(self.progress)
        self.show_content(7)
        try:
            wf = open("./data/Information_Security/information_security_progress.txt","w")
            new_line = [self.user_id] + self.pressed_list
            new_line = ",".join(map(str,new_line))
            self.lines[self.user_index] = new_line
            for line in self.lines:
                wf.write(f"{line}\n")
        except FileNotFoundError:
            print("Make sure that all files are present in the data folder.")

    def show_content(self,topic_index):
        try:
            self.content = InfoSecurityContent(self.master,self,topic_index)
        except FileNotFoundError:
            print("Make sure that all files are present in the data folder.")
        self.forget_homepage()
        self.content.show_content()
        
        
    def show_homepage(self):
        self.place(relx=.5,rely=.1,anchor=tk.CENTER)
        self.content_buttons.show_buttons()
        self.backbutton.place(relx=.08,rely=.95,anchor=tk.CENTER)
        self.img.show_label()
        self.label.show_label()

    def forget_homepage(self):
        self.place_forget()
        self.content_buttons.forget_buttons()
        self.backbutton.forget_button()
        self.img.forget_label()
        self.label.forget_label()

    def back_selection(self):
        self.forget_homepage()
        self.master_previous.selection_show()

if __name__ == "__main__":
    pass