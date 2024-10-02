import operator

# Dictionary mapping supported operations to functions
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(expression):
    """
    Parses and evaluates a basic arithmetic expression.
    :param expression: str, an arithmetic expression (e.g., "2 + 3")
    :return: float or int, result of the expression
    :raises: ValueError if the input is invalid
             ZeroDivisionError if division by zero occurs
    """
    try:
        # Split the expression into parts (operand1, operator, operand2)
        parts = expression.split()
        if len(parts) != 3:
            raise ValueError("Invalid input format. Use format: <operand> <operator> <operand>")

        operand1, operator_symbol, operand2 = parts
        
        # Convert operands to float
        operand1 = float(operand1)
        operand2 = float(operand2)
        
        # Get the corresponding operation function
        if operator_symbol not in operations:
            raise ValueError(f"Unsupported operator: {operator_symbol}")

        operation_func = operations[operator_symbol]

        # Perform the calculation
        result = operation_func(operand1, operand2)

        return result
    
    except ValueError as ve:
        raise ValueError(f"Input error: {ve}")
    
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed.")

def run_calculator():
    """
    Command-line interface for the text calculator.
    Continuously prompts the user for input until they exit.
    """
    print("Simple Text Calculator")
    print("Supported operations: +, -, *, /")
    print("Input expression in the format: <operand1> <operator> <operand2>")
    print("Type 'exit' to quit.")

    while True:
        expression = input("\nEnter an expression: ").strip()

        if expression.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        try:
            result = calculate(expression)
            print(f"Result: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_calculator()
