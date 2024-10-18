# Loops
'''

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)

# same work in this 

for i in range(1,8):
    print(i)

'''
    
# while loops
'''
i= 1
while(i<6):
    print(i)
    i+=1   # i=i+1

i=0
while(i<=5):
    print("ranjan")
    i+=1
'''

# # list in while 

name=["ranjan", 23, False, "hay", 22.56]

# work in while loops

'''
i=0
while(i<len(name)):
    print(name[i])
    i+=1
'''

# work in for loops
'''
for i in name:
    print(i)
'''

# for loops


# tuple in for loop
'''
t=(1, 2, 3, 6,4 ,3 )
for i in t:
    print(i)
'''

# str in for loop
'''
l="ranjan"
for i in l:
    print(i)
'''

# dict in for loop
'''
l={2,5,7,2,  2,1 , 2, }
for i in l:
    print(i)
else:
    print("hello")
'''

# break , continue , pass, statement in loops 
'''
for i in range(10):
    if(i==5):
        break # stop there (selected eliment)
    print(i)
# output 
0
1
2
3
4
'''
'''
for i in range(10):
    if(i==5):
        continue # skip selected eliment
    print(i)
# output 
0
1
2
3
4
6
7
8
9
'''
'''
for i in range(11):
    if(i==5):
        pass # nothing will happen
    print(i)
'''
'''
for i in range(10):
    print(i)
    if(i==5):
        pass # skip selected eliment
'''
'''
for i in range(12):

  pass    
           # pass skip whole program
  
i=0

while (i<10):
    i+=1
    print(i)
'''

