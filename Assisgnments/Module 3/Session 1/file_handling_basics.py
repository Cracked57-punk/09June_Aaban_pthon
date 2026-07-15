import os

os.chdir("Assisgnments/Module 3/Session 1")

playlist = open("my_fav_songs.txt","w")

playlist.write("Song 1\nSong 2\nSong 3\nSong 4\nSong 5\n")
playlist.close()