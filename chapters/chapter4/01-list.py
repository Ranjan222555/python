name = [" Ranjan ", "age", 22, "23.34"]
'''
print(name[2])

name[2] = "24"
print(name[3])  # list are mutable

print(name[0:3])

'''

 # list methods 
'''
name.append("python")  # append means add some item
print(name)

print(name[4])
'''

'''
number=[1,34,22,4,222,4321,33,2,4]

# number.sort()
# number.reverse()
# number.insert(2, 120)
# number.pop(2,)
# print(number.pop(2))
# num=number.pop(2)
num=number.remove(4)

print(num)

'''
# tuple

'''
a=(1, 2, 3)
a=(1,)
print(type(a))
'''

# tuple methods
'''
a=(1, 2, 3,True, False, "ranjan", "age",20.33 )

alist=list(a)

alist.remove("age")

print(tuple(alist))

print(a.index("ranjan"))

print(a.count("ranjan"))

'''