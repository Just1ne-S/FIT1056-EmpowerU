import tkinter as tk
from interfaces.main_window import MW
from app.adjust_lines import adjust_lines

def main():
    adjust_lines("./data/receptionist_login_info.txt")
    adjust_lines("./data/user_login_info.txt")
    root = MW(title="EmpowerU - Learning Application",width="950",height="700")
    root.mainloop()
    print("EmpowerU proper shutdown completed.")

if __name__ == "__main__":
    main()
