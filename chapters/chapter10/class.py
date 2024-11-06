
# basic class and object
'''
class employe:
    lan = "py"  # this is class attribute
    salary =200000
    
ranjan =employe() # ranjan is a object
ranjan.name ="ranjan"   # name can add instance here ( this is instance attribute)
print( ranjan.lan, ranjan.salary, ranjan.name)   

sipun =employe() 
sipun.name= "sipun"   
print( sipun.name, sipun.lan, sipun.salary)   
'''
# class attribute vs instance attribute
'''
class employe:
    lan = "py"  
    salary =200000

ranjan =employe()
ranjan.lan = "javascript"
print(ranjan.lan, ranjan.salary) # lan take instance attribute first then class 
'''
# using methods
# self method
'''
class employe:
    lan = "python"  
    salary =200000
    
    def getemploye(self):
        print(f"lang is {self.lan} and salary is {self.salary}")  
         
    @staticmethod     # its a static method dont need object 
    def greet():
        print(f"good morning {ranjan.name} ")

ranjan =employe()
# ranjan.lan = "javascript"
ranjan.name ="ranjan"
ranjan.greet()
ranjan.getemploye()
# employe.getemploye(ranjan)  # both are same
'''

# constructor 
'''
class employe:
    lan = "python"  
    salary =200000
    
    def __init__(self, name , salary, lan):  # dunder method its auto call
       self.name =name
       self.salary =salary
       self.lan =lan
    print("hello there")
    
    def getemploye(self):
        print(f"lang is {self.lan} and salary is {self.salary}")  
         
    @staticmethod    
    def greet():
        print(f"good morning {ranjan.name} ")

ranjan =employe("ranjan", 250000, "react")

# ranjan.name ="ranjan"
print(ranjan.name,ranjan.lan, ranjan.salary)
'''