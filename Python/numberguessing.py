import random
print("Welcome to the Number Guessing Game. The computer has chosen a number within range 100, you have to guess it!")
choice=input("Choose your difficulty level? (hard/easy): ")
guess=0
num=random.randint(1,101)
def guess_number(num):
    if choice=="easy":
      attempts=10
      while attempts!=0:
        guess=int(input("Enter your guess: "))
        if guess>num:
          attempts-=1
          print(f"Too high, you have {attempts} attempts left")         
        elif guess<num:
          attempts-=1
          print(f"Too low, you have {attempts} attempts left")         
        elif guess==num:
          print("Congrats! You have guessed it!")
          break
    elif choice=="hard":
      attempts=5
      while attempts!=0:
        guess=int(input("Enter your guess: "))
        if guess>num:
          attempts-=1
          print(f"Too high, you have {attempts} attempts left")         
        elif guess<num:
          attempts-=1
          print(f"Too low, you have {attempts} attempts left")         
        elif guess==num:
          print("Congrats! You have guessed it!")
          break
num=random.randint(1,101)
guess_number(num)