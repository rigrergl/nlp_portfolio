"""
Assignment 1
Rigre Garciandia

Assumptions:
    - I decided to rename the class Person detailed in the instructions to Employee for naming consistency
    - To avoid a conflict with built-in name 'id', I renamed the field in the instructions to 'emp_id'
"""
import sys
import pathlib
import re


class Employee:
    def __init__(self, last, first, mi, emp_id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.emp_id = emp_id
        self.phone = phone

    def display(self):
        print("Employee id: ", self.emp_id)
        print("\t", self.first, self.mi, self.last)
        print("\t", self.phone, "\n")


def gen_employees(text_in_list):  # TODO
    if not text_in_list:
        raise Exception("input must not be empty")
    if not type(text_in_list) == list:
        raise TypeError("text_in must be a list")

    result = {}

    for line_in in text_in_list:
        # split on comma to get fields as text variables
        last, first, mi, emp_id, phone = line_in.split(",")

        # modify last name and first name fo be in Capital Case
        last = last.title()
        first = first.title()

        # modify the MI to be a single upper case letter, use 'X' as MI if one is missing
        if mi:
            mi = mi.upper()
        else:
            mi = 'X'

        # modify emp_id if necessary
        m = re.match(r'^[a-zA-Z]{2}\d{4}$', emp_id)
        while not m:
            print("ID invalid:", emp_id, "\nID is two letters followed by 4 digits")
            emp_id = input("Please enter a valid ID: ")
            m = re.match(r'^[a-zA-Z]{2}\d{4}$', emp_id)

    return result


if __name__ == '__main__':
    # Check if the relative path was entered
    if len(sys.argv) < 2:
        print("Please enter the relative path of the data file as a system arg")
        quit()

    # Retrieve the input data in text format
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        text_in = f.read().splitlines()

    # Generate Employee objects from input data
    employees = gen_employees(text_in[1:])  # ignoring header lines
