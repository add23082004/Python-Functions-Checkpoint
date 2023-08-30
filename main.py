def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = float(input("Enter the first number: "))
    should_continue = True

    while should_continue:
        print("Available operation symbols:")
        for symbol in operations.keys():
            print(symbol)

        operation_symbol = input("Select an operation symbol (+, -, *, /) or 'end' to exit: ")

        if operation_symbol == 'end':
            print("Exiting the calculator.")
            break

        if operation_symbol in operations:
            num2 = float(input("Enter the second number: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            use_answer = input("Do you want to use the answer for the next calculation? (yes/no): ")
            if use_answer.lower() == 'yes':
                num1 = answer
            else:
                should_continue = False
                calculator()  # Start a new calculation
        else:
            print("Invalid operation symbol. Please choose from +, -, *, /.")


# Call the calculator function to start the calculation
calculator()
