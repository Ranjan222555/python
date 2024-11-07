# problem -1

'''
number1=int(input("enter no-1: "))
number2=int(input("enter no-2: "))
number3=int(input("enter no-3: "))
number4=int(input("enter no-4: "))

if(number1>number3 and number1>number4 and number1>number2):
    print("gragest number : ", number1)
    
elif (number2>number1 and number2>number3 and number2>number4):
    print("gragest number : ", number2)
    
elif (number3>number2 and number3>number1 and number3>number4):
    print("gragest number : ", number3)
    
elif (number4>number3 and number4>number1 and number4>number2):
    print("gragest number : ", number4)

''' 

# problem -2

'''
marks1=int(input("subject-1: "))
marks2=int(input("subject-2: "))
marks3=int(input("subject-3: "))
marks4=int(input("subject-4: "))

total_percentage=(marks1+marks2+marks3+marks4)/400*(100)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print("you pass", total_percentage)

else:
    print("you failed", total_percentage)
'''

# problem -3
# spam filter
'''
spam1=" Make a lot of money"
spam2="buy now"
spam3="subscribe this"
spam4="click this"

message=input("enter msg: ")

if((spam1 in message) or (spam2 in message) or (spam3 in message) or (spam4 in message) ):
    print("its a spam ")

else:
    print("not spam")
'''
# problem -4
'''
name=input("enter name: ")

if((len)(name)<10):
    print("with in 10 letters")

else:
    print("out of 10 letters")
'''

# problem -5
'''
l=["ranjan", "sipun", "hello", "there"]

msg=input("enter name: ")

if(msg in l):
    print("present")
    
else:
    print("not present")
'''

# problem -6
'''
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
'''
'''
marks=int(input("enter mark: "))

if(marks<=100 and marks>=90 ):
    grade="EX"
    
elif(marks<90 and marks>=80 ):
    grade="A"
    
elif(marks<80 and marks>=70 ):
    grade="B"
    
elif(marks<70 and marks>=60 ):
    grade="C"
    
elif(marks<60 and marks>=50 ):
    grade="D"
    
elif(marks<50):
    grade="F"
    
print(grade)

'''
# problem -7
'''
l="ranjan"

post=input("enter story: ")

if(l in post):
    print("my name is there")
    
else:
    print("nice story")
    
'''
# another way
'''
post=input("enter post: ")


if("ranjan" in post.lower()):
    print("my name")
    
else:
    print("no problem")

'''