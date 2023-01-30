# Assignment 1 Overview
The goal of this program is to get familiar with text processing in python. 
It takes a csv input file and standardizes the formats of the data fields.
It then creates a objects for each entry in the input file and creates a dictionary for those objects.
It then uses a pickle to dump and load the dictionary object and then displays the contents of the objects.

For input fields that are not in a correct format, the program outputs and error message and asks the user to re-enter the value.

## How to run it
Requirements:
- Python 3 or above interpreter installed on computer
- [`main.py`](Assignment1/main.py) source file 
- `data.csv` file

Steps:
1. `cd` into the same directory as `main.py`
2. Enter the following command `python main.py [relative path to data file]`

Example run: `python main.py data/data.csv`

## My opinions on text processing using Python
In my opinion, python is suitable for text processing because of the vast library ecosystem, as well as the ability to slice strings.
One weakness that python does have for text processing is the lack of types, which can cause some confusion for programmers, which is an issue that I imagine is much bigger when maintaining legacy code.

## What I learned
In this assignment, I learned:
- How to use sysarg in python
- Basics of object-oriented programming in python
- Basics of using regex in python
- How to use pickle files
- Basic file I/O in python
- Basics of how to write 'pythonic' code
- Get comfortable with python programming using PyCharm