'''
def square(n):
    return n*n
# same work using lambda

  # square = lambda s: s*s      #  lambda arguments: expression
print(square(4))

# using multiple arguments
sum = lambda a,b,c : a+b+c

print(sum(2,5,6))
'''

#  join methods
'''
a = ["ranjan", "kumar", "majhi"]
final = "_" .join(a)
print(final)
'''
# format methods
'''
fin = "{1} is a goog boy and {0} also".format("ranjan", "sipun")  # you can change arguments by add 1,0
print(fin)
'''

#  MAP, FILTER & REDUCE methods 
 
# map methods 

'''
li = [1,2,3,4,3,2,]
square = lambda s: s*s
sqlis = map(square, li)
print(list(sqlis))
'''
# or
'''
#sqrlis = list(map(lambda s:s*s , li, )) 
sqrlis = list(map(lambda s:s**2 , li, ))  # it can write like this 
print(sqrlis)
'''
# filter method
'''
def even(n):
  if (n%2 ==0):
    return True
  return False
onlyev = filter(even, li)  
print(list(onlyev))
'''
# or
'''
onlyeven = list(filter(lambda s:s%2 ==0 , li))
print(onlyeven)
'''
# reduce method
'''
from functools import reduce
def sum(a,b):
  return a+b
print(reduce(sum, li))
'''
# or
'''
from functools import reduce
product1 = reduce(lambda a,b : a+b, li)
product2 = reduce(lambda a,b : a*b, li)
print(product1)
print(product2)
'''




