"""
Authors: Cameron Hurst, Anna Youngstrom, Kamila Turapova, Mackay Grange
Project: Milestone 2
Date: 2/9/2024
Class: CS2450

This program, UVsim, will read in a text file containing a basicML program written one command per line.Each basicML command will be a four-digit signed word.
UVsim will convert the first two digits into one of 12 operations.The second two will be an operand.
The operations include: 10-read, 11-write, 20-load, 21-store, 30-add, 31-subtract, 32-divide, 33-multiply, 40-branch, 41-branchneg, 42-branchzero, and 43-halt.
"""
import sys
# import functions here:
from Memory import *

def main():
    prog = Memory()
    
    try:
        prog.readProgram(sys.argv[1])
    except:
        prog.readProgram(input("Please input the name of your program file: "))
    
    operation = ''
    
    while prog.pointer <= 99 and operation != '43':
        if len(prog.registers[prog.pointer]) == 5:
            operation = prog.registers[prog.pointer][1:3]
            mem = int(prog.registers[prog.pointer][3:])

        elif len(prog.registers[prog.pointer]) == 4:
            operation = prog.registers[prog.pointer][0:2]
            mem = int(prog.registers[prog.pointer][2:])
            
        match operation:
        #i/o operations:
            #READ
            case '10':
                prog.read(mem)
            #WRTIE
            case '11':
                prog.write(mem)
        #load/store operations:
            #LOAD
            case '20':
                prog.load(mem)
            #STORE
            case '21':
                prog.store(mem)
        #Arithmetic operation:
            #ADD
            case '30':
                prog.add(mem)
            #SUBTRACT
            case '31':
                prog.subtract(mem)
            #DIVIDE
            case '32':
                prog.divide(mem)
            #MULTIPLY
            case '33':
                prog.multiply(mem)

        #Control operation:
            #BRANCH
            case '40':
                prog.branch(mem)
            #BRANCHNEG
            case '41':
                prog.branchneg(mem)
            #BRANCHZERO
            case '42':
                prog.branchzero(mem)          
            #HALT
            case '43':
                break

            #default:
            case _:
                prog.pointer += 1
                continue
        prog.pointer += 1
    return

if __name__ == "__main__":
    main()
