#number checking

print("\thighest number checker v1.0\nhello user")  

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
if num1 > num2:
    print(f"{num1} is larger than {num2}.")
elif num2 > num1:
     print(f"{num2} is larger than {num1}.")
elif num1 == num2:
    print("both of the numbers are equal.")
else:
     print("\tinvalid input\nenter an integer.")