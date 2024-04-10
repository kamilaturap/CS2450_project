class Memory:
    def __init__(self):
        self.registers = {}
        for i in range(250):
            self.registers[i] = '+000000'
        self.accumulator = "+000000"
        self.pointer = 0
        self.commands_2_digit = ['10', '11', '20', '21', '30', '31', '32', '33', '40', '41', '42', '43']
        self.commands_3_digit = ['0' + i for i in self.commands_2_digit]

    def clear(self):
        self.registers = {}
        for i in range(250):
            self.registers[i] = '+000000'
        self.accumulator = "+000000"
        self.pointer = 0

    def readProgram(self, file):
        """Reads in file containing a basicML program. Loads registers."""
        lst = file.split("\n")
        for i in range(len(lst)):
            self.registers[i] = lst[i].strip()
        return

    # i/o operations:
    # READ
    def read(self, targetMemoryLocation, word):
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
        self.registers[int(targetMemoryLocation)] = word
        return

        # WRITE

    def write(self, targetMemoryLocation):
        return self.registers[int(targetMemoryLocation)]

    # load/store operations:
    # LOAD
    def load(self, targetMemoryLocation):
        self.accumulator = self.registers[int(targetMemoryLocation)]
        return

        # STORE

    def store(self, targetMemoryLocation):
        self.registers[int(targetMemoryLocation)] = self.accumulator
        return

    # Arithmetic operation:
    # ADD
    def add(self, targetMemoryLocation):
        num = str(int(self.accumulator) + int(self.registers[int(targetMemoryLocation)]))
        if num[0] in ['+', '-']:
            while len(num) < 7:
                num = num[0:1] + '0' + num[1:]
            self.accumulator = num[0:7]
        else:
            while len(num) < 6:
                num = '0' + num
            self.accumulator = num[0:6]
        return

        # SUBTRACT

    def subtract(self, targetMemoryLocation):
        num = str(int(self.accumulator) - int(self.registers[int(targetMemoryLocation)]))
        if num[0] in ['+', '-']:
            while len(num) < 7:
                num = num[0:1] + '0' + num[1:]
            self.accumulator = num[0:7]
        else:
            while len(num) < 6:
                num = '0' + num
            self.accumulator = num[0:6]
        return

        # DIVIDE

    def divide(self, targetMemoryLocation):
        if int(self.registers[int(targetMemoryLocation)]) != 0:
            num = str(int(self.accumulator) // int(self.registers[int(targetMemoryLocation)]))
            if num[0] in ['+', '-']:
                while len(num) < 7:
                    num = num[0:1] + '0' + num[1:]
                self.accumulator = num[0:7]
            else:
                while len(num) < 6:
                    num = '0' + num
                self.accumulator = num[0:6]
        return

        # MULTIPLY

    def multiply(self, targetMemoryLocation):
        num = str(int(self.accumulator) * int(self.registers[int(targetMemoryLocation)]))
        if num[0] in ['+', '-']:
            while len(num) < 7:
                num = num[0:1] + '0' + num[1:]
            self.accumulator = num[0:7]
        else:
            while len(num) < 6:
                num = '0' + num
            self.accumulator = num[0:6]

    # Control operation:
    # BRANCH
    def branch(self, targetMemoryLocation):
        self.pointer = int(targetMemoryLocation) - 1
        return
        # BRANCHNEG

    def branchneg(self, targetMemoryLocation):
        accum_val = int(self.accumulator)
        if accum_val < 0:
            self.pointer = int(targetMemoryLocation) - 1
        # BRANCHZERO

    def branchzero(self, targetMemoryLocation):
        accum_val = int(self.accumulator)
        if accum_val == 0:
            self.pointer = int(targetMemoryLocation) - 1
        return

    def inc_reg(self):
        self.pointer += 1
        return
