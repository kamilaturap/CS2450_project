'''
This file does the same thing as maingui.py but it separates the code based on the presentation layer and the business model layer.
'''
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
        self.addLabel(text='Program Output:', row=2, column=0, background='#275D38', foreground='#A7A8AA')
        self.progField = self.addTextArea(text=self.text, row=3, column=0, columnspan=3, width=20)
        self.addButton(text='Clear', row=4, column=1, command=self.clear)
        self.addButton(text="Import File", row=0, column=0, command=self.import_file)

    def output(self, o):
        self.progField.appendText(o + '\n')

    def popup(self):
        return self.prompterBox(title='input', promptString='enter signed four-digit word')

    def clear(self):
        self.load.setText('')
        self.progField.setText('')
        self.run.clear()

    def import_file(self):
        self.file_path = filedialog.askopenfilename(title="Select a file",
                                               filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

    def get_file(self):
        return self.file_path

    def load_program(self):
        self.load.setText('Loaded')

    def set_registers(self, content):
        self.progField.appendText(tk.END, content)

# consider automatically loading the program as soon as user inputs file, rather than making them separately load it


class RunProgram:
    def __init__(self):
        self.gui = Gui(self)
        self.prog = Memory()

    def clear(self):
        self.prog.clear()

    def load_file(self):
        self.prog.clear()
        self.gui.load_program()
        self.prog.readProgram(self.gui.get_file())



    def execute_program(self):
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


'''printing the registers to the file/ not working
if self.gui.get_file():
    with open((self.gui.get_file(), "r")) as file:
        content = file.read()
        self.gui.set_registers(content)
'''
