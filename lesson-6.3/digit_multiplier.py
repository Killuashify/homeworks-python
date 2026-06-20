def multiply_digits_until_single(number):
    while number > 9:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product

    return number


if __name__ == "__main__":
    print("Digit Multiplier (User Input Mode)")

    while True:
        user_input = input("Enter an integer (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            num = abs(int(user_input))

            final_result = multiply_digits_until_single(num)
            print(f"Result: {user_input} -> {final_result}")
            print("-" * 40)

        except ValueError:
            print("Error: Please enter a valid integer!")
            print("-" * 40)