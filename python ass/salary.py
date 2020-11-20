#salary earner

print("\tNet salary checker v1.0\nhello user")  

name = input("what is your name?: ")
salary = float(input(f"{name}, enter your salary: "))
year = int(input(f"{name}, how many years have you worked in this company?: "))
net_salary = ((0.08)*salary)+salary
if year >= 8:
    print(f"{name}, we are giving you an intrest of 5%\nyour net salary will be {net_salary}.")
else:
    print(f"{name}, your salary remains {salary}.")
