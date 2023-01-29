"""
Assignment 1
Rigre Garciandia

Assumptions:
    - I decided to rename the class Person detailed in the instructions to Employee for naming consistency
    - To avoid a conflict with built-in name 'id', I renamed the field in the instructions to 'emp_id'
"""
import sys
import pathlib

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
def gen_employees(text_in): # TODO
    return text_in


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please enter the relative path of the data file as a system arg")
        quit()

    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        text_in = f.read().splitlines()

    employees = gen_employees(text_in[1:])  # ignoring header lines

    test_emp = Employee("Luffy", "Monkey", "D", "123", "111-222-3333")
    test_emp.display()

