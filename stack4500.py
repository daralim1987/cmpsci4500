# Author: Logan Pettit, Dara Lim
# Date: September 19, 2019
# Class: CS 4500 section 002
# Description: This program implents a stack using a python list structure. The menu prompts the user to start entering
# only characters into the stack. If the stack is empty the user will not be able to view or pop from the stack.
import turtle

stack = []
print("************Welcome to Stack Data Type**************")
print()
flag = True
y = 0

rectangle = turtle.Turtle()

while flag:
    choice = input("""
            A: Pop the item out of Stack
            B: Push the item onto the Stack
            C: View stack
            D: See top of stack
            E: Exit program
    
            Please enter your choice: """)

    if choice == "A" or choice == "a":

        if len(stack) != 0:
            print("\nYour stack is:")
            stack.pop()
            rectangle.begin_fill()
            rectangle.pencolor("white")
            rectangle.forward(10)
            rectangle.right(90)
            rectangle.forward(30)
            rectangle.right(90)
            rectangle.forward(30)
            rectangle.right(90)
            rectangle.forward(30)
            rectangle.right(90)
            rectangle.forward(30)
            rectangle.penup()
            rectangle.back(10)
            y -= 30
            rectangle.sety(y)
            rectangle.pendown()
            rectangle.color("white")
            rectangle.end_fill()

            print(stack)
        else:
            print("\nError: your stack is empty, please push characters into stack.")

    elif choice == "B" or choice == "b":
        characters = input("\nEnter your input")
        if characters.isalpha():
            stack.append(characters)
            print(stack)
            rectangle.pencolor("black")
            rectangle.write(characters, False, "center", ("Arial", 24, "normal"))
            rectangle.penup()
            y += 30
            rectangle.sety(y)
            rectangle.pendown()
        else:
            print("\nThe input is not a character")

    elif choice == "C" or choice == "c":
        if len(stack) != 0:
            print("\nOur stack is: ")
            print(stack)
            for i in stack:
                rectangle.write(i, False, "center", ("Arial", 24, "normal"))

        else:
            print("\nError: your stack is empty, please push characters into stack.")

    elif choice == "D" or choice == "d":
        if len(stack) != 0:
            print("The top of the stack is: ")
            length = len(stack)
            print(stack[length - 1])
        else:
            print("\nError: your stack is empty, please push characters into stack.")

    elif choice == "E" or choice == "e":
        print("\nProgram is exiting")
        flag = False

    else:
        print("\nYou must only select either A, B or C")
        print("\nPlease try again")

