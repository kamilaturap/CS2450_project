Scrum Master: Anna Youngstrom

UVSim simulates running a BasicML script. All files imported into UVSim should be written in standard BasicML format with a maximum of 100 registers.

How to install and run UVSim:
1. Make sure you have Python installed and set up on your computer.
2. Download the "program" folder.
3. Run "run_program.py" using python.

How to use UVSim:
  
  If importing a pre-written program:
    1. Click "Import .txt File" and select your BasicML file.
    2. Click "Load Selected Program"
    3. Make any needed changes to the BasicML program. Note: if any changes are made, you must save them by clicking "Save Program Changes" then repeat steps 1 and 2 before the BasicML script will run with the changes.
    4. Click "Run Progam" to run the BasicML script.
  
  If writing a new BasicML program in UVSim:
    1. Write your BasicML script in the top text field. Keep in mind that each row is equivalent to one register. Each line of the script should be a 4-digit word. There should be a maximum of 100 lines.
    2. Click "Save Program Changes" and save the file.
    3. Click "Import .txt File" and select the file you just saved.
    4. Click "Load Selected Program"
    5. Click "Run Program" to run the BasicML script.

How to change color scheme:
1. Click "Settings"
2. Set the background color by moving the color selector bars or imputting a hex value for "Primary Color". Then click "apply".
3. To set the text color, repeat step 2 for "Secondary Color".
4. Repeat steps 2 and 3 until you have the desired color scheme.
5. When finished click "Done" to return to the programming page.

BasicML vocabulary defined as follows:

I/O operations:
READ = 10 Read a word from the keyboard into a specific location in memory.
WRITE = 11 Write a word from a specific location in memory to screen.

Load/store operations:
LOAD = 20 Load a word from a specific location in memory into the accumulator.
STORE = 21 Store a word from the accumulator into a specific location in memory.

Arithmetic operation:
ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
SUBTRACT = 31 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
DIVIDE = 32 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).
MULTIPLY = 33 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).

Control operation:
BRANCH = 40 Branch to a specific location in memory
BRANCHNEG = 41 Branch to a specific location in memory if the accumulator is negative.
BRANCHZERO = 42 Branch to a specific location in memory if the accumulator is zero.
HALT = 43 Stop the program

The last two digits of a BasicML instruction are the operand – the address of the memory location containing the word to which the operation applies.

  
