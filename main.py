"""
Authors: Cameron Hurst, Anna Youngstrom, Kamila Turapova, Mackay Grange
Project: Milestone 2
Date: 2/9/2024
Class: CS2450

{High level description of program goes here}
"""
import sys
#import functions here:

def readProgram(file):
    """Reads in file containing a basicML program. Loads registers."""
    registers = {}
    for i in range(100):
        registers[i] = ''
    with open(file, "r") as program:
        lst = program.readlines()
        for i in range(len(lst)):
            registers[i] = lst[i].strip()
    return registers

def main():
    try:
        program = readProgram(sys.argv[1])
    except:
        program = readProgram(input("Please input the name of your program file: "))
    
    operation = ''
    i = 0
    
    while i < 99 and operation != '43':
        operation = program[i][1:3]
        match operation:
        #i/o operations:
            #READ
            case '10':
                print(operation)
            #WRTIE
            case '11':
                print(operation)

        #load/store operations:
            #LOAD
            case '20':
                print(operation)
            #STORE
            case '21':
                print(operation)

        #Arithmetic operation:
            #ADD
            case '30':
                print(operation)
            #SUBTRACT
            case '31':
                print(operation)
            #DIVIDE
            case '32':
                print(operation)
            #MULTIPLY
            case '33':
                print(operation)

        #Control operation:
            #BRANCH
            case '40':
                print(operation)
            #BRANCHNEG
            case '41':
                print(operation)
            #BRANCHZERO
            case '42':
                print(operation)
            #HALT
            case '43':
                break

            #default:
            case _:
                continue
        i += 1
    return

if __name__ == "__main__":
    main()
