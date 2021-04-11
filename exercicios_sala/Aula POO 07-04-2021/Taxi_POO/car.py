class Car:
    def __init__(self, **kwargs):
        self._id = kwargs['id']        
        self._name = kwargs['name']
        self._brand = kwargs['brand']

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand