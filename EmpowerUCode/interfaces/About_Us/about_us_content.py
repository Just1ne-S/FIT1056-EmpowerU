#about us
import tkinter as tk
class AboutUs(tk.Frame):
    def __init__(self,master):
        super().__init__(master=master)
        """
        about_us function prints the information about the company EmpowerU and the services it provides
        """
        about_us_text = (
            "\n"
            "EmpowerU(version1.0)\n"
            "At EmpowerU, our aim is to support and encourage adults to learn and provide the right tools they need to explore and develop essential technical skills. Whether you are starting your journey or looking forward to improving your foundation, we're here to assist your learning to real-world scenarios in three major areas:\n\n"
            "    Programming (Python) - Learn the fundamentals of the widely used programming language.\n"
            "    Information Security - Learn how to safeguard information in the advanced digital age.\n"
            "    Artificial Intelligence (AI) - Learn about the fastest growing sector which shapes and transforms multiple major industries.\n\n"
            "What Makes EmpowerU Different?\n"
            "EmpowerU is designed to offer a dynamic learning experience that provides interactive quizzes, tutorials, a progress tracker, and feedback to ensure learning is smooth and progressive.\n"
            "    Interactive Learning - Provides interactive tutorials and quizzes.\n"
            "    Progress Tracking - Track your progress and plan your study.\n"
            "    Feedback - Provides feedback and explanation on mistakes to boost learning.\n\n"
            "We are strongly committed to increasing awareness and skillsets among adults in this technology-driven world that can drive real-world impact. Whether you are new to technology or looking to improve, join us today and begin your journey towards mastering the essential tech skills of tomorrow!")

    # Label to display the About Us
        self.about_us_label_1 = tk.Label(master=self, text="ABOUT US", justify="left", wraplength=500,font=("Arial Bold",18))
        self.about_us_label_1.grid(row=0, columnspan=2, padx=10, pady=10)

        self.about_us_label_2 = tk.Label(master=self, text=about_us_text, justify="left", wraplength=700,font=("Arial",13))
        self.about_us_label_2.grid(row=1, columnspan=2, padx=10, pady=10)

        # Close button to hide About Us (initially hidden)
        self.close_button = tk.Button(master=self, text="Close", command=self.hide_about_us,font=("Arial",14))
        self.close_button.grid(row=2, columnspan=2, padx=10, pady=10)

    def show_about_us(self):
        self.place(relx=.5,rely=.1,anchor=tk.N)

    def hide_about_us(self):
        self.place_forget()
