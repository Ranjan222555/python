# this is advance python

'''
# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)


if (n := len([21,121,1,23,]))< 111:  # ":=" its a walrus operater 
    print(f"list is {n}")
'''

#  Types
'''
n: int = 3
name : str= "ranjan"

def sum(a:int, b:int)-> int:
    return a+b
print(sum(22, 11))
'''
'''
def greet(name:str)-> str:
    return f"Good morning {name}!"

print(greet("ranjan!!"))
'''
# advance type

from typing import List, Tuple, Dict, Union

'''
number: list[int] =[21, 2212, 12,1 , 2, 2,212, 12]
print(number)
'''
'''
person :tuple[str, int] = ("ranjan", 24)
print(person)
'''
'''
ident : Union[int, str]= "hello 324"
ident = 12121
print(ident)
'''

# match case
'''
def http_status(status):
        match status:
            case 200:
                return "OK"
            case 404:
                return "Not Found"
            case 500:
                return "Internal Server Error"
            case _:
                return "Unknown status"

print(http_status(500)) 
'''
 # DICTIONARY MERGE & UPDATE OPERATORS
'''
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merge = dict1 | dict2
print(merge)
# Output: {'a': 1, 'b': 3, 'c': 4}
'''
# multiple context manager with statement
'''
with(    open("poem.txt") as f1,
          open ("my.txt") as f2
    ):
    print(f1.read(), f2.read())
'''
# exception handeling 
'''
try:
    a = int(input("Enter a number: "))
    print (a)
    
except ValueError as v:
    print(v)
    print("this is value error")   
    
except TypeError as t:
    print(t)
    print("this is type error")     
    
except Exception as b:
    print(b)
    print("please try a valid num")
'''
# raising execption 
'''
try:
    a = int(input("enter a number: "))
    b = int(input("enter b number: "))

    print(f"the division of a/b is {a/b}")
    
except ZeroDivisionError as z:
    print(z)
    # print("this a division error")
'''
# another way
'''
a = int(input("enter a number: "))
b = int(input("enter b number: "))

if (b==0):
    raise ZeroDivisionError ("this is division error")
else:
    print(f"the division of a/b is {a/b}")
'''
# try else statement
'''
try:
    a = int(input("Enter a number: "))
    print (a)
except Exception as b:
    print(b)
else:                       # this else will be print if try  sucessfully run
    print("this is else ")
'''
# try finally statement
'''
try:
    a = int(input("Enter a number: "))
    print (a)
except Exception as b:
    print(b)
finally:                            # finally will breake all boundary and run 
    print("this is finally ")       # it compulsory have to run
'''
 # use function 
'''
def main():
    try:
        a = int(input("Enter a number: "))
        print (a)
        return
    except Exception as b:
        print(b)
        return
    finally:                          # if finally usen inside the function it can over write the return
        print("this is finally ")       # simply finally break all rules and it compulsory
        
main()        
'''
# if __name__ == "__main__" 
'''
def goodday():
    print("good day")
    
if __name__ == "__main__"  :
    print("directly running this code ")      
    goodday()
    print(__name__)
''' 
# global 

'''
a= 3232
def fun():
    global a         # global is use to local variable and global also
    a= 3
    print(a)
fun()
print(a)
'''
 #  ENUMERATE FUNCTION

'''
l = [13, 32, 43, 223]

index =0
for item in l:
    print(f"the item is {index} is {item}")
    index +=1
# output
the index is 0 is 13
the index is 1 is 32
the index is 2 is 43
the index is 3 is 223 
'''
 
#  same work using enumerate function
'''
for item, index in enumerate(l):
    print(f"the item is {index} is {item}")
# out put 
the item is 13 is 0
the item is 32 is 1
the item is 43 is 2
the item is 223 is 3
'''
'''
for index,item in enumerate(l):
    print(f"the item is {index} is {item}")
# out put  
the item is 0 is 13
the item is 1 is 32
the item is 2 is 43
the item is 3 is 223
'''

# List Comprehension
'''
lis= [1,23,22,19, 2, 5, 3, 7]
squrelist=[]
for item in lis :
    squrelist.append(item*item)
print(squrelist)
'''
# same work here
'''
squrelist=[ i*i for i in lis ]
print(squrelist)
# out put 
[1, 529, 484, 361, 4, 25, 9, 49]
'''

