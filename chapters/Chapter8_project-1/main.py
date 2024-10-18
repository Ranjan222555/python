import random

'''
1 for snake 
0 for gun
-1 for water

'''
computer= random.choice( [1, 0, -1])

your_input=input("Enter your choice: ")
your_dict={
    "s":1,
    "g": 0,
    "w": -1
}
revers_disct={
    1: "snake",
    0: "gun",
    -1: "water"
}

you_chose= your_dict[your_input]

print(f"You chose: {revers_disct[you_chose]}\nComputer chose: {revers_disct[computer]}")

if (computer==you_chose):
    print("its Draw!")
else:
    '''
    # its a shorter form of code 
    
    if ((computer - you_chose)== -1 or (computer - you_chose)== 2):
        print("You Lose!")
    else:
        print("you Win!")
    
    '''
      
    if (computer==-1 and you_chose==1):
        print("You Win!")
        
    elif (computer==-1 and you_chose==0):
        print("You Lose!")
        
    elif (computer==1 and you_chose==-1):
        print("You Lose!")
        
    elif (computer==1 and you_chose==0):
        print("You Win!")
        
    elif (computer==0 and you_chose==1):
        print("You Win!")
        
    elif (computer==0 and you_chose==-1):
        print("You Lose!")
        
    else:
        print("something wrong")

