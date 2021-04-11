from car import Car
class Taxi:
    def __init__(self, **kwargs):
        self._id = kwargs['id']
        self._description = kwargs['description']
        self._license_number = kwargs['license_number']
        self._license_plate = kwargs['license_plate']
        self._km = kwargs['km']
        self._type = kwargs['type']

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
    
    @property
    def type(self):
        return self._type

    
    @type.setter
    def type(self, type):
        self._type = type
    
    @property
    def km(self):
        return self._km
    
    @km.setter
    def km(self, km):
        self._km = km

    #  TODO: Terminar o restante!
    
    