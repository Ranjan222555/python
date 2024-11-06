
'''
import random

n= random.randint(1,100)
a= -1
guess= 0
while(a != n):
    guess +=1
    a= int(input("Guess the number: "))
    print(f"This is the number= {n} you have to guess")
    if (a>n):
        print("Lower num please!")
    else:
        print("Higher num please!")

print (f" congratulation!!! you have gussed the {n} number in {guess} attempt")
'''