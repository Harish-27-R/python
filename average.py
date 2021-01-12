Name=(input("Enter your Name :\t"))
Mark1=int(input("Enter the mark in Subject 1:\t"))
Mark2=int(input("Enter the mark in Subject 2:\t"))
Mark3=int(input("Enter the mark in Subject 3:\t"))
Mark4=int(input("Enter the mark in Subject 4:\t"))
Mark5=int(input("Enter the mark in Subject 5:\t"))
total=Mark1+Mark2+Mark3+Mark4+Mark5
avg=total/5
print("The marks of ",Name)
print("The Mark of subject 1 is : ",Mark1)
print("The Mark of subject 2 is : ",Mark2)
print("The Mark of subject 3 is : ",Mark3)
print("The Mark of subject 4 is : ",Mark4)
print("The Mark of subject 5 is : ",Mark5)
print("The Total Marks obtained is :",total)
print("The average of your total is :",avg)
if(Mark1 or Mark2 or Mark3 or Mark4 or Mark5 <50):
    print("Result : FAIL )
    else:
    print("Result : PASS)