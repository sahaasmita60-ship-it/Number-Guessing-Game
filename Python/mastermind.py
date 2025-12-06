import random
no=random.randint(1000,10000)
n1=list(str((no)))
no2=(input("The computer has chosen a 4-digit number, let's try to guess it. Guess the number: "))
n2=list(no2)
n3=""
n4=[]
if(no==no2):
    print("Congrats! You are a mastermind")
else:
    pass
t1=0
t2=0
for i in range(0,4):
    if(n1[i]==n2[i]):
        n3=n3.join(n2[i])
        t1=1
        t2+=1
    else:
        n3=n3.join("X")
    if(t1==1):
        print(f"You have guessed {t2} digits")
        print(n3)

 