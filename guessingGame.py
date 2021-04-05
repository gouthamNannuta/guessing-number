
import random
randnum=random.randint(1, 9)

chances=0
print(chances)
while chances < 5: 
    guess=int(input("Enter your guessing number between(0-10) : "))
    number=randnum

    if guess == number:
       print("Congratulation YOU WON!!!")
       break
    elif guess != number:
        if guess < number:
            print("your guess is lower than the number ")
        elif guess>number:
            print("your guess is more than the number")
    chances=chances+1
else:
     if not chances < 5:
         if guess != number:
            print("YOU LOSE!!! The number is : ",number)


