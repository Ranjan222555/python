# problem-1
'''
n=int(input("enter number: "))

for i in range(1,11):
    print(f"{n}x{i}={n*i}")
'''
# problem-2
'''
l = ["ranjan", "sipun", "rahul", "rohan"]

for name in l:
    if name.startswith("r"):
        
        print( f"hi there how are you {name}")
'''
# problem-3
'''
n=int(input("enter any number: "))

i=0
while (i<10):
    i+=1
    print(f"{n}x{i}={n*i}")
'''
# problem-4
# check prime numbers
'''
n=int(input("Enter any number: "))

for i in range(2,n):
    if(n%i)==0:
        print("not prime")
        break
else:
    print("its a prime")
'''

# problem-5
'''
n=int(input("Enter any number: "))
i=1
sum=0
while(i<=n):
    sum +=i
    i+=1
print(sum)
'''

# problem-6
'''
n=int(input("Enter any number: "))

product=1

for i in range(1, n+1):
    product=product*i
print(f"factorial {n} is {product}")
'''

# problem-7
# star pattern
'''
n=int(input("Enter any number: "))

for i in range(1, n+1):
    print(" "* (n-i),end="" )        
    print("*"* (2*i-1),end=""  )        
    print("")    
'''

# problem-8
'''
n=int(input("Enter any number: "))

for i in range(1, n+1):
    print("*"* i,end="" )               
    print("") 
'''

# problem-9
'''
n=int(input("Enter any number: "))

for i in range(1, n+1):
    if (i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("") 
    
'''
    
'''
n=int(input("Enter any number: "))

for star in range(1, n+1):
    space= n-star
    print(" "* space +"*"*star )
for star in range(n-1, 0, -1):
    space= n-star
    print(" "* space +"*"*star )
'''   

# problem-10
'''
n=int(input("enter number: "))

for i in range(1,11):
    print(f"{n}x{11-i}={n*(11-i)}")

'''
        