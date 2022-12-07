class MarvelHero(object):
    def __init__(self, id, name, description, image):
        self._id = id
        self._name = name
        self._description = description
        self._image = image

    def getId(self):
        return self._id
            
    def getName(self):
        return self._name
   
    def getDescription(self):
        return self._description
    
    def getImage(self):
        return self._image
