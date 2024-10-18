
# problem-1

'''
def numbers(a,b,c):
    if(a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>b and c>a):
        return c
a=23
b=22
c=121

print(numbers(a,b,c))
'''
# problem-2  convert Celsius to Fahrenheit
'''
formula for Celsius to Fahrenheit

c/5 =(f-32)/9

c = 5*(f-32)/9
'''

'''
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in Fahrenheit: "))
print(f_to_c(f))
'''

'''
def f_to_c(f):
    return (5/9) * (f - 32)

f = int(input("Enter temperature in Fahrenheit: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")


def c_to_f(c):
    return (9/5) * c + 32

c = int(input("Enter temperature in Celsius: "))
f = c_to_f(c)
print(f"{round(f, 2)}°F")
    
'''
'''
# c/5 =(f-32)/9
c=(5/9)*(f-32)
f=(9/5)*(c+32)

'''
# Fahrenheit to Fahrenheit
'''
def c_to_f(c):
    return 9/5*(c+32)

c=int(input("enter any num: "))
d=c_to_f(c)

print(f"your reselt is : {(d)}°F")

'''
# problem-3  print() function to not print a new line at the end.
'''
print("a")
print("f",end=" ")
print("3")
print("v")
'''

# problem-4
'''
def rec_fun(n):
    if n==1:
        return 1
    else:
       return n + rec_fun(n-1)
   
print(rec_fun(5))
   
    
# n=int(input("enter any num: "))
# result=rec_fun(n)
# print(f"here the {n} is the res: {result}")

'''

# problem-5 star pattern
# using for loop
'''
def star_pattern(n):
    for i in range(n,0,-1):
        print("*"* i)

n= int(input("neter: "))
star_pattern(n)
'''
# using recursion
'''
***
**
*
'''
'''
def star_pattern(n):
    if (n==0):
        return
   # print("")      # tacking space in between 
   # print("", end="")   # between space removed
    print("*" * n)
    star_pattern(n-1)

    
star_pattern(3)
'''

# problem-6
# converts inches to cms.
'''
def converter(n):
    return (n * 2.54)

n=int(input("enter : "))
print(converter(n))
'''
'''
def converter(n):
    return (n * 2.54)

n=int(input("enter: "))
res=converter(n)
print(f" {n} inch is:{res} cm")
'''
# converts cm to inch.
'''
def converter(n):
    return (n / 2.54)

n=int(input("enter: "))
res=converter(n)
print(f" {n} cm is:{round(res,2)} inch")
'''

# problem-7

# remove some words in list
'''
lis=["ranjan", "ran", "sipun", "sipu", "raj"]

def remove_word(lis,word ):
    for item in lis:
        lis.remove(word)
        return lis

print(remove_word(lis, "ran"))

'''
# strip words 
'''
def remmpve_words(lis, word):
    n=[]
    for item in lis:
        if not (item ==word):
            n.append(item.strip(word))
    return n

lis=["ranjan","sipun", "hay", "raaj"]

print(remmpve_words(lis, "ra"))
'''
# problem-8
# multification using fumction
'''
def multi(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
        
multi(4)
'''
