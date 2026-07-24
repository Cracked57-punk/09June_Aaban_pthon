class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        print(f"Title: {self.title}\nArtist: {self.artist}\nDuration: {self.duration} minutes") 

song1=Song("songname1" ,"singer1" ,"3:59")
song2=Song("songname2","singer2","3:00")
