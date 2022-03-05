# Nand2Tetris Miterm Project: The Game of Life
Write Game of life simulator on hack assemly. You only need the CPU Emulator program to test the project.

### [50%] Combination 1:

The simulator world consists of a 16x3 matrix, the tray is either occupied (1) or free (0). The initial state of the universe will be loaded through the test file. I'm stuck in the memory of the world at the following addresses:
`` `
RAM [100] == Grid (0, 0)
RAM [132] == Grid (1, 0)
RAM [611] == Grid (16, 31)
`` `

And RAM [99] states how much iteration your simulator should perform.
Each iteration generates a new world. The rules are simple:
`` `
For a space that is "populated":
* Each cell dies with one or none of its neighbors, as if from loneliness.
* Each cell of four or more neighbors dies, as if in an overpopulated population.
* Each cell is survived by two or three neighbors.

For a space that is "empty" or "populated"
* Each cell is inhabited by three neighbors.
`` `

### [50%] Combination 2:
Visualization of all simulators uses a hack screen. The screen is of 256x512 resolution. For convenience, the action within the GameOfLife tray on the screen should be drawn in 16x16 squares. Accordingly the screen will also come out with a matrix of 16x32 squares.

If the tray is busy (1) its corresponding square should be black on the screen (all dots in the square should be black), if the tray is empty (0) all dots in its corresponding square should be white on the screen.

The screen must be transferred after each iteration!


Game of Life is not a simple game, it is so called. cellular automata, one of the types of computational theoretical computer. It is known that he is Turing complete. Which means that despite its meager rules, if we have an infinite universe and can determine the initial state of the universe, it can detect any human being, even if it is computable!

For details see the link https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
