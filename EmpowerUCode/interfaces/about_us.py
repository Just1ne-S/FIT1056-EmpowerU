#about us
import tkinter as tk

def about_us(about_us_label, close_button):
    """
    about_us function prints the information about the company EmpowerU and the services it provides
    """
    about_us_text = (
        "ABOUT US\n\n"
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

    about_us_label.config(text=about_us_text)
    about_us_label.grid()
    close_button.grid()

