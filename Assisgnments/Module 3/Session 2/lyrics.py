import os 

os.chdir("Assisgnments/Module 3/Session 2")
lyrics = open("lyrics.txt", "w")

lyrics.write("lyrics of song 1\nlyrics of song 2\nlyrics of song 3\nlyrics of song 4\nlyrics of song 5")
lyrics.close()