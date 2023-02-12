Chess Openings Identifier:
This project is a simple tool that takes two files as inputs: a file containing chess openings and a file containing a recorded chess game. It then outputs the name of the opening used in the game.

Usage:
The program can be executed using the following command:
python main.py openings_file game_file

Input Files:
The chess openings file should be in CSV format, with two columns: name and moves. Name is the name of the opening and moves is a string of moves separated by space. Example file is included.

The recorded chess game file should contain moves in the following format:
1.b3 f5 h7 2.e3 f5 4.a6

Output:
The program outputs the name of the opening used in the recorded game. If no opening matches with the game, a NoMatchingOpeningsError is raised. If the game has no moves, a EmptyGameError is raised.

Dependencies:
The program requires the following packages to run:
- csv
- re
- argparse
