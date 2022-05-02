employeeName = "Claudia Evans"
hourlyWage = 11.0
hoursWorked = 51

def weeklyPay(hourlyWage, hoursWorked):
    return hourlyWage * hoursWorked

print(f"Employee: {employeeName} paycheck for week is {weeklyPay(hourlyWage, hoursWorked):,.2f}")

hourlyPay = float(input("What is the employee's hourly rate? "))
print(hourlyPay)