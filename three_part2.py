# Get user input and convert it to an integer.
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

# Try dividing the 2 numbers.
try: 
    answer = num1 / num2
    print(f"Answer: {answer}")

# Print an error where the number to be divided with is zero.
except ZeroDivisionError:
    print('Error: Cannot divide by zero.')