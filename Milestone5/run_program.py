from experimental_gui import *
from memory import *


class RunProgram:
    def __init__(self):
        self.gui = UVSimGui(self)
        self.prog = Memory()
        self.file = FileManager()
        self.commands_2_digit = ['10', '11', '20', '21', '30', '31', '32', '33', '40', '41', '42', '43']
        self.commands_3_digit = ['0' + i for i in self.commands_2_digit]
        self.valid = ['+000000', '000000', '+0000', '0000', '']

    def new_window_runner(self):
        new_app = RunProgram()
        new_app.gui.mainloop()

    def load_file(self):
        """Function: clears everything, branches to FileManager class which will load the text area to the program"""
        self.clear()
        self.file.RunFile(self.prog, self.gui)

    def clear(self):
        """Function: clears all the registers and accumulator value"""
        self.prog.clear()

    def make_register_long(self, word):
        """Function: temporarily updates a given register value to be a signed or unsigned 6-digit value."""
        if len(word) > 0:
            if word[0] in ['+', '-']:
                while len(word) < 7:
                    if word[1:3] in self.commands_2_digit:
                        word = word[0:1] + '0' + word[1:3] + '0' + word[3:]
                    elif word[1:4] in self.commands_3_digit:
                        word = word[0:4] + '0' + word[4:]
                    else:
                        word = word[0:1] + '0' + word[1:]
                word = word[0:7]
            else:
                while len(word) < 6:
                    if word[0:2] in self.commands_2_digit:
                        word = '0' + word[0:2] + '0' + word[2:]
                    elif word[0:3] in self.commands_3_digit:
                        word = word[0:3] + '0' + word[3:]
                    else:
                        word = '0' + word
                word = word[0:6]
        return word
    
    def check_registers(self, memory):
        """Function: Checks all registers in a given memory to make sure all user created values are the same length."""
        if len(memory[0]) == 6 or len(memory[0]) == 7:
            for i in memory.values():
                if len(i) != 6 and len(i) != 7 and i not in self.valid:
                    print(i, len(i))
                    return False
        elif len(memory[0]) == 4 or len(memory[0]) == 5:
            for i in memory.values():
                if len(i) != 4 and len(i) != 5 and i not in self.valid:
                    print(i, len(i))
                    return False
        else:
            print(memory[0])
            return False
        return True

    def execute_program(self):
        """Function: Takes the function calls from the text file and parses it. It then will call
        program to run the provided function with the specified register."""
                
        operation = ''
        self.prog.pointer = 0

        if not self.check_registers(self.prog.registers):
            operation = '043'
            self.gui.error_popup("Registers in provided program are not of a consistent length. Please edit your program and try again.")

        while self.prog.pointer <= 249 and operation != '043':
            if len(self.prog.registers[self.prog.pointer]) == 7:
                operation = self.prog.registers[self.prog.pointer][1:4]
                mem = int(self.prog.registers[self.prog.pointer][4:])

            elif len(self.prog.registers[self.prog.pointer]) == 6:
                operation = self.prog.registers[self.prog.pointer][0:3]
                mem = int(self.prog.registers[self.prog.pointer][3:])

            else:
                self.prog.registers[self.prog.pointer] = self.make_register_long(self.prog.registers[self.prog.pointer])
                if len(self.prog.registers[self.prog.pointer]) == 7:
                    operation = self.prog.registers[self.prog.pointer][1:4]
                    mem = int(self.prog.registers[self.prog.pointer][4:])

                elif len(self.prog.registers[self.prog.pointer]) == 6:
                    operation = self.prog.registers[self.prog.pointer][0:3]
                    mem = int(self.prog.registers[self.prog.pointer][3:])

            match operation:
                # i/o operations:
                # READ
                case '010':
                    self.prog.read(mem, self.gui.popup())
                # WRITE
                case '011':
                    o_word = self.prog.write(mem)
                    self.gui.output(o_word)
                # load/store operations:
                # LOAD
                case '020':
                    self.prog.load(mem)
                # STORE
                case '021':
                    self.prog.store(mem)
                # Arithmetic operation:
                # ADD
                case '030':
                    self.prog.add(mem)
                # SUBTRACT
                case '031':
                    self.prog.subtract(mem)
                # DIVIDE
                case '032':
                    self.prog.divide(mem)
                # MULTIPLY
                case '033':
                    self.prog.multiply(mem)

                # Control operation:
                # BRANCH
                case '040':
                    self.prog.branch(mem)
                # BRANCHNEG
                case '041':
                    self.prog.branchneg(mem)
                # BRANCHZERO
                case '042':
                    self.prog.branchzero(mem)
                # HALT
                case '043':
                    break

                # default:
                case _:
                    self.prog.pointer += 1
                    continue
            self.prog.pointer += 1
        return


if __name__ == "__main__":

    instances = [None]
    instances[0] = RunProgram()
    instances[0].gui.mainloop()