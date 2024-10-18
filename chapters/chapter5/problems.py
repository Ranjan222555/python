
# problem -1
'''
words={
    "how are you":"kese ho",
    "fine":"thik hoon",
    "you":"tum"
    }

word=input("enter any words: ")
    
print(words[word])
'''

# problem -2

'''
n=set()

word=input("enter numbers: ")
n.add(int(word))
word=input("enter numbers: ")
n.add(int(word))
word=input("enter numbers: ")
n.add(int(word))
word=input("enter numbers: ")
n.add(int(word))
word=input("enter numbers: ")
n.add(int(word))
word=input("enter numbers: ")
n.add(int(word))

print(n) 

'''
# problem -3
'''
s=set()
s.add(18)
s.add("18")

print(s)
'''

# problem -4
'''
s = set()
s.add(20) 
s.add(20.0)
s.add('20') # length of s after these operations?

print(s)
print(len(s))
ans- 2

'''
# problem -5

'''
s={}
print(type(s))

ans- dict
'''
# problem -6

'''
name={}

frind=input("enter your fav name: ")
lang=input("enter your fav lag : ")
name.update({frind:lang})

frind=input("enter your fav name: ")
lang=input("enter your fav lag : ")
name.update({frind:lang})

frind=input("enter your fav name: ")
lang=input("enter your fav lag : ")
name.update({frind:lang})

frind=input("enter your fav name: ")
lang=input("enter your fav lag : ")
name.update({frind:lang})


print(name)

'''

# problem -7 & 8

'''

ans- if names are same then the output will be re-write updated value.
ans - nothing happen. 

'''
# problem -9

# s = {8, 7, 12, "ranjan", [1,2]} 

'''
s = {8, 7, 12, "ranjan", (1,2)} # change this set list to tuple

s.remove((1,2))
s.add((33,22))
print(s) # list can't be store in set
        #you can change list to tuple then it will chnage
        
'''

