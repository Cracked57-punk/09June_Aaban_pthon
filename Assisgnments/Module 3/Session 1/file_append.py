import os 
os.chdir("Assisgnments/Module 3/Session 1")


playlist=open("my_fav_songs.txt","a")

playlist.write("Song 6\nSong 7")
playlist.close()