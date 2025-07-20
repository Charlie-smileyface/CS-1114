
def calculate_income(hourly_rate):
    total_hour = 0
    for i in range(5):
        day_hour = int(input("Enter the number of hours worked today: "))
        total_hour += day_hour
    if total_hour > 40:
        standard_hour = 40
        overtime = (total_hour - 40) * 1.5
        total_hour = standard_hour + overtime
    income = total_hour * hourly_rate
    return income
    
def calculate_expenses():
    expense = input("Enter how much money you spent or Q if done: ")
    total_expense = 0
    while expense != "Q":
        total_expense += float(expense)
        expense = input("Enter how much money you spent or Q if done: ")
    return total_expense

def budget_outcome(income,expense):
    outcome = income - expense
    if outcome > 0:
        print(f"Well done you had a gain of {outcome}")
    elif outcome < 0:
        print(f"You had a loss of {outcome}")
        print("You got a 0 budget")

def main():
    income = calculate_income(15)
    expense = calculate_expenses()
    outcome = budget_outcome(income,expense)
main()
