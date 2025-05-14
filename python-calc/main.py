import calculator

def main():
    print("Simple Python Calculator")
    print("Select operation: +, -, *, /")
    operation = input("Enter operation: ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == '+':
        result = calculator.add(a, b)
    elif operation == '-':
        result = calculator.sub(a, b)
    elif operation == '*':
        result = calculator.mul(a, b)
    elif operation == '/':
        result = calculator.div(a, b)
    else:
        result = "❌ Invalid operation"

    print("Result:", result)

if __name__ == "__main__":
    main()
