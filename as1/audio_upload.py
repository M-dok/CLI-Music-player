# Student ID:122383206
import os
import shutil
import json
from audio import Audio

class AudioUpload(Audio):
    def __init__(self, name,path):
        super().__init__(name,path)
        self._info = {}
        self._file_name = ""
        self._file_path = ""
        self.publish()

    def publish(self):
        # first establishes a directory to place audio files in the current place in the folder
        cwd = os.getcwd()
        music_path = f"{cwd}/audio_files"
        music_info_path = f"{cwd}/audio_info"
        if not os.path.isdir(music_path) or not os.path.isdir(music_info_path):
            os.mkdir(music_path)
            os.mkdir(music_info_path)

        if ".mp3" not in self.path:
            raise Exception(
                "Please insert a valid file name that includes .mp3 or .wav")
        if not os.path.isfile(self.path):
            raise Exception(f"The file you entered does not exist. Please enter the absolute path of your file")

        info_list = []
        self._file_name = os.path.basename(self.path)
        self._file_path = os.path.join(music_path, self._file_name)
        self._info.update({ "isSong":False,
                            "Title":self._name,
                            "File Path": self._file_path})
        music_info_file = f"{music_info_path}/info.json"
        if not os.path.isfile(music_info_file):
            info_list.append(self._info)
            with open(os.path.abspath(music_info_file), "w") as info:
                json.dump(info_list,info,indent=4)
            
            shutil.move(self.path, music_path)
                
        else: #Code from: https://howtodoinjava.com/python-json/append-json-to-file/
            with open(os.path.abspath(music_info_file),"r") as info:    
                data = json.load(info)
            
            data.append(self._info)
        
            with open(os.path.abspath(music_info_file),"w") as info:
                json.dump(data,info,indent=4)

            shutil.move(self.path, music_path)
            
            
    
    def getInfo(self):
        return self._info

    def __str__(self):
        return f'''{self._info}'''

    info = property(getInfo)


if __name__ == "__main__":
    der = AudioUpload("bob")
    print(der)
