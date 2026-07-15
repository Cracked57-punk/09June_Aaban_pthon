import os 
os.chdir("Assisgnments/Module 3/Session 1")

playlist = open("my_fav_songs.txt", "r")

songs = playlist.readlines()

print(f"Total number of songs: {len(songs)}")
playlist.close()