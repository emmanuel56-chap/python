print ("program to check the number of attendance of a student")
num_of_class = int(input("total number of classes held :"))
num_of_atten = int (input("total number of attendance:"))
per = (num_of_atten/num_of_class)* 100
if per < 75:
    print ("you cant sit for the exam", per)
else:
    print ("your exam starts now")