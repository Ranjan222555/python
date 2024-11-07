
# Function defination
'''
def fun():
    a =int(input("enter numb: "))
    b =int(input("enter numb: "))
    c =int(input("enter numb: "))
    
    average=(a+b+c)/3
    print(f"{average}")
    # print(average)
    '''
# Function call
'''   
fun()
print("thanks")
    
fun()
print("thanks")
    
fun()
'''
# quick quizz
'''
def goodday():
    print("good Days")
goodday()

# name with greet

def fun():
    a=input("enter name: ")
    print(a,"good morning")

fun()
'''

# Function with arrgument
'''
def goodday(name,enddd):
    print("good Day " + name)  # for concatinent you can add "+" or "," for adding.
    print(enddd)
    
goodday("Ranjan", "thanks")  # For Fun() call you can't add "+" use only "," for adding. 
goodday("sipun", "thanks")
goodday("Raaaj", "thanks")
'''

# Function with return value
'''
def goodday(name,enddd):
    print("good Day " + name)
    print(enddd)
    return "thanks"

new = goodday("Ranjan", "you are great ")
print(new)
'''
# Function with deafult
'''
def goodday(name, enddd="you are great "):
    print(f"good Day, {name}")
    print(enddd)

goodday("Ranjan", "ok great")
goodday("sipun")
'''
'''
def goodday(enddd="you are great "):
    print(enddd)

goodday() #you are great              
goodday("hay") # hay
'''


# RECURSION

'''
factorial(0)= 1
factorial(1)= 1
factorial(2)= 2x1
factorial(3)= x3x2x1
factorial(4)= 4x3x2x1
factorial(5)= 5x4x3x2x1
factorial(n)= nx(n-1)x........5x4x3x2x1


factorial(n)= n x factorial(n-1)

'''
'''
def factorial(n):
    if (n==1)or(n==0):
        return 1
    return n* factorial(n-1)

n= int(input("enter any number: "))
print(f"factorial of this: {factorial(n)}")
'''
                