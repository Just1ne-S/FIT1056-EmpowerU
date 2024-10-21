import tkinter as tk

class ContentButton(tk.Frame):
    def __init__(self,master,topic1,topic2,topic3,topic4,topic5,topic6,topic7,topic8):
        super().__init__(master=master)
        self.master = master
        self.topic_1 = tk.Button(master=self,text=topic1,width=30,height=5)
        self.topic_1.grid(row=2,column=0,padx=10,pady=10,sticky=tk.E)
        
        self.topic_2 = tk.Button(master=self,text=topic2,width=30,height=5,state="disabled")
        self.topic_2.grid(row=2,column=1,padx=10,pady=10,sticky=tk.W)

        self.topic_3 = tk.Button(master=self,text=topic3,width=30,height=5,state="disabled")
        self.topic_3.grid(row=3,column=0,padx=10,pady=10,sticky=tk.E)

        self.topic_4 = tk.Button(master=self,text=topic4,width=30,height=5,state="disabled")
        self.topic_4.grid(row=3,column=1,padx=10,pady=10,sticky=tk.W)

        self.topic_5 = tk.Button(master=self,text=topic5,width=30,height=5,state="disabled")
        self.topic_5.grid(row=4,column=0,padx=10,pady=10,sticky=tk.E)

        self.topic_6 = tk.Button(master=self,text=topic6,width=30,height=5,state="disabled")
        self.topic_6.grid(row=4,column=1,padx=10,pady=10,sticky=tk.W)

        self.topic_7 = tk.Button(master=self,text=topic7,width=30,height=5,state="disabled")
        self.topic_7.grid(row=5,column=0,padx=10,pady=10,sticky=tk.E)

        self.topic_8 = tk.Button(master=self,text=topic8,width=30,height=5,state="disabled")
        self.topic_8.grid(row=5,column=1,padx=10,pady=10,sticky=tk.E)

    def show_buttons(self):
        self.place(relx=.7,rely=.5,anchor=tk.CENTER)

    def forget_buttons(self):
        self.place_forget()
