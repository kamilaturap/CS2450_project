Scrum Master: Cameron Hurst

To run this program, download the folder titled gui. Start the program GUI by running the file maingui.py. Enter the name of your BasicML program file at the top of the window where it says, "enter filepath". Click "load program" to load the program into the simulator's registers. Click the "run" button to execute the BasicML program. Enter any inputs as prompted. The simulator will print any outputs in the "program output" field. Clicking the "clear" button at the bottom will clear the Basic ML program from the registers, resetting them all back to "+0000". "Clear" will also clear any outputs. To re-run a program or to run a new program after a program has been cleared, a program file name will need to be input and loaded.

BasicML logic:
I/O operation: READ = 10 Read a word from the keyboard into a specific location in memory. WRITE = 11 Write a word from a specific location in memory to screen.

Load/store operations: LOAD = 20 Load a word from a specific location in memory into the accumulator. STORE = 21 Store a word from the accumulator into a specific location in memory.

Arithmetic operation: ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator) SUBTRACT = 31 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator) DIVIDE = 32 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator). MULTIPLY = 33 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).

Control operation: BRANCH = 40 Branch to a specific location in memory BRANCHNEG = 41 Branch to a specific location in memory if the accumulator is negative. BRANCHZERO = 42 Branch to a specific location in memory if the accumulator is zero. HALT = 43 Stop the program
