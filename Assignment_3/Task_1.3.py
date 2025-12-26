# Task 1: Calculate Factorial Using a Function

num = int(input("Enter a number: "))

# Defining the function:
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(f"\nFactorial of {num} is: {factorial(num)}")

        

