#Task 1: Calculator and Number Guessing Game
import random

def calculator():
    print("Enter two numbers:")
    try:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    print("Enter an operator: + - * /")
    sign = input("Operator: ")
    if(sign == "+"):
        print(f"{num1} + {num2} = {num1 + num2}")
    elif(sign == "-"):
        print(f"{num1} - {num2} = {num1 - num2}")
    elif(sign == "*"):
        print(f"{num1} * {num2} = {num1 * num2}")
    elif(sign == "/"):
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
            
def number_guessing_game():
    print("I am thinking of a number between 1 and 100 (inclusive). Try to guess it")
    number = random.randint(1,100)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        attempts += 1
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < number:
            print("Too Low, try again")
        elif guess > number:
            print("Too High, try again")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break

print("Calculator")
print("To play the calculator, enter 'calc'. To play the guessing game enter 'guess'. To exit, enter 'end'.")
while True:
    choice = input("Enter your choice: ").strip().lower()
    if choice == 'end':
        print("Exiting the calculator.")
        break
    elif choice == 'calc':
        calculator()
    elif choice == 'guess':
        number_guessing_game()
    else:
        print("Invalid choice: Select 'calc' for calculator, 'guess' for guessing game, or 'end' to exit.")