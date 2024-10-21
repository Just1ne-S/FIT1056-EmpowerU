import tkinter as tk
from interfaces.progress_bar import ProgressBar
from interfaces.content_buttons import ContentButton
from interfaces.back_button import BackButton
from interfaces.display_label import DisplayLabel
from interfaces.Artificial_Intelligence.ai_content import AIContent
from app.quiz_ui import QuizUI

class AI_HP(tk.Frame):
    def __init__(self,master,master_previous,user):
        super().__init__(master=master)
        self.master = master
        self.master_previous = master_previous
        self.path_1 = "1.Introduction to Artificial Intelligence"
        self.path_2 = "2.History and Variations of AI"
        self.path_3 = "3.Machine Learning and Deep Learning"
        self.path_4 = "4.Natural Language Processing (NLP)"
        self.path_5 = "5.Computer Vision"
        self.path_6 = "6.AI in Robotics"
        self.path_7 = "7.Ethics and Bias in AI"
        self.path_8 = "8.Conclusion"
        self.path_9 = "9.Quiz"
        self.user = user
        self.user_id = self.user.user_id
        self.pressed_list = []
        self.content_buttons = ContentButton(self.master,self.path_1,self.path_2,self.path_3,self.path_4,self.path_5,self.path_6,self.path_7,self.path_8,self.path_9)
        self.button_list = [self.content_buttons.topic_1,self.content_buttons.topic_2,self.content_buttons.topic_3,self.content_buttons.topic_4,self.content_buttons.topic_5,self.content_buttons.topic_6,self.content_buttons.topic_7,self.content_buttons.topic_8,self.content_buttons.topic_9] 
        with open("./data/AI/ai_progress.txt","r") as rf:
                self.lines = rf.readlines()
                self.lines = [line.strip() for line in self.lines]
                for user_index,line in enumerate(self.lines):
                    user_id,bool1,bool2,bool3,bool4,bool5,bool6,bool7,bool8,bool9 = line.split(",")
                    if self.user_id == user_id: 
                       self.pressed_list = [bool1,bool2,bool3,bool4,bool5,bool6,bool7,bool8,bool9]
                       self.user_index = user_index

        for i in range(len(self.pressed_list)):
            if self.pressed_list[i] == "False":
                self.button_list[i].config(state="normal")

        self.title = tk.Label(master=self,text="Empowering the Future with Artificial Intelligence",font=("Arial Bold",16))
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
            self.img = DisplayLabel(master=self.master,text_input=None,directory="./images/AI Logo.png",role="Image",rel_x=.2,rel_y=.4,font=None)
        except tk.TclError:
            print("Make sure that all files are present in the images folder.")
        self.backbutton = BackButton(self.master,self,"Back to Selection Page")
        self.backbutton.back_button.config(command=self.back_selection)

        self.label = DisplayLabel(master=self.master,text_input=
"Welcome to the exciting world of Artificial Intelligence!\n\
\n\
Embark on a journey to understand-\n\
how AI is transforming industries and our daily lives.\n\
\n\
From machine learning to neural networks,\n\
explore the concepts step-by-step and-\n\
discover the endless possibilities that AI offers.\n\
\n\
Remember, every new skill learned is a step towards-\n\
innovation and problem-solving!"
                ,directory=None,role="Text",rel_x=.2,rel_y=.7,font=("Arial Bold",12))  
        self.content_buttons.topic_9.config(command=self.check_ninth_button)
        
        self.quiz_ui = QuizUI(master=self.master,master_previous=self,back_button_text="Back to Information Security Homepage",quiz_file_path="./data/quizzes/ai_quiz.txt",is_interactive=True)
                
    def activate_button(self,index):
        self.button_list[index].config(state="normal")
        self.pressed_list[index] = "False"
        self.show_content(index-1)
        count = self.pressed_list.count("False")
        self.progress = 100/9*count
        self.progressbar.progress_value.set(self.progress)
        try:
            wf = open("./data/AI/ai_progress.txt","w")
            new_line = [self.user_id] + self.pressed_list
            new_line = ",".join(map(str,new_line))
            self.lines[self.user_index] = new_line
            for line in self.lines:
                wf.write(f"{line}\n")
        except FileNotFoundError:
            print("Make sure that you have the file python_progress.txt in the data folder")

    
    def check_ninth_button(self):
        self.pressed_list[0] = "False"   
        count = self.pressed_list.count("False")
        self.progress = 100/9*count
        self.progressbar.progress_value.set(self.progress)
        try:
            wf = open("./data/AI/ai_progress.txt","w")
            new_line = [self.user_id] + self.pressed_list
            new_line = ",".join(map(str,new_line))
            self.lines[self.user_index] = new_line
            for line in self.lines:
                wf.write(f"{line}\n")
        except FileNotFoundError:
            print("Make sure that all files are present in the data folder.")
        try:
            self.quiz_ui = QuizUI(master=self.master,master_previous=self,back_button_text="Back to Artificial Intelligence Homepage",quiz_file_path="./data/quizzes/ai_quiz.txt",is_interactive=True)
            self.quiz_ui.place_frame()
            self.quiz_ui.back_button(rel_x=.118,rel_y=.95)
            self.forget_homepage()
        except FileNotFoundError:
            print("Make sure that all files are present in the data folder.")

    def show_content(self,topic_index):
        try:
            self.content = AIContent(self.master,self,topic_index)
        except FileNotFoundError:
            print("Make sure that all files are present in the data folder.")
        self.forget_homepage()
        self.content.show_content()
        
        
    def show_homepage(self):
        self.place(relx=.5,rely=.1,anchor=tk.CENTER)
        self.content_buttons.show_buttons()
        self.backbutton.place(relx=.08,rely=.95,anchor=tk.CENTER)
        self.quiz_ui.back_button_quiz.forget_button()
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
