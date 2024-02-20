'''
main.py: 
put the whole thing into a class, and started working on taking input from user. the program pauses after it takes the file and idk why
i'm lowkey going crazy
'''

from tkinter_test import *


class RunProgram:
    def __init__(self):
        self.prog = Memory()
        self.word_entry = None
        self.root = tk.Tk()
        self.gui = SimpleGUI(self.root)

    def main(self):
        self.gui.call_screen()
        operation = ''

        while self.prog.pointer <= 99 and operation != '43':
            if len(self.prog.registers[self.prog.pointer]) == 5:
                operation = self.prog.registers[self.prog.pointer][1:3]
                mem = int(self.prog.registers[self.prog.pointer][3:])
            elif len(self.prog.registers[self.prog.pointer]) == 4:
                operation = self.prog.registers[self.prog.pointer][0:2]
                mem = int(self.prog.registers[self.prog.pointer][2:])

            match operation:
                # i/o operations:
                # READ
                case '10':
                    # the program is either stopping here or in readProgram
                    word_entry = self.gui.read_input()
                    self.prog.read(mem, word_entry)
                # WRITE
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
                # default
                case _:
                    self.prog.pointer += 1
                    continue
            self.prog.pointer += 1

        self.root.mainloop()


if __name__ == "__main__":
    runner = RunProgram()
    runner.main()

'''
tkinter.py file
this file basically contains all the gui elements and functions
'''

import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from Memory import *


class SimpleGUI:
    def __init__(self, root):
        self.word_entry = None
        self.text_widget = None
        self.root = root
        self.button = None
        self.prog = Memory()

    def read_input(self): #this function is not working 
        while True:
            self.word_entry = tk.Entry(self.root)
            self.word_entry.pack()  # put the entry widget onto the screen
            # break the loop temporarily to wait for user input
            self.root.wait_window(self.word_entry.winfo_toplevel())
            word = self.word_entry.get()
            if word:
                return word
            else:
                messagebox.showwarning("Warning", "Please enter a value.")

    def import_file(self):
        file_path = filedialog.askopenfilename(title="Select a file",
                                               filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_widget.delete('1.0', tk.END)
                self.text_widget.insert(tk.END, content)
            self.prog.readProgram(file_path)

    def call_screen(self):
        self.root.title("UVSim")

        # Set window size and position
        window_width = 800
        window_height = 500

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        label = tk.Label(self.root, text="Welcome to UVSim!")
        label.pack(pady=10)

        import_button = tk.Button(self.root, text="Import File",
                                  command=lambda: self.import_file())
        import_button.pack(pady=5)

        self.text_widget = tk.Text(self.root, wrap="word", width=50, height=20)
        self.text_widget.pack(pady=5)

''' 
memory.py 

only changed the read function
'''
    def read(self, targetMemoryLocation, word):
        if word[0] in ['+', '-']:
            while len(word) < 5:
                word = word[0:1] + '0' + word[1:]
            word = word[0:5]
        else:
            while len(word) < 4:
                word = '0' + word
            word = word[0:4]
        self.registers[int(targetMemoryLocation)] = word
        return
