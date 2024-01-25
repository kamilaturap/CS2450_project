def readProgram(file):
    registers = {}
    for i in range(101):
        registers[i] = ''
    with open(file, "r") as program:
        lst = program.readlines()
        for i in range(len(lst)):
            registers[i] = lst[i]
    return registers

def main():
    print(readProgram('Test1.txt'))
    return

if __name__ == "__main__":
    main()