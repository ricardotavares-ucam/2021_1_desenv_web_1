from user import User

class TaxiDriver(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._login = kwargs['login']
        self._password = kwargs['password']
        self._drivers_license = kwargs['drivers_license']
    
    # ISSO É UM BAD SMELL - CÓDIGO DUPLICADO
    # TODO: arrumar as classes para evitar duplicação de código
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, login):
        print('setando login')
        self._login = login
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
    
    @property
    def drivers_license(self):
        return self._drivers_license
    
    @drivers_license.setter
    def drivers_license(self, drivers_license):
        self._drivers_license = drivers_license