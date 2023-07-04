## Instructions
To run the code run the main.py file. You will be able to input commands continuously until you exit the program 

## Notes Re Code
The code is structured using a controller that accepts a user's inputs, then processes those inputs and interacts with the robot and table classes.

The table class represents the 5x5 table that the robot moves around on.

The robot class contains the methods to move the robot around the table, and update information such as its current location or direction

Given the nature of 2d arrays, from a code point of view the coordinates are written in a (y,x) format, but displayed to the user in an (x,y) format. For example when accessing the table the code would look something like table[y][x].


## The table structure
The table is a 2d array, with 'x' representing an empty space, and 'R' representing the robots current position. 

The most challenging aspect of this coding challenge was dealing with the fact that the origin point of the table (0,0) was the bottom left corner, and not the top left. This meant having to work backwards with the y coordinate, and using -1, -2 etc. I accomplished this by getting the negative absolute value of the y coordinate, and then subtracting 1 from it. I am very interested in discussing other ways to accomplish this. 

## Unit Testing
I have used PyTest to write unit tests that test the sample inputs given on the coding challenge website. I have also written unit tests that verify the robot will not move off the board in every direction, and that it can not be placed on an invalid coordinate. I have also written a unit test to verify that the robot will not be deployed with an invalid direction.

## More Time?
If I had more time to work on this challenge, I would look write a more comprehensive set of unit tests. I would also look to get opinions from other developers on how best to handle the origin of the table being in the bottom left corner.  