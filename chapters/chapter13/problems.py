# problem -1 
# create vertual env
# created env1 and env2
 
# problem -2
'''
a = input("enter your name: ")
b = int(input("enter your marks: "))
c = int(input("enter your phone number: "))
detls =f"name is {a} and marks is {b} and number is {c}"
print(detls)

# or

dets= "name is {} and marks is {} and num is {}".format("ranjan", "90", "6576")
print(dets)
'''
# or
'''
a = input("enter your name: ")
b = int(input("enter your marks: "))
c = int(input("enter your phone number: "))

det = "name is {} and marks is {} and num is {}".format(a,b,c)
print(det)
'''
# problem -3
'''
mul = []
def mul(n):
    for i in range(1,11):
        print(f"[{n}X{i}={n*i}]") 
mul(4)
'''
# or
'''
table = [str(7*i) for i in range(1,11)]
li = "\n".join(table)
print(li)
'''
# problem -4
'''
num = [5, 10, 2, 15, 3, 8, 25, 30, 29]
numbers = list(filter(lambda x:x%5==0, num))
print(numbers)
'''
# or 
'''
def devi(n):
  if (n%5==0):
      return True
  return False
newnum= filter(devi, num)
print(list(newnum))
'''
# problem -5
'''
from functools import reduce

num = [5, 10, 2, 15, 3, 8, 25, 30, 295]
def grater(a,b):
    if (a>b):
        return a
    return b
print(reduce(grater, num))

# or
newnum = reduce(lambda x,y :x if x>y else y , num)
print(newnum)
'''
# problem -6
# Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.
# done

# problem -7
# Explore the ‘Flask’ module and create a web server using Flask & Python
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()
'''