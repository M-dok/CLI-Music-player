import os 
class Audio(object):
    def __init__(self, name, path):
        self._name = name
        self._path = path

    def getName(self):
        return self._name
    
    def getPath(self):
        return self._path
    
    def __str__(self) -> str:
        return f"{self._name}"
    name = property(getName)
    path = property(getPath)
    
    
