import tkinter as tk
from interfaces.main_window import MW
from app.compiled_adjust_lines import compiled_adjust_lines

def main():
    compiled_adjust_lines()
    root = MW(title="EmpowerU - Learning Application",width="1200",height="840")
    root.mainloop()
    print("EmpowerU proper shutdown completed.")    

if __name__ == "__main__":
    main()
                
