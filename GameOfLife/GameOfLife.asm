// The game of life world consists of 2D grid 16x32, the grid is mapped in memory:
// RAM[100] == grid(0, 0)
// RAM[132] == grid(1, 0)
// RAM[611] == grid(16, 31)
//
// RAM[99] contains number of generations to iterate over the Game of life world (aka grid)
//
// Iteration rules:
// For a space that is 'populated':
// * Each cell with one or no neighbors dies, as if by solitude.
// * Each cell with four or more neighbors dies, as if by overpopulation.
// * Each cell with two or three neighbors survives.
//
// For a space that is 'empty' or 'unpopulated'
// * Each cell with three neighbors becomes populated.
//
// initial values are set by test. The are only two values allowed:
// 1 -- the cell is populated
// 0 -- the cell is empty

// your code here

(LOOP)
////////////////////////////////////////////////////////////////////////

@KBD
D=A
@size
M=D //Assign KBD
@SCREEN
D=A
@size
M=M-D //Assign size = KBD-SCREEN ->(24576-16384)


@100
D=A

@index
M=D //to find out which point we are searching (at start = 100)

@helper
M=D //helper = 100 at start

@col
M=0

@row
M=0

/////////////////

(PAINT)
@size
D=M

@START
D,JEQ //if all painted then start iteration

@helper
D=M

A=D
D=M

@ZERO
D,JEQ


    (ONE)
    @KBD
    D=A

    @size
    D=D-M

    A=D
    M=-1

    @UPDATE_INFO
    0;JMP


    (ZERO)
    @KBD
    D=A

    @size
    D=D-M

    A=D
    M=0



(UPDATE_INFO)
///
@size
M=M-1 //size--
///

@col
D=M

@31
D=D-A

@NEW_LINE
D,JEQ //if column == 31 (reached the left edge)

//if not

@col
M=M+1

@helper
M=M+1

@PAINT
0;JMP

////////////

(NEW_LINE)
@row
D=M

@15
D=D-A

@INCREASE_IND
D,JEQ //if row=15/D=0 so we finished with one line of blocks 

//if not 

@row
M=M+1

@col
M=0

@index
D=M

@helper
M=D

@PAINT
0;JMP

////////////

(INCREASE_IND)
@row
M=0

@col
M=0

@32
D=A

@index
M=M+D

@index
D=M

@helper
M=D

@PAINT
0;JMP

///////////////////////////////////////////////////////////////////
(START)

@99 //Get number of iterations 
D=M //Save in D register

@END //If number of iterations is less or equal to zero jump to END
D,JLE

//-------
@512
D=A

@i //create i = 512 number of all squares in grid
M=D 

/////////////////////////////////////////////////////////////////

@column
M=0 //create column symbol

@row
M=0 //create row symbol


// ----------------------------------------------------------

    (FOR_LOOP)
    @i
    D=M

    @MINUS_ITERATION
    D,JEQ    //If we have been in/update every 512 squares, then one iteration is complete

    //If not find out populated neighbours

    @counter
    M=0 //create counter to store number of populated neighbours
    

///////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////

    (UPPER)
    //Upper neighbours

    @row
    D=M

    @LOWER
    D,JEQ // if row is eqrual to 0 no upper neighbours so jump to the lower neightbours

/////////////////

        (UP_LEFT)
        //Upper left neighbour

        @column
        D=M

        @UP_MIDDLE
        D,JEQ //if column == 0 no left neigbour

    /////
        
        //current point address -> RAM[100 + (512 - i)]
        @612
        D=A //D=612

        @i
        D=D-M //D=612 - i -> current point address
        
        @33
        D=D-A //D-33 -> upper left neughbour's address

        A=D //@(upper left neighbour)

        D=M // D=RAM[612-i-33]

        @UP_MIDDLE
        D,JEQ //if  0 then go to up_middle

        //if not 

        @counter
        M=M+1 //counter ++

///////////////////

        (UP_MIDDLE)
        //Upper middle neighbour

        //current point address -> RAM[100 + (512 - i)]
        @612
        D=A //D=612

        @i
        D=D-M //D=612 - i -> current point address
        
        @32
        D=D-A //D-32 -> upper middle neughbour's address

        A=D //@(upper middle neighbour)

        D=M // D=RAM[612-i-32]

        @UP_RIGHT
        D,JEQ //if  0 then go to up_right 

        //if not 

        @counter
        M=M+1 //counter ++

//////////////////

        (UP_RIGHT)
        //Upper right neighbour

        @column
        D=M

        @31
        D=D-A // column - 31

        @LOWER
        D,JEQ //if (D=0) column = 31 no right neigbour

    /////

        //current point address -> RAM[100 + (512 - i)]
        @612
        D=A //D=612

        @i
        D=D-M //D=612 - i -> current point address
        
        @31
        D=D-A //D-31 -> upper right neughbour's address

        A=D //@(upper right neighbour)

        D=M // D=RAM[612-i-31]

        @LOWER
        D,JEQ //if  0 then go to lower

        //if not 

        @counter
        M=M+1 //counter ++


//////////////////////////

    (LOWER)
    //Below neighbours

    @row
    D=M

    @15
    D=D-A //row - 15

    @ASIDE
    D,JEQ // if (D=0) row is eqrual to 15 no lower neighbours so jump to the aside neightbours

///////////////////

        (DOWN_LEFT)
        //Lower left neighbour

        @column
        D=M

        @DOWN_MIDDLE
        D,JEQ //if column = 0 no left neigbour

    /////

        //current point address -> RAM[100 + (512 - i)]
        @612
        D=A //D=612

        @i
        D=D-M //D=612 - i -> current point address
        
        @31
        D=D+A //D+31 -> down left neughbour's address

        A=D //@(down left neighbour)

        D=M // D=RAM[612-i+31]

        @DOWN_MIDDLE
        D,JEQ //if  0 then go to down_middle

        //if not 

        @counter
        M=M+1 //counter ++


/////////////////////

        (DOWN_MIDDLE)
        //Lower middle neighbour

        //current point address -> RAM[100 + (512 - i)]
        @612
        D=A //D=612

        @i
        D=D-M //D=612 - i -> current point address
        
        @32
        D=D+A //D+32 -> down middle neughbour's address

        A=D //@(down left neighbour)

        D=M // D=RAM[612-i+32]

        @DOWN_RIGHT
        D,JEQ //if  0 then go to down_right

        //if not 

        @counter
        M=M+1 //counter ++



////////////////////

        (DOWN_RIGHT)
        //Lower right neighbour

        @column
        D=M

        @31
        D=D-A // column - 31

        @ASIDE
        D,JEQ //if (D=0) column = 31 no right neigbour

    /////

        //current point address -> RAM[100 + (512 - i)]
        @612
        D=A //D=612

        @i
        D=D-M //D=612 - i -> current point address
        
        @33
        D=D+A //D+33 -> down right neughbour's address

        A=D //@(down right neighbour)

        D=M // D=RAM[612-i+33]

        @ASIDE
        D,JEQ //if  0 then go to ASIDE

        //if not 

        @counter
        M=M+1 //counter ++


////////////////////////////

    (ASIDE)
    //Aside neighbours

////////////////////

        (ASIDE_LEFT)
        //Aside left neighbour

        @column
        D=M

        @ASIDE_RIGHT
        D,JEQ //if column = 0 no left neigbour

    /////

        //current point address -> RAM[100 + (512 - i)]
        @612
        D=A //D=612

        @i
        D=D-M //D=612 - i -> current point address
        
        @1
        D=D-A //D-1 -> aside left neughbour's address

        A=D //@(aside left neighbour)

        D=M // D=RAM[612-i-1]

        @ASIDE_RIGHT
        D,JEQ //if  0 then go to ASIDE_RIGHT

        //if not 

        @counter
        M=M+1 //counter ++


/////////////////////

        (ASIDE_RIGHT)
        //Aside right neighbour

        @column
        D=M

        @31
        D=D-A // column - 31

        @INCREASE_ROW
        D,JEQ //if (D=0) column = 31 no right neigbour

    /////

        //current point address -> RAM[100 + (512 - i)]
        @612
        D=A //D=612

        @i
        D=D-M //D=612 - i -> current point address
        
        @1
        D=D+A //D+1 -> aside right neughbour's address

        A=D //@(aside right neighbour)

        D=M // D=RAM[612-i+1]

        @INCREASE_COLUMN
        D,JEQ //if  0 then go to INCREASE_COLUMN

        //if not 

        @counter
        M=M+1 //counter ++


// finished checking neighbours

///////////////////////////////////////////////////////////
    
    (INCREASE_COLUMN)

    @column
    M=M+1 //column ++ 
    
    //find_out if survived or died
    @FIND_OUT
    0;JMP

///////////////////////////////////////////////////////////////////////////////
    
    (INCREASE_ROW)

    // @row
    // D=M
    
    // @column
    // D=D+M

    // @46
    // D=D-A // column + row - 46(15 + 31)

    // @MINUS_ITERATION
    // D,JEQ //if(column + row = 46 then it was last square in grid)

    //else
    
    @row
    M=M+1 //row ++

    @column
    M=0 //column = 0

    //find_out if survived or died
    @FIND_OUT
    0;JMP

////////////////////////////////////////////////////////////////////////////

    (FIND_OUT)
    
    //current point address -> RAM[100 + (512 - i)]
    @612
    D=A //D=612

    @i
    D=D-M //D= 612 - i -> current point address

    A=D //@(612 - i)

    D=M // D=RAM[612-i]

    @EMPTY
    D,JEQ //If RAM[612 - i] = 0 -> empty jump to EMPTY if not it means POPULATED

//----------------------------------------------------------

    (POPULATED)
    
    @counter
    D=M

    @3
    D=D-A //D=D-3

    @SetAlive
    D,JEQ //if 3 neighbours

    //or

    @counter
    D=M

    @2
    D=D-A //D=D-2

    @SetAlive
    D,JEQ //if 2 neighbours

///if not 

    //current point address -> RAM[100 + (512 - i)]
    @612
    D=A //D=612

    @i
    D=D-M //D=612 - i -> current point address

    @600
    D=D+A //D=D+600 where we will save new state 

    A=D //@(612 - i + 600)

    M = 0 //set empty

    @i
    M=M-1 //i --

    //Jump to FOR_LOOP
    @FOR_LOOP
    0;JMP


////////////////////////////////////////////////////////////////////////

    (EMPTY)

    @counter
    D=M

    @3
    D=D-A //D=D-3

    @SetAlive
    D,JEQ //if 3 neighbours

/// if not 
    
    //current point address -> RAM[100 + (512 - i)]
    @612
    D=A //D=612

    @i
    D=D-M //D=612 - i -> current point address

    @600
    D=D+A //D=D+600 where we will save new state 

    A=D //@(612 - i + 600)

    M=0 //set empty

    @i
    M=M-1 //i --

    //Jump to FOR_LOOP
    @FOR_LOOP
    0;JMP


//--------------------------------------------------------------

    (SetAlive)

    //current point address -> RAM[100 + (512 - i)]
    @612
    D=A //D=612

    @i
    D=D-M //D=612 - i -> current point address

    @600
    D=D+A //D=D+600 where we will save new state 

    A=D //@(612 - i + 600)

    M = 1 //set populated

    @i
    M=M-1 //i --

    //Jump to FOR_LOOP
    @FOR_LOOP
    0;JMP

// -------------------------------------------------------------

(MINUS_ITERATION)
@99 //Number of iterations - 1
M=M-1


//////////////////////////////
@512
D=A

@k
M=D //k = 512

(UPDATE)
@k
D=M

@LOOP
D,JEQ //if k = 0

@612
D=A //D=612

@k
D=D-M //D=612 - k -> current point address

@600
D=D+A //D=D+600

A=D
D=M

@EMPTY_POINT
D,JEQ //if equals 0 then EMPTY if not POPULATE
    
    (POPULATE_POINT)
    @612
    D=A //D=612

    @k
    D=D-M //D=612 - k -> current point address

    A=D
    M=1 //populate

    @k
    M=M-1

    @UPDATE
    0;JMP


    (EMPTY_POINT)
    @612
    D=A //D=612

    @k
    D=D-M //D=612 - k -> current point address

    A=D
    M=0 //empty

    @k
    M=M-1

    @UPDATE
    0;JMP

@LOOP //Jump up to the LOOP 
0;JMP

(END) //The END
@END
0;JMP






