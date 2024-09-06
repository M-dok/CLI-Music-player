from audio import Audio
class Song(Audio):
    def __init__(self, name, path, artist, genre):
        super().__init__(name,path)
        self._artist = artist
        self._genre = genre
    
    def getArtist(self):
        return self._artist
    
    def getGenre(self):
        return self._genre
    
    def __str__(self) -> str:
        return super().__str__()
    
    artist = property(getArtist)
    genre = property(getGenre)