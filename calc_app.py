
import os

# Function to perform calculation
def perform_calculation():
    try:
        # Input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")

        # Perform the calculation based on the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operation. Please choose +, -, *, or /.")
            return

        # Display the result
        equation = f"{num1} {operation} {num2} = {result}"
        print(equation)

        # Save the result in equations.txt
        with open("equations.txt", "a") as file:
            file.write(equation + "\n")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

# Function to print previous equations
def print_previous_equations():
    # Check if the file exists
    if os.path.exists("equations.txt"):
        with open("equations.txt", "r") as file:
            equations = file.readlines()
            if equations:
                print("Previous equations:")
                for equation in equations:
                    print(equation.strip())
            else:
                print("No previous equations found.")
    else:
        print("No previous equations file found.")

# Function to handle user input
def main():
    while True:
        print("\nSimple Calculator")
        print("1. Perform a calculation")
        print("2. Print previous calculations")
        print("3. Exit")

        try:
            choice = int(input("Choose an option (1, 2, or 3): "))

            if choice == 1:
                perform_calculation()
            elif choice == 2:
                print_previous_equations()
            elif choice == 3:
                print("Exiting the program.")
                break
            else:
                print("Error: Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Error: Invalid input. Please enter a number (1, 2, or 3).")

# Run the calculator application
if __name__ == "__main__":
    main()
