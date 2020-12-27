name=input("enter your first name:")
lname=input("enter your last name:")
age=int(input("enter your age:"))
dob=int(input("enter your year of birth:"))
liste=[name, lname, age, dob]

for i in liste[0:4]:
    print(i)
    
if age<18:
    print("you can't go out because it's too dangerous")
if age>18:
    print("you can go out to the street")
