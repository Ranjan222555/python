# problem-1 " display a user entered name using input () function"
'''
name = input("enter your name  :")


print("good afternoon" ,name)

# Fstring 

print(f"good afternoon   {name}")

'''

# problem-2   " fill in a letter template"

letter = '''
Dear <|Name|>,
You are selected!
<|Date|
'''

# print(letter.replace("|Name|" ,"ranjan").replace("<|Date|" , "22 sept "))


# problem-3  "detect double space"

'''
name = "ranjan   kumar "

print(name.find(" "))
'''

# problem-4 "Replace the double space "
'''
name = "ranjan  kumar "

print(name.replace("  ", " "))

''' # strings are immutable 

# problem-5 " escape sequence characters "

letter = "Dear Ranjan,\n\t This python course is nice. \nThanks!"

print(letter)

