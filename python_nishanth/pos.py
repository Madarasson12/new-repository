# num = int(input ("Enter a number: "))
# if num>0:
#     print("The number is positive")
# elif num <0:
#     print("The number is negative")
# else:
#     print("The number is zero")  


a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")
try:
    if not (a.isnumeric()  b.isnumeric() and c.isnumeric()):
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
