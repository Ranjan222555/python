# ask to user 
'''
n= int(input("enter num: "))
print("*" * n)    
'''
'''
enter num: 9
*********
'''
# use function to print
'''
def star(n):
    print("*" * n)
star(3)
'''

# questions
'''
# star pattern -5
* * * * *  
* * * * *
* * * * *
* * * * *
* * * * *
'''
'''
n=5
for i in range(n):       # 1st loop for colum
    for j in range(n):   # 2nd loop for row
        print("*", end=" ")  # end="" for not print new line,if use this" "you can add space between stars
    print("")
'''
# incresing triangle 

'''
* 
* *
* * *
* * * *
* * * * *
'''
'''
n=5
for i in range(n):
    for j in range(i):
        print("*", end=" " ) 
    print()    
'''

# decresing triangle 
'''
* * * * * 
* * * *
* * *
* *
*
'''
'''
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
'''
# right side tringle
'''
n=5
for i in range(n):
    
    for j in range(i,n):
     print(" ", end="")
        
    for k in range(i+1):
     print("*", end="")
    print()
    
out put

     *
    **
   ***
  ****
 *****       
'''
 # pyramid paytern
'''
n=5
for i in range(n):
    
    for j in range(i,n):
     print(" ", end="")
        
    for k in range(i+1):
     print("*", end=" ")
    print()
    
out put 
     * 
    * *
   * * *
  * * * *
 * * * * *
'''
# right side tringle

'''
n=5
for i in range(n):
    for j in range(n+1):
        print(" ", end="")
    for j in range(i, n):
        print("*", end="")
    print()

out put
      *****
      ****
      ***
      **
      *       
'''   
'''
n=5
for i in range(n):
    for j in range(i+1):
        print(" ", end="")
    for j in range(i, n):
        print("*", end=" ")
    print()
    
out put
 * * * * * 
  * * * *
   * * *
    * *
     *

'''
'''
n=5
for i in range(n):
    for j in range(i+1):
        print(" ", end="")  # if space add then output is this 
    for j in range(i, n):  
        print("*", end="")
    print()
    
out put
 *****
  ****
   ***
    **
     *
'''