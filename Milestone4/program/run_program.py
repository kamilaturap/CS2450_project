from file_manager import *
from experimental_gui import *


class RunProgram:
    def __init__(self):
        self.gui = UVSimGui(self)
        self.prog = Memory()
        self.file = FileManager()

    def load_file(self):
        """Function: clears everything, branches to FileManager class which will load the text area to the program"""
        self.clear()
        self.file.RunFile(self.prog, self.gui)

    def clear(self):
        """Function: clears all the registers and accumulator value"""
        self.prog.clear()

    def execute_program(self):
        """Function: Takes the function calls from the text file and parses it. It then will call
        program to run the provided function with the specified register."""

        operation = ''
        self.prog.pointer = 0

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

if __name__ == "__main__":
    app = RunProgram()
    app.gui.mainloop()
