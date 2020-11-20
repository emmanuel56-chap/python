#workm,sex,male,female

print("\tjob checker v1.0\nhello user")

name = input("what is your name?: ")
gender = input("what is your gender?: ")
marital_status = input("what is your marital_status  ?: ")
if gender.lower() == "male" or gender.lower() == "m":
    age = int(input(f"{name} enter your age: "))
    if age >= 20 and age <= 40:
        print(f"{name}, you can work in both urban and rural areas.")
    elif age >= 40 and age<= 60:
         print(f"{name}, you can only work in urban areas.")
    else:
         print("you are not qualified for this service.")
elif gender.lower() == "female" or gender.lower() == "f":
    age = int(input(f"{name} enter your age: "))
    print(f"{name}, you would be working in urban areas.")
else:
    print("invalid input\nenter either (male\m) or (female\f)")


 


