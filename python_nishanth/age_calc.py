
def age_calc():
    from datetime import datetime 
    current_year = datetime.now().year
    age = current_year - int(user_year)
    current_month = datetime.now().month
    month_1 = current_month - int(user_month)  

    current_day = datetime.now().day
    day_1 = current_day - int(user_day)


    return age
user_input = str(input("Enter your year of birth:dd/mm/yyyy "))
user_day = user_input[0:1]
user_month = user_input[3:5]
user_year = user_input[6:11]
int= month
age= age_calc()
print(f"you are {age} years old and {month_1} months and {day_1} days old")