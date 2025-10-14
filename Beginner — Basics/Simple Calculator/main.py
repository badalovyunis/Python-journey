def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num == 0:
            return "Error"
        return num1/num2
    else:
        return "You input wrong operator! (+, -, *, /)"

def main():
    print("=== Simple Calculator ===")

    try:
        num1 = float(input("Input first number: "))
        operator = input("Input operator: ")
        num2 = float(input("Input second number: "))

        result = calculate(num1, num2, operator)
        print("Result: ", result)

    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()