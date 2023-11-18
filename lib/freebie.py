
class Freebie:

    all = []
    
    def __init__(self, item ,value, dev, company):
        self.item = item
        self.value = value
        self.dev = dev
        self.company = company
        Freebie.all.append(self)

    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, new_item):
        if isinstance(new_item, str):
            self._item = new_item
        else:
            print('item must be a string')

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, int):
            self._value = new_value
        else:
            print('value must be an integer')

    def dev(self):
        return [f.dev for f in Freebie.all]
    
    def company(self):
        return [f.company for f in Freebie.all]

