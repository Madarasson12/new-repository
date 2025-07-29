def date_time():
    from datetime import datetime 
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time
 
print("do you want to check the time ? \n1. Yes\n2. No")
choice = str(input("Enter your choice: "))
if choice == yes:
    print("Current date and time:", date_time())
elif choice == no:
    print("Exiting without checking time.")
else:
     print("Invalid choice. Please enter 1 or 2.")