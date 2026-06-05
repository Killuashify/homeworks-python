def calculator():
    print("--- Simple Calculator ---")


    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Error: Please enter a valid number!")
        return


    operation = input("Enter an operation (+, -, *, /): ").strip()


    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter a valid number!")
        return


    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")

    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")

    elif operation == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")

    elif operation == '/':

        if num2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")

    else:
        print("Error: Invalid operation! Please use +, -, * or /.")



if __name__ == "__main__":
    calculator()