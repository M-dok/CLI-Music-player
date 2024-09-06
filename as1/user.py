# Student ID:122383206
from song_upload import SongUpload
from audio_upload import AudioUpload


class User():
    def __init__(self, fname, lname, username, email):
        self._fname = fname
        self._lname = lname
        self._username = username
        self._email = email

    def publish_song(self):
        '''Allows user to upload songs'''
        title = input("Enter song title: ")
        artist_name = input("Enter artist name: ")
        genre = input("Enter the genre of music: ")
        path = input("Enter the file path (including extension):")
        SongUpload(title,path,artist_name,genre)

    def publish_audio(self):
        name = input("Enter title: ")
        path = input("Enter the file path (including extension):")
        AudioUpload(name,path)


    def GetFname(self):
        return self._fname

    def SetFname(self, fname):
        if type(fname) != str:
            raise "Please enter a valid name"
        else:
            self._fname = fname

    def GetLname(self):
        return self._lname

    def SetLname(self, lname):
        if type(lname) != str:
            raise "Please enter a valid name"
        else:
            self._lname = lname

    def GetUsername(self):
        return self._username

    def SetUsername(self, username):
        if type(username) != str:
            raise "Please enter a valid name"
        else:
            self._username = username

    def GetEmail(self):
        return self._email

    def SetEmail(self, email):
        if "@" not in email or "." not in email:
            raise TypeError("Please insert a valid email")
        else:
            self._email = email


    
    def __str__(self):  # Need to change !
        return f"{self.name} is a listener and his email is {self.email}"

    fname = property(GetFname, SetFname)
    lname = property(GetLname, SetLname)
    username = property(GetUsername, SetUsername)
    email = property(GetEmail, SetEmail)




if __name__ == "__main__":
    der = User("mike", "ok", "wasda", "mick@gmail.com")
    der.publish_song()
    der.publish_audio()

   
