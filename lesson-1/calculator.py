# task_1
# number = float(input("Enter a number: "))
# # square = number ** 2
# # print("The square of", number, "is", square)

# task_2
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
#
# average = (num1 + num2 + num3) / 3
# print("The average is: ", average)

# task_3
# total_minutes = int(input("Enter the total minutes: "))
# hours = total_minutes // 60
# minutes = total_minutes % 60
#
# print(f"{hours}:{minutes}")

# task_4
# price = float(input("Enter your price: "))
# discount_pecent = float(input("Enter your discount percentage: "))
#
# final_price = price * (1 - discount_pecent / 100)
# print(f"Your final price: {final_price}")

#task 5
# number = int(input("Enter a number: "))
# last_digit = number % 10
# print(f"Last digit: {last_digit}")

# task 6
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
#
# perimeter = 2 * (length + width)
# print(f"Perimeter: {perimeter}")

#task 7
number = int(input("Enter a 4-digit number: "))

digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

print(digit1)
print(digit2)
print(digit3)
print(digit4)
