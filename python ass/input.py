first = input ("enter first age")
second = input ("enter second age")
third = input ("rnter third age")
if first >= second and first >= third:
    print ("oldest is first")
if second >= first and second >= third:
    print ("oldest is second")
if third >= first and third >= second:
    print ("oldest is third")
else:
    print ("all are equal")