import os 
os.chdir("Assisgnments/Module 3/Session 2")

lyrics = open("lyrics.txt", "r")

print(lyrics.tell())
lyrics.read(10)
print(lyrics.tell())
lyrics.close()