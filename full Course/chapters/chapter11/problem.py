# problem-1
'''
class twoDvector:
    def __init__(self,i, j):
        self.i =i
        self.j =j

    def show(self):
        print(f"vector is {self.i}-i and {self.j}- j")
        
class threeDvector(twoDvector):
  def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k =k
       
  def show(self):
        print(f"vector is {self.i}-i and {self.j}- j and {self.k}-k")    
        
a =twoDvector(23, 34)
a.show()
b= threeDvector(222, 344, 243)       
b.show()
'''
# problem-2
'''
class animals:
    pass
class pets(animals):
    pass
class dog(pets):   
    @staticmethod
    def bark():
        print("bow bow!")       
d= dog()
d.bark()
'''
# problem-3
'''
class Employee:
    salary = 25698
    increment = 94.6
    @property
    def salaryAfterInc(self):
       return  self.salary + self.salary * (self.increment/100)
   
    @salaryAfterInc.setter
    def salaryAfterInc(self,salary ):
       self.increment=  ((salary /self.salary)-1)*100

e= Employee()
print(e.salaryAfterInc)
e.salaryAfterInc =50008
print(e.increment)
'''

# problem-4
'''
class complex:
    def __init__(self, i, r):
        self.i = i
        self.r = r
    def __add__(self, c2):
        return complex(self.r +c2.r , self.i + c2.i) 

    def __str__(self):
        return f"{self.i}-i + {self.r}-r "


c1= complex(1,2)
c2 = complex(3,4)
print(c1+c2)
'''

# problem-7
'''
class complex:
    def __init__(self, i):
        self.i = i
    
    def __len__(self):
        return len(self.i)    
        
c= complex([2,3,4,3, 32, 3,3 ,2,32 ,3])

print(len(c))
'''