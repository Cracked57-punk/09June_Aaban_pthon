import os
os.chdir("Assisgnments/Module 3/Session 2")

playlist = open("playlist.txt", "w")
playlist.write("Song 1\nSong 2\nSong 3\nSong 4\nSong 5")
playlist.close()

playlist = open("playlist.txt", "r")

playlist.readline()
playlist.readline()
position = playlist.tell()
print(f"{playlist.seek(position)}\n{playlist.readline()}")
playlist.close()