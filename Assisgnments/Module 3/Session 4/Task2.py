
Songs =["The Abyss","Is there someone else","Moth to a Flame","Cry for Me"]

def add_song_to_playlist() :
    song_name=input ("Enter the Song you want to add:")
    if song_name in Songs:
        raise SongAlreadyExistsError(song_name)
    else :
        print(f"Your song '{song_name}' is added to the playlist.")



class SongAlreadyExistsError (Exception):
    def __init__(self, song_name):
        self.song_name = song_name
        super().__init__(f"'{song_name}' already exists in the playlist.")

try:
    add_song_to_playlist()
except SongAlreadyExistsError as e:
    print(e)