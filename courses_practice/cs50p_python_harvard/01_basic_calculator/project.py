"""
PROJECT TITLE: SIMPLE OPERATIONS BETWEEN TWO NUMBERS

PERSONAL DETAILS:
Name: Elisei
Country: Romania
City: Brașov

DESCRIPTION: This is a simple calculator who perform addition, substraction,
multiplication and division between two numbers. If you try to enter a string,
an error message will appear with instruction. The program will perform
as many operations as you need, until you choose the option from the menu
who stops the program.

VIDEO DEMO: https://youtu.be/SNUhBZeEEbk

THANK YOU FOR EVERYTHING!
"""

def add(a, b):
    try:
        return a + b
    except:
        return "ERROR: Not a valid number. Try again!"

def sub(a, b):
    try:
        return a - b
    except:
        return "ERROR: Not a valid number. Try again!"

def mul(a, b):
    try:
        return a * b
    except:
        return "ERROR: Not a valid number. Try again!"

def div(a, b):
    if b == 0:
        return "You cannot divide by 0."
    else:
        try:
            return a / b
        except:
            return "ERROR: Not a valid number. Try again!"

def main():
    print("-----------------------------------")
    print("Simple calculator between 2 numbers")
    print("")
    print("Choose the operation:")
    print("")
    while True:
        print("[1] Addition")
        print("[2] Substraction")
        print("[3] Multiplication")
        print("[4] Division")
        print("[0] STOP DE PROGRAM")
        print("")
        choice = input("Insert your choice (1/2/3/4/0): ")
        print("")
        if choice == '1':
            print("ADDITION")
            try:
                num1 = float(input("Insert the first number: "))
                num2 = float(input("Insert the second number: "))
                print("")
                print(f"--- RESULT: {num1} + {num2} =", add(num1, num2))
                print("")
            except:
                print("")
                print("ERROR: Not a valid number. Try again!")
                print("")
        elif choice == '2':
            print("SUBSTRACTION")
            try:
                num1 = float(input("Insert the first number: "))
                num2 = float(input("Insert the second number: "))
                print(f"--- RESULT: {num1} - {num2} =", sub(num1, num2))
                print("")
            except:
                print("")
                print("ERROR: Not a valid number. Try again!")
                print("")
        elif choice == '3':
            print("MULTIPLICATION")
            try:
                num1 = float(input("Insert the first number: "))
                num2 = float(input("Insert the second number: "))
                print(f"--- RESULT: {num1} * {num2} =", mul(num1, num2))
                print("")
            except:
                print("")
                print("ERROR: Not a valid number. Try again!")
                print("")
        elif choice == '4':
            print("DIVISION")
            try:
                num1 = float(input("Insert the first number: "))
                num2 = float(input("Insert the second number: "))
                if num2 == 0.0:
                    print("")
                    print("ERROR: You cannot divide by 0.")
                else:
                    print(f"--- RESULT: {num1} / {num2} =", div(num1, num2))
                print("")
            except:
                print("")
                print("ERROR: Not a valid number. Try again!")
                print("")
        elif choice == '0':
            print("Thank you for using my program!")
            print("-----------------------------------")
            break
        else:
            print("Invalid option")
            print("")

if __name__ == "__main__":
    main()