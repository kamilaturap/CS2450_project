from tkinter import filedialog

from breezypythongui import EasyFrame
from Memory import *
import tkinter as tk


class Gui(EasyFrame, tk.Tk):
    def __init__(self, run):
        EasyFrame.__init__(self, title="UV Sim", background='#275D38')
        self.prog = None
        self.run = run
        self.text = ''
        self.inField = ''
        self.load = self.addTextField(text='', row=0, column=2)
        # self.addLabel(text='Input program filepath:', row=0, column=0, background='#275D38', foreground='#A7A8AA')
        self.addButton(text='Load program', row=0, column=1, command=self.run.load_file)
        self.addButton(text='Run', row=0, column=3, command=self.run.execute_program)
        self.addLabel(text='Program Registers:', row=2, column=0, background='#275D38', foreground='#A7A8AA')
        self.progField = self.addTextArea(text=self.text, row=3, column=0, columnspan=3, width=20)
        self.addButton(text='Clear', row=6, column=1, command=self.clear)
        self.addButton(text="Import File", row=0, column=0, command=self.import_file)
        self.addLabel(text="Output: ", row=4, column=0, background='#275D38', foreground='#A7A8AA')
        self.output_text = self.addTextArea(text='', row=5, column=0, columnspan=2, width=10, height=5)

    def output(self, o):
        #One parameter: o, the text to be output.
        #Function: prints out the text passed through o.
        self.output_text.appendText(o + '\n')

    def popup(self):
        #Function: small popup prompting the user for an input
        return self.prompterBox(title='input', promptString='enter signed four-digit word')

    def clear(self):
        #Function: resets all text fields and all information in the memory class.
        self.load.setText('')
        self.progField.setText('')
        self.run.clear()
        self.output_text.setText('')

    def import_file(self):
        #Function: first clears all registers then prompts the user to select a file from a directory.
        #         The function then opens the file and reads in the text to a text box to be edited.
        self.clear()
        self.file_path = filedialog.askopenfilename(title="Select a file",
                                                    filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        with open(self.file_path, "r") as file:
            content = file.read()
            self.progField.delete('1.0', tk.END)
            self.progField.insert(tk.END, content)

    def get_file(self):
        #Function: A getter for the file_path variable
        return self.file_path

    def load_program(self):
        #Function: text that prints out when the program gets loaded letting the user know the load
        #         was successful
        self.load.setText('Loaded')

    def set_registers(self, content):
        #Function: loads the function calls from the text file into the program.
        self.progField.appendText(tk.END, content)


class RunProgram:
    def __init__(self):
        self.gui = Gui(self)
        self.prog = Memory()

    def clear(self):
        #Function: clears everything that was there.
        self.prog.clear()

    def load_file(self):
        #Function: clears everything, loads the text file into the program then loads the text
        #         into the editor box.
        self.prog.clear()
        self.gui.load_program()
        self.prog.readProgram(self.gui.get_file())

    def execute_program(self):
        #Function: Takes the function calls from the text file and parses it. It then will call
        #         program to run the provided function with the specified register.
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
                    self.prog.read(mem, self.gui.popup())
                # WRITE
                case '11':
                    o_word = self.prog.write(mem)
                    self.gui.output(o_word)
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


runner = RunProgram()
runner.gui.mainloop()
