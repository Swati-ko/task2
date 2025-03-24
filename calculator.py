def calculator():
    print("Welcome to the Basic Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user to choose an operation
    while True:
        try:
            choice = int(input("Enter the number corresponding to the operation (1-4): "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

    # Input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Perform the chosen operation
    if choice == 1:
        print(f"The result of {num1} + {num2} is {num1 + num2}")
    elif choice == 2:
        print(f"The result of {num1} - {num2} is {num1 - num2}")
    elif choice == 3:
        print(f"The result of {num1} * {num2} is {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"The result of {num1} / {num2} is {num1 / num2}")
        else:
            print("Division by zero is undefined.")

# Run the calculator
calculator()
