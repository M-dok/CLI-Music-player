#Student ID:122383206
from user import User
from audioManager import Audio_Manager

user = User("michael", "O'Keeffe", "user123", "mick@gmail.com")
man = Audio_Manager()
print(user.fname)
user.publish_song()             #Allows user to publish a song 
user.publish_audio()            #allows user to publish audio
man.play_audio(man.show_audio()) #plays audio from the return val of show_audio
man.play_audio(man.show_audio())
print(man.getHistory())         #gets user history 
man.delete_history()            #deletes most recent song on users history 
print(man.getHistory())         

