try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    opp = input("Enter an operator ")

    if not (num1.isnumeric() and num2.isnumeric()):
        raise ValueError("Inputs must be numeric")

    num1 = int(num1)
    num2 = int(num2)

    match opp:
        case "+" | "add" | "plus":
            result = num1 + num2
        case "-" | "sub"| "minus":
            result = num1 - num2
        case "*" |"mul"| "multiply" :
            result = num1 * num2
        case "/"   | "div"| "divide" :
            if num2 != 0:
                result = num1 / num2
            else:
                raise ValueError("Cannot divide by zero")
        case _:
            raise ValueError("Invalid operator")

    print("The result is:", result)
except Exception as e:
    print("An error occurred:", e)  
    