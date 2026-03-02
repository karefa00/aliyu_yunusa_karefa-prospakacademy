# Lab 1: Building a Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number entered. Please try again.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(result if isinstance(result, str) else f"{num1} / {num2} = {result}")
    else:
        print("Invalid choice. Please try again.")