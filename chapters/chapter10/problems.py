# problem-1
'''
class programers:
    work = "microsoft"

    def __init__(self, name , sal, lan):
        self.name = name
        self.lan =lan
        self.sal = sal

ranjan = programers("ranjan", "react", 1500000)
print(ranjan.work,ranjan.lan, ranjan.sal, ranjan.name )

sipun = programers("sipun", "javascript", 1200000)
print(sipun.work,sipun.lan, sipun.sal, sipun.name )
'''
# problem-2
'''
class calculater:
    def __init__(self, n):
        self.n = n
        
    def squre(self):
        print(f"squre of {self.n} is : {self.n*self.n} ")
        
    def cube (self):
        print(f"cube of {self.n} is : {self.n*self.n*self.n} ")
        
    def root(self):
        print(f"root of {self.n} is : {self.n**1/2} ")
             
c = calculater(4)
c.squre()
c.cube()
c.root()
'''

# problem-3
'''
 #class attribute is change
class demo :
    a= 2
at = demo()
print(at.a)
at.a = 0
print(at.a)
 
# ans is : class attribute not change
'''
# problem-4
'''
# use static method
class calculater:
    def __init__(self, n):
        self.n = n
    
    @staticmethod    
    def greet():
        print("good morning all")
    
    def squre(self):
        print(f"squre of {self.n} is : {self.n*self.n} ")
        
    def cube (self):
        print(f"cube of {self.n} is : {self.n*self.n*self.n} ")
        
    def root(self):
        print(f"root of {self.n} is : {self.n**1/2} ")
             
c = calculater(4)
c.greet()
c.squre()
c.cube()
c.root()
'''
# problem-5
'''
from random import randint  # import random is also same 

class train:
    
    def __init__(self, trainNo ):
        self.trainNo = trainNo
         
    def book(self, fro ,to ):
        print(f"Train{self.trainNo} is book {fro} to {to} is conform")
        
    def getStatus(self):
        print(f"Train {self.trainNo} is running  on time")
        
    def getFare(self):
        print(f"Train{self.trainNo} booking done: {randint(500, 5000)}")
        
t =train(" 756002") 
t.book("balasore", "pune")  
t.getStatus()
t.getFare() 

outPut
Train 756002 is book balasore to pune is conform
Train  756002 is running  on time
Train 756002 booking done: 3684
'''
# problem-6
'''
self insted of slf can use 

'''
