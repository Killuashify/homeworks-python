def run_calculator():
    print("Smart Calculator Started")

    while True:
        try:

            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1 / num2
            else:
                print("Error: Invalid operation!")
                continue

            print(f"Result: {num1} {operation} {num2} = {result}")

        except ValueError:
            print("Error: Please enter valid numbers!")
            continue

        user_choice = input("\nDo you want to continue? (yes/y to continue): ").strip().lower()
        if user_choice not in ['yes', 'y']:
            print("Thank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    run_calculator()