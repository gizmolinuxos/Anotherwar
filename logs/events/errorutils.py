if not __name__ == "__main__":
    print("Started <AnotherWar_ErrorUtils>")
    class GenerateErrorScreen:
        def __init__(self):
            pass
        
        def ErrorScreen(self):
            import tkinter as tk
            import sys
            from tkinter import messagebox
            try:
                self.mod_Pygame__.quit()
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror("AnotherWar closed because an error occurred", f"AnotherWar closed because an error occurred\n\nMore Details:\n{self.ErrorMessage}")
                sys.exit()
            except Exception as Message:
                sys.exit()
