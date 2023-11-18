from .freebie import Freebie

class Dev:

    all = []
    
    def __init__(self, name):
        self.name = name
        Dev.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise Exception('name must be a string')
        
    def freebies(self):
        return [ f for f in Freebie.all if f.dev == self]
    
    def companies(self):
        return [f.company for f in Freebie.all if f.dev == self]