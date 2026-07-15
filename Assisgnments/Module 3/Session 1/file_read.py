import os 
os.chdir("Assisgnments/Module 3/Session 1")


file = open("my_fav_songs.txt", "r")

count = 1
for line in file:
    print(f"{count}){line.strip()}")
    count += 1

file.close()