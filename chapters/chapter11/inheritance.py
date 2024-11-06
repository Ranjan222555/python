# inheritance
'''
class employ:
    company = "ITC"
    name = "ranjan"
    salary  = 1200000
    def show(self):
        print(f"this is the {self.salary} and this is the {self.name}")

# class programer:
#     company = "ITC infotech"
    
#     def show(self):
#         print(f"this is the {self.salary} and this is the {self.name}")
        
#     def showlang(self):
#         print(f"this is the {self.lang} and this is the {self.name}")
      
        
# inharitance

class programer(employ):     #  htis is called inherited class
    company = "ITC infotech"
    lang = "python"
    def showlang(self ):
        print(f"this is the {self.lang} and this is the {self.name}")    
            
a =employ()
b =programer()
b.show()
b.showlang()
'''

# Multiple inheritance
'''
class employ:
    company = "ITC"
    name = "ranjan"
    salary  = 1200000
    def show(self):
        print(f"this is the salary {self.salary} and this is the name {self.name}")

class coder:
    langauge ="python"
    def showLangauge(self):
        print(f"this is the langauge {self.langauge} ")


class programer(employ, coder):   # this is the multiple inheritance
    company = "ITC infotech"
    def showlang(self ):
        print(f"this is the langauge {self.langauge} and this is the name {self.name}") 
        
        
a = employ()
b= programer()

b.showlang()
b.showLangauge()
b.show()

'''

# Multilevel inheritance 
'''
class emplyee:
    a=1

class programer(employee):
    b=2

class manager(programer):
    c=3
    
o =emplyee()
# o.a() # show erroe bcz 'int' object is not callable
print(o.a)
# print(o.b) # 'emplyee' object has no attribute 'b

p =programer()
print(p.b)

m= manager()
print(m.c)

print(m.c, p.b, o.a)
'''

# super() method
'''
class emplyee:
    def __init__(self):
        print("constroctur of employee")
    a=1

class programer(emplyee):
    def __init__(self):
        print("constroctur of programer")
    b=2

class manager(programer):
    def __init__(self):
        super().__init__() # super() method run perent constroctur
        print("constroctur of manager")
    c=3
    
# o =emplyee()
# print(o.a)

# p =programer()
# print(p.b)

m= manager()
print(m.c)
'''
# class methods
'''
class emplyee:
    a=1334
    @classmethod # this attribute run class atr
    def show(cls):
        print(f"class atr is {cls.a}")
        
e= emplyee()
e.a = 26

e.show()
'''
# property decorater
'''
class emplyee:
    a=1334
    @classmethod 
    def show(cls):
        print(f"class atr is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"    

    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

        
e= emplyee()
e.a = 26

e.name ="ranjan kumar"
print(e.fname, e.lname)

e.show() 
'''
'''
 #  abstraction and encapsulation
1. Abstraction
Abstraction is the concept of hiding the complex implementation details
and showing only the essential features of an object. It allows you to focus on what an 
object does rather than how it does it.

2. Encapsulation
Encapsulation is the concept of bundling data (attributes) and methods (functions) that
operate on that data into a single unit or class. It also restricts direct access to some of 
an object,7s components, which is a form of data hiding.

'''
# operater overloading
'''
class number:
    def __init__(self,n):
      self.n= n
   
    def __add__ (self, num):
        return self.n + num.n

n= number(2)
m =number(5)

print(n + m)
'''