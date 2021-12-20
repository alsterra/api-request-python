from helper import validate_and_execute, user_input_message
# or from helper import *
# or import helper as h

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dict)
    validate_and_execute(days_and_unit_dict)
