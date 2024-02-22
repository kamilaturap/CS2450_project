from breezypythongui import EasyFrame
from Memory import *
from main import *

class Gui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="UV Sim", background='#275D38')
        self.prog = Memory()
        self.text = ''
        self.inField = ''
        self.file = self.addTextField(text='',row=0, column=1)
        self.addLabel(text='Input program filepath:', row=0, column=0, background='#275D38', foreground='#A7A8AA')
        self.addButton(text='load program', row=0, column=2, command= self.handleButtonClick_loadFile)
        self.addButton(text='Run', row=0, column=3, command= self.handleButtonClick_run)
        self.addLabel(text='Program Output:', row=2, column=0, background='#275D38', foreground='#A7A8AA')
        self.progField = self.addTextArea(text=self.text, row=3, column= 0, columnspan= 3, width=20)
        self.addButton(text='clear', row=4, column=1, command= self.handleButtonClick_clear)
    
    def guiOut(self, o):
        self.progField.appendText(o + '\n')

    def handleButtonClick_clear(self):
        self.file.setText('')
        self.progField.setText('')
        self.prog = Memory()

    def handleButtonClick_loadFile(self):
        file = self.file.getText()
        self.prog.readProgram(file)
        
    def handleButtonClick_run(self):
        self.run()
        
    def run(self):
        operation = ''
    
        while self.prog.pointer <= 99 and operation != '43':
            if len(self.prog.registers[self.prog.pointer]) == 5:
                operation = self.prog.registers[self.prog.pointer][1:3]
                mem = int(self.prog.registers[self.prog.pointer][3:])

            elif len(self.prog.registers[self.prog.pointer]) == 4:
                operation = self.prog.registers[self.prog.pointer][0:2]
                mem = int(self.prog.registers[self.prog.pointer][2:])
                
            match operation:
            #i/o operations:
                #READ
                case '10':
                    self.prog.read(mem, self.prompterBox(title='input', promptString='enter signed four-digit word'))
                #WRTIE
                case '11':
                    o_word = self.prog.write(mem)
                    self.guiOut(o_word)
            #load/store operations:
                #LOAD
                case '20':
                    self.prog.load(mem)
                #STORE
                case '21':
                    self.prog.store(mem)
            #Arithmetic operation:
                #ADD
                case '30':
                    self.prog.add(mem)
                #SUBTRACT
                case '31':
                    self.prog.subtract(mem)
                #DIVIDE
                case '32':
                    self.prog.divide(mem)
                #MULTIPLY
                case '33':
                    self.prog.multiply(mem)

            #Control operation:
                #BRANCH
                case '40':
                    self.prog.branch(mem)
                #BRANCHNEG
                case '41':
                    self.prog.branchneg(mem)
                #BRANCHZERO
                case '42':
                    self.prog.branchzero(mem)          
                #HALT
                case '43':
                    break

                #default:
                case _:
                    self.prog.pointer += 1
                    continue
            self.prog.pointer += 1
        return

Gui().mainloop()
