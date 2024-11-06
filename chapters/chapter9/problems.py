# problem-1
'''
file= open("poem.txt", )
line =  file.read()
if ("twinkel" in line):
    print("twinkel present")
else:
    print("twinkel  not present")
file.close()
'''

# problem-2
'''
import random

def game():
    print("you are playing this game...")
    score= random.randint(1, 100)
    # fetching the high score
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if (hiscore!=""):
            hiscore= int (hiscore)
        else:
            hiscore=0
    print(f"your score is: {score}")        
    if( score>hiscore ):
        with open("hiscore.txt", "w") as f:
    
         f.write(str(score))
        
        
        return score
game()
'''
# problem-3
# tables from 2 to 20  persist in file
'''
def generate_table(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i} \n"

    with open ( f"tables/table_{n}.txt", "w") as f:
        f.write(table)
for i in range(2,21):
    generate_table(i)
'''
    
# problem-4
'''
w = "donkey" 
with open("poem.txt") as f:
    content=f.read()
    
new_content= content.replace(w, "######")

with open("poem.txt", "w") as f:
    f.write(new_content)
'''
# problem-5
'''
w = ["donkey","bad" ] 
with open("poem.txt") as f:
    content = f.read()
    for word in w:   
        content = content.replace(word, "#" * len(word) )

with open("poem.txt", "w") as f:
    f.write(content)
'''
# problem-6

'''
with open("poem.txt") as f:
    read = f.read()
    
if ("python" in read):
    print("yess")    
else:
    print("not")
'''

# problem-7
'''
with open("poem.txt") as f:
    lines = f.readlines()

lineno = 1
for lin in lines:
    if ("python" in lin):
        print(f"yes present line no :{lineno}")
        break
    lineno += 1
    
else:
    print("not present")    
'''
# problem-8
'''
with open("poem.txt") as f:
   content=  f.read()
    
with open("poem_copy.txt", "w") as f:
    f.write(content)
'''
# problem-9
'''
with open("poem.txt") as f:
   content1=  f.read()
    
with open("poem_copy.txt") as f:
   content2 = f.read()
   
if (content1 == content2):
    print("same")
else:
    print("not same")
'''
    
# problem-10
# wipe out the content 
'''
with open("poem_copy.txt", "w") as f:
    f.write("")
'''
# problem-11

'''
with open("poem_copy.txt") as f:
    content = f.read()
    
with open("re-poem_copy.txt", "w") as f:
    f.write(content)
'''
    
