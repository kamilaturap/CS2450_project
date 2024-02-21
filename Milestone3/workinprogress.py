'''
cleaned it up a bit. read still isn't working, I think it's because the while loop is not reaching mainloop() after the read function, which would be why the widget does not appear
the solution would be to create a separate tkinter loop to make it pop up in another screen which is not ideal but idk how else to do it
'''
import sys
import tkinter as tk
from tkinter import ttk, filedialog
from Memory import *


class Frame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UVSim")

        window_width = 900
        window_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.main = Main(self)

        self.mainloop()


class Main(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.input = None
        self.prog = Memory()
        self.readfile = ReadFile(self)
        self.executor()

    def executor(self):
        operation = ''

        while self.prog.pointer <= 99 and operation != '43':
            if len(self.prog.registers[self.prog.pointer]) == 5:
                operation = self.prog.registers[self.prog.pointer][1:3]
                mem = int(self.prog.registers[self.prog.pointer][3:])

            elif len(self.prog.registers[self.prog.pointer]) == 4:
                operation = self.prog.registers[self.prog.pointer][0:2]
                mem = int(self.prog.registers[self.prog.pointer][2:])

            if operation == '10':
                self.input = UserInput(self)
                self.input.read_entry()
                word_entry = self.input.get_entry()
                self.prog.read(mem, word_entry)

            match operation:
                # i/o operations:
                # READ
                case '11':
                    self.prog.write(mem)
                # load/store operations:
                # LOAD
                case '20':
                    self.prog.load(mem)
                # STORE
                case '21':
                    self.prog.store(mem)
                # Arithmetic operation:
                # ADD
                case '30':
                    self.prog.add(mem)
                # SUBTRACT
                case '31':
                    self.prog.subtract(mem)
                # DIVIDE
                case '32':
                    self.prog.divide(mem)
                # MULTIPLY
                case '33':
                    self.prog.multiply(mem)

                # Control operation:
                # BRANCH
                case '40':
                    self.prog.branch(mem)
                # BRANCHNEG
                case '41':
                    self.prog.branchneg(mem)
                # BRANCHZERO
                case '42':
                    self.prog.branchzero(mem)
                # HALT
                case '43':
                    break

                # default:
                case _:
                    self.prog.pointer += 1
                    continue
            self.prog.pointer += 1
        return


class ReadFile(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.text_widget = None
        self.prog = Memory()
        self.import_widgets()

    def import_file(self):
        file_path = filedialog.askopenfilename(title="Select a file",
                                               filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_widget.delete('1.0', tk.END)
                self.text_widget.insert(tk.END, content)
            self.prog.readProgram(file_path)

    def import_widgets(self):
        import_button = tk.Button(text="Import File",
                                  command=lambda: self.import_file())
        import_button.pack(pady=5)

        self.text_widget = tk.Text(wrap="word", width=50, height=20)
        self.text_widget.pack(pady=5)
        

class UserInput (tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.entry = None
        self.display_label = None
        self.read_entry()

    def read_entry(self):
        enter = tk.Label(text="Please enter an input")
        enter.pack()

        self.entry = tk.Entry()
        self.entry.pack()

        submit_button = tk.Button(text="Submit", command=self.print_entry)
        submit_button.pack()

        self.display_label = tk.Label(text="")
        self.display_label.pack()
        
    def print_entry(self):
        entry_value = self.get_entry()
        self.display_label.config(text=f"Entered value: {entry_value}")
    
    def get_entry(self):
        return self.entry.get()


Frame()
