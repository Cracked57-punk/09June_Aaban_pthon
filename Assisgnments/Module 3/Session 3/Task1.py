songs = {
    "The Abyss": "4:43",
    "is there someone else": "3:19",
    "Moth to a Flame": "3:54",
    "Cry for Me" : "3:54",
}

def get_song_duration():
    try:
        song_name =input("Enter the name of the song: ")
        duration = songs[song_name]
        return duration
    except KeyError:                     #accessing a missing dictionary key with square brackets (dict[key]) raises a KeyError
        return "Song not found in the dictionary."

print(get_song_duration())  