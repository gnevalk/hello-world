a=input("enter your name: ")
print("hello", a, "\n" "let's play a game, you try to find the number i kept in my memory")

sayac=0
while sayac!=6:
    sayac+=1
    
    b=int(input("you have 6 chance, let's enter a number between 1 and 20:"))
    if b<1 or b>20:
     print("invalid value")
     continue
    elif b==10:
     print("you win!! Congratulations")
     break
    elif b!=10 and sayac==6:
     print("You lost the game. The number was 7")
     break
    elif b>=15:
     print("enter a smaller number")
     continue
    elif b<=5:
     print("enter a larger number")
     continue
    elif 5<b<15:
     print("you come closer")
     continue


    