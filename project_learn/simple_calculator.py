def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate(operation, a, b):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    return operations[operation](a, b)


operation = input("Enter an operation (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculate(operation, num1, num2)
print("Result:", result)
