# import os

# def print_directory_contents(chapter):
#     try:
#         # Get the list of files and directories
#         entries = os.listdir(chapter)
#         # Print each entry
#         for entry in entries:
#             print(entry)
#     except FileNotFoundError:
#         print(f"The directory {chapter} does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access the directory {chapter}.")

# # Specify the chapter to the directory you want to list
# directory_chapter = 'pc file'  # '.' refers to the current directory

# # Print the contents of the directory
# print_directory_contents(directory_chapter)


import os

directory_path ='.'
path = os.listdir(directory_path)

print(path)