# problem -1
'''
try:
    with open ("1st.txt", "r") as f1:
        print(f1.read())  
except Exception as e:
    print(e)        
        
try:
    with open("2nd.txt", "r") as f1:
        print( f1.read())
except Exception as e:
    print(e)        

print("thank u")
'''

# problem -2
'''
lis= [12, 22, 122, 222, 343, 132, 44, 454]

for i, item in enumerate(lis):
    if i==2 or i==4 or i==6:
        print(item)
'''
# problem -3
'''
n= int(input("enter a number: "))

for i in range(1,11):
    print(f"multification of {n} is : {n}X{i}={n*i}")
    
multi =[n*i for i in range(1,11)]
print(multi)
'''
# problem -4
'''
try:
    a=int(input("enter a number: "))
    b=int(input("enter b number: "))
    print(f"Division of a, b is: {a/b}")
except ZeroDivisionError as z:
    print(z)
'''
# problem -5
'''
n=int(input("enter a num: "))
table =[n*i for i in range(1,11)]
with open("table.txt", "a") as t:
    t.write(f"Table of {n} :{str(table)} \n" )
'''
