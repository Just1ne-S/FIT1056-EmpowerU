import tkinter as tk
class TipsContent(tk.Frame):
    def __init__(self,master):
        super().__init__(master=master)
        """
        tips function includes some information which provides some tips on efficient and effective learning
        parameters - None
        """
        text_1 = "Tips on maximising learning on EmpowerU"
        text_2 = """    
        1. Make use of interactive tutorials and quizzes\n\
        2. To make learning easy break down concepts\n\
        3. Track progress with the help of progress tracker and set effective goals\n\
        4. Learn from mistakes with the help of feedback\n\
        5. Stay motivated and consistent\n\
        6. Embrace small wins and try to earn badges\n\
        7. Take short breaks to learn effectively\n\
        8. Stay away from distractions when learning"""

        # Label to display the About Us
        self.about_us_label_1 = tk.Label(master=self, text=text_1, justify="left", wraplength=500,font=("Arial Bold",18))
        self.about_us_label_1.grid(row=0, columnspan=2, padx=10, pady=10)

        self.about_us_label_2 = tk.Label(master=self, text=text_2, justify="left", wraplength=700,font=("Arial",15))
        self.about_us_label_2.grid(row=1, columnspan=2, padx=10, pady=100)

        # Close button to hide About Us (initially hidden)
        self.close_button = tk.Button(master=self, text="Close", command=self.hide_tips,font=("Arial",14))
        self.close_button.grid(row=2, columnspan=2, padx=10, pady=10)

    def show_tips(self):
        self.place(relx=.5,rely=.1,anchor=tk.N)

    def hide_tips(self):
        self.place_forget()
