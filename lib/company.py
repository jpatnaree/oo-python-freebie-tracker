from .freebie import Freebie

class Company:

    all = []

    def __init__(self, name,founding_year):
        self.name = name
        self.founding_year = founding_year
        Company.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise Exception('name must be a string')
        
    @property
    def founding_year(self):
        return self._founding_year
    
    @founding_year.setter
    def founding_year(self, new_founding_year):
        if hasattr(self, "_founding_year"):
            if isinstance(new_founding_year, int):
                self._founding_year = new_founding_year
            else:
                raise Exception('founding_year must be an integer')
        else:
            raise Exception("founding_year cannot be change")
        
    def freebies(self):
        return [f for f in Freebie.all if f.company == self]
    
    def devs(self):
        return [f.dev for f in Freebie.all if f.company == self]