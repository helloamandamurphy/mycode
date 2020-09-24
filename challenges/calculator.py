#!/usr/bin/env python3

def calc(a, b, operator):
    a = float(a)
    b = float(b)

    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "/":
        print(a / b)
    elif operator == "*":
        print(a * b)
    else:
        print("You broke my brain. Time to buy a new calculator.")


def promptUser():
    print("I will be your trusty calculator.")
    print("What would you like to calculate today friend?")
    a = input("What's the first number?")
    print("Enter + for addition.")
    print("Enter - for subtraction.")
    print("Enter / for division.")
    print("Enter * for multiplication.")
    operator = input("What would you like to do with this number?")
    b = input("What's the second number?")
    print("Thanks for your input. Let me think about it.")
    calc(a, b, operator)

if __name__ == "__main__":
    promptUser()










