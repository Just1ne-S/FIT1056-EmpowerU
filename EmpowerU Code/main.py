import tkinter as tk
from interfaces.main_window import MW

def main():
    root = MW(title="EmpowerU - Learning Application",width="950",height="700")
    root.mainloop()
    print("EmpowerU proper shutdown completed.")

if __name__ == "__main__":
    main()
