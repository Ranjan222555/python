# persist means save file
'''
"w" = 'w' is used for text files (strings)
"wb" ='wb' is used for binary files (bytes)
"r" ='r' stands for read mode 
'''
'''
fil = open("new.txt")
dta = fil.read()
print(dta)
fil.close()
'''
'''
sat="Ranjan is a good boy"
file = open("my.txt", "w")  # "w" means create new file
file.write(sat)
file.close()
'''
'''
sat=" Ranjan is a good boy "
file = open("my.txt", "a")  # "a" add in last file
file.write(sat)
file.close()

'''

'''
file = open("new.txt") 
read_line= file.readlines()
print(read_line, type(read_line))
file.close()
'''
# while loop
'''
varrr= file.readline()
while (varrr != ""):
    print(varrr)
    varrr= file.readline()
file.close()
'''

# with statement 

'''
with open("new.txt") as file:
    print(file.read())
'''

