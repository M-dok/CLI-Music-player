# Student ID:122383206
import os
import json
import vlc
import time 
from song import Song
from audio import Audio


class Audio_Manager(object):
    def __init__(self):
        self._audios = []
        self._music_path = f"{os.getcwd()}/audio_files"
        self._music_info_path = f"{os.getcwd()}/audio_info/info.json"

    def show_audio(self):
        '''Goes through music_files and shows the audio files available to play'''
        if len(os.listdir(self._music_path)) == 0:       #If there is no songs it tells user and quits program
            print("There are no songs that you can play")
            quit() 
        for i in range(len(os.listdir(self._music_path))):
            print(f"{i+1}:{os.listdir(self._music_path)[i]} \n")

        user_choice = int(input("Insert the number for the file you want to listen to: ")) - 1

        if user_choice < 0 or user_choice > len(os.listdir(self._music_path)):
            raise IndexError("Please insert a valid number")

        else:  # Code from: https://howtodoinjava.com/python-json/append-json-to-file/
            with open(self._music_info_path, "r") as fp:
                data = json.load(fp)
            
            file_path = data[user_choice]["File Path"]
            title = data[user_choice]["Title"]
            if data[user_choice]["isSong"]:
                genre = data[user_choice]["Genre"]
                artist = data[user_choice]["Artist"]
                self._audios.append(Song(title, file_path, artist,genre))
                return Song(title, file_path, artist,genre)
            else:
                self._audios.append(Audio(name=title,path=file_path))
                return Audio(name=title,path=file_path)
    
    def stop_audio(self,media):
        '''Stops song'''
        user_input = int(input("1:Stop\nEnter the number at the side of options: "))
        if user_input > 2:
            raise ("You can only pause or stop")
        else:
            if user_input == 1:
                media.stop()
        

    def play_audio(self, audio):  #Take an instance of Song 
        '''Plays song of users choice'''
        media = vlc.MediaPlayer(audio.path)
        print(f"Playing:'{audio.name}'")
        # Start playing the audio
        media.play()
        time.sleep(3)

        while media.is_playing():
            self.stop_audio(media)

        media.stop()
    
    def recent(self):
        if len(self._audios) == 0:
            return "You haven't listened to any songs yet"
        else:
            return f"Last played song:{self._audios[-1]}"
        
    def delete_history(self):
        '''Removes the last listened to song from user history'''
        if len(self._audios) ==0:
            return "You haven't listened to any songs yet"
        else:
            self._audios.pop()


    def getHistory(self):
        '''Shows user listening history from most recent to least recent songs listened to'''   
        if len(self._audios) == 0:
            return "No History"
        else:
            history = "Listening History"
            for i in range(1,(len(self._audios))+1):
                history = history + "\n" + (f"{(i)} - {self._audios[-i]}")
            return history        
    
    def GetMusic_Path(self):
        return self._music_path
    
    def GetMusic_Info_Path(self):
        return self._music_info_path
    
    music_path = property(GetMusic_Path)
    music_info_path = property(GetMusic_Info_Path)       



if __name__ == "__main__":
    der = Audio_Manager()
    der.show_audio()
    der.play_song(der._audios[-1])
    print(der.getHistory())
