import os

os.chdir("Assisgnments/Module 3/Session 2")

def read_next_line(filename):
    file = open(filename, "r")
    file.seek(20)
    return file.readline()

name = input("Enter the filename: ")
print(read_next_line(name))
