# WAGES AND HOURLY PAID

print("This program will calculate your wages at rate 60$ per hour")

name = input("Enter your name: ")
hours_worked = int(input("Enter the number of hours worked: "))
hourly_pay = 60

wages = hours_worked * hourly_pay

int(f"Your wages for {hours_worked} hours is ${wages}")