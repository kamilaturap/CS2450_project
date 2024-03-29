class Memory:
    def __init__(self):
        self.registers = {}
        for i in range(100):
            self.registers[i] = '+0000'
        self.accumulator = "+0000"
        self.pointer = 0

    def readProgram(self, file):
        """Reads in file containing a basicML program. Loads registers."""
        with open(file, "r") as program:
            lst = program.readlines()
            for i in range(len(lst)):
                self.registers[i] = lst[i].strip()
        return

    #i/o operations:
        #READ
    def read(self, targetMemoryLocation):
        word = input(f"enter signed four-digit word to be stored at {targetMemoryLocation}: ")
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

        #WRITE
    def write(self, targetMemoryLocation):
        print(self.registers[int(targetMemoryLocation)])
        return
    
    #load/store operations:
        #LOAD
    def load(self, targetMemoryLocation):
        self.accumulator = self.registers[int(targetMemoryLocation)]
        return
    
        #STORE
    def store(self, targetMemoryLocation):
        self.registers[int(targetMemoryLocation)] = self.accumulator
        return
    
    #Arithmetic operation:
        #ADD
    def add(self, targetMemoryLocation):
        num = str(int(self.accumulator) + int(self.registers[int(targetMemoryLocation)]))
        if num[0] in ['+', '-']:
            while len(num) < 5:
                num = num[0:1] + '0' + num[1:]
            self.accumulator = num[0:5]
        else:
            while len(num) < 4:
                num = '0' + num
            self.accumulator = num[0:4]
        return
    
        #SUBTRACT
    def subtract(self, targetMemoryLocation):
        num = str(int(self.accumulator) - int(self.registers[int(targetMemoryLocation)]))
        if num[0] in ['+', '-']:
            while len(num) < 5:
                num = num[0:1] + '0' + num[1:]
            self.accumulator = num[0:5]
        else:
            while len(num) < 4:
                num = '0' + num
            self.accumulator = num[0:4]
        return        

        #DIVIDE
    def divide(self, targetMemoryLocation):
        if int(self.registers[int(targetMemoryLocation)]) != 0:
            num = str(int(self.accumulator) // int(self.registers[int(targetMemoryLocation)]))
            if num[0] in ['+', '-']:
                while len(num) < 5:
                    num = num[0:1] + '0' + num[1:]
                self.accumulator = num[0:5]
            else:
                while len(num) < 4:
                    num = '0' + num
                self.accumulator = num[0:4]
        return
    
        #MULTIPLY
    def multiply(self, targetMemoryLocation):
        num = str(int(self.accumulator) * int(self.registers[int(targetMemoryLocation)]))
        if num[0] in ['+', '-']:
            while len(num) < 5:
                num = num[0:1] + '0' + num[1:]
            self.accumulator = num[0:5]
        else:
            while len(num) < 4:
                num = '0' + num
            self.accumulator = num[0:4]

    #Control operation:
        #BRANCH
    def branch(self, targetMemoryLocation):
        self.pointer = int(targetMemoryLocation)
        return
        #BRANCHNEG
    def branchneg(self, targetMemoryLocation):
        accum_val = int(self.accumulator)
        if accum_val < 0:
            self.pointer = int(targetMemoryLocation)
        #BRANCHZERO
    def branchzero(self, targetMemoryLocation):
        accum_val = int(self.accumulator)
        if accum_val == 0:
            self.pointer = int(targetMemoryLocation)
        return
    
    def inc_reg(self):
        self.pointer += 1
        return
