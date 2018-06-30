# untapt Tech Puzzle


## The Problem

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, 
must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to 
send back to Earth.
 
A rover's position and location is represented by a combination of x and y co-ordinates and a letter representing one 
of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position 
might be 0, 0, N, which means the rover is in the bottom left corner and facing North.
 
In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'.  
'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 
'M' means move forward one grid point, and maintain the same heading.
 
Assume that the square directly North from (x, y) is (x, y+1).
 
INPUT:
The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.
 
The rest of the input is information pertaining to the rovers that have been deployed. 
Each rover has two lines of input.
 
- The first line gives the rover's position, and the second line is a series of instructions telling the rover how to 
explore the plateau.
 
- The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates 
and the rover's orientation.
 
- Each rover will be finished sequentially, which means that the second rover won't start to move until the first one 
has finished moving.
 
 
## OUTPUT
The output for each rover should be its final co-ordinates and heading.
 
## INPUT AND OUTPUT
 
### Test Input:
5 5<br>
1 2 N<br>
LMLMLMLMM<br>
3 3 E<br>
MMRMMRMRRM
 
### Expected Output:
1 3 N<br>
5 1 E<br>
==========


## Solution

 - Language: Python 3.5
 - Input: `input.txt`
 - Output: results printed to terminal
 - Execution: `$ ./run.sh`
 - Unit Test Execution: `$ ./test.sh`
 
 ### Modules
 
1. controller.py - controls application flow

    - read_input_file - read input source file
    - main - main processing logic
 
2. input.txt - input source file
 
3. model.py - application interface for file operations

    - read_file - for a given input file path, read and validate the file.  Returns list of valid and invalid orders

4. rover.py - class definitions for following rover instructions

    - init - initializes the rover properties: (x, y) starting position, starting direction, maximum distance to 
    travel along the x & y axis and the instructions for the rover
    
    - move_rover - moves the rover based on the input instructions and returns the rover's final position and direction
      
    - move_in_matrix - moves the rover in the specified direction making sure not to exit specified area
 
5. run.sh - Bash script to execute the application
 
6. test.sh - Bash script to run automated tests
 
7. test_model.py - automated tests for model.py

    - test_model_read_file - tests reading a normal input file, missing input file and zero length input file
 
8. test_rover.py - automated tests for rover.py

    - test_move_rover_simple - tests object successfully created and a simple rover move
    - test_move_rover_complex - tests 2 complex rover instructions sets
  
9. test_rover.py - automated tests for rover.py

    - test_move_rover_simple - tests object successfully created and a simple rover move
    - test_move_rover_complex - tests 2 complex rover instructions sets
 
10. view.py - application interface to display information to the user

    - display_msg - displays message to user
