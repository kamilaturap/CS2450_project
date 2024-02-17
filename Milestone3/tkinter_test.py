'''
main.py: 

class RunProgram:
    @staticmethod
    def main(file_path):
        prog = Memory()
        prog.readProgram(file_path)

I changed main.py to be a class that takes in a file parameter, with all the other functions inside of it too. 

'''

import tkinter as tk
from tkinter import filedialog, messagebox

from main import RunProgram

#takes in a file. so far does nothing else with it so it endlessly loads right now. 
def import_file():
    file_path = filedialog.askopenfilename(title="Select a file",
                                           filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        RunProgram.main(file_path)
    else:
        messagebox.showerror("Error", f"File '{file_path}' not found.")

# initializes the gui
def main():
    root = tk.Tk()
    root.title("Test GUI")

    # sets window size and position
    window_width = 800
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # centers the screen on startup
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # top header
    label = tk.Label(root, text="Welcome to UVSim!")
    label.pack(pady=10)

    # button to import file
    import_button = tk.Button(root, text="Import File",
                              command=lambda: import_file())
    import_button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
