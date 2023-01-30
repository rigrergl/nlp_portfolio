"""
Assignment 1
Rigre Garciandia

Assumptions:
    - I decided to rename the class Person detailed in the instructions to Employee for naming consistency
    - To avoid a conflict with built-in name 'id', I renamed the field in the instructions to 'emp_id'
    - If input file contains duplicate IDs, I will not ask the user to correct it, just print an error message
"""
import sys
import pathlib
import re
import pickle


class Employee:
    def __init__(self, last, first, mi, emp_id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.emp_id = emp_id
        self.phone = phone

    def display(self):
        print("Employee id:", self.emp_id)
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

        # modify phone number if necessary
        is_phone_in_dash_format = False
        while not is_phone_in_dash_format:
            dot_format_match = re.match(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{4}$', phone)  # xxx.xxx.xxxx
            space_format_match = re.match(r'^[0-9]{3}\s[0-9]{3}\s[0-9]{4}$', phone)  # xxx xxx xxxxx
            all_together_format_match = re.match(r'^[0-9]{10}$', phone)  # xxxxxxxxxx
            dash_format_match = re.match(r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$', phone)  # xxx-xxx-xxxx

            if dash_format_match:
                is_phone_in_dash_format = True
            elif dot_format_match:
                phone = re.sub(r'\.', '-', phone)
            elif space_format_match:
                phone = re.sub(r'\s', '-', phone)
            elif all_together_format_match:
                phone = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]
            else:
                print("Phone", phone, "is invalid")
                print("Enter phone number in form 123-456-7890")
                phone = input("Enter phone number:")

        if emp_id not in result:
            result[emp_id] = Employee(last, first, mi, emp_id, phone)
        else:
            print("Error: ID", emp_id, "is repeated in the input file")

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

    # Pickle the employees
    pickle.dump(employees, open('employees.pickle', 'wb'))

    # read the pickle back in
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    # output employees
    print("\n\nEmployee list:\n")
    for obj_id in employees_in.keys():
        employees_in[obj_id].display()
