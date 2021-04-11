class User:
    def __init__(self, **kwargs):
        self._id = kwargs['id']
        self._cpf = kwargs['cpf']
        self._name = kwargs['name']
        self._address = kwargs['address']
        self._email = kwargs['email']
        self._phone_number = kwargs['phone_number']

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def phone_number(self):
        return self._email
    
    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number