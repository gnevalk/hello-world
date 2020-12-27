sayac=0
while sayac!=4:
    sayac+=1 

    a="Neval Kılınç"
    b=input("enter your first name and last name: ")

    if b==a:
      print("Welcome", a)
      break
    elif b!=a and sayac==4:
      print("please try again later")
      break
    elif b!=a:
      print("incorrect entry")
      continue

def choice():
    
    lessons=["1-Java", "2-Python", "3-C++", "4-Deep Learning", "5-Machine Learning"]
    print("Lessons:", lessons, "\n", "you have to choese at least 3 lessons and you can choose up to 5 lessons")
    x=int(input("how many lessons will you choice:"))
    if x==1 or x==2:
      return "you failed in class"
    elif x>5:
      return "you can choise at most 5 lessons"
    else:
      return "you should choice the lesson you'll enter exam"

print(choice())


z=input("your choice: ")
print("Now, please you enter the grades you took from this lesson")
     

c=int(input("enter your midterm grade:"))
d=int(input("enter your final grade:"))
e=int(input("enter your project grade:"))
grades={"midterm":c, "final":d, "project":e}
print("your grades:", grades)

passgrade= (c*0.3) + (d*0.5) + (e*0.2)
print("your passing grade:", passgrade)
if passgrade>90:
    print("you passed with AA")
elif 70<passgrade<90:
    print("you passes with BB")
elif 50<passgrade<70:
    print("you passes with CC")
elif 30<passgrade<50:
    print("you passes with DD")
elif passgrade<30:
    print("you failed with FF")


    