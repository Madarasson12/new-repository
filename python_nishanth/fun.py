
def calc():
    try:
        num1 = input("Enter first number: ")
        opp = input("Enter the operator ")
        num2 = input("Enter second number: ")
       

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

def comp():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    c = input("Enter third number: ")
    try:
     if not (a.isnumeric() and b.isnumeric() and c.isnumeric()):
            raise ValueError("Input must be numeric")
     else:
            if a >= b and a >= c:
                print("The biggest number is:", a)
            elif b >= a and b >= c:
                print("The biggest number is:", b)
            else:
                print("The biggest number is:", c)  
    except Exception as e:
        print("An error occurred:", e)
val= int(input("wat you need me to do ?\n---type the number to select--- \n1. Calculator\n2. Compare numbers\n0. Exit\nEnter your choice: "))
if val == 1:
    calc()
elif val == 2:
    comp()
elif val == 0:
   print("exiting program .......")
else :
    print("Invalid choice, please try again.")