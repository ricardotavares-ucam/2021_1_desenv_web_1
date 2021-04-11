from user import User

class Client(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._login = kwargs['login']
        self._password = kwargs['password']
    
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, login):
        self._login = login

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
    