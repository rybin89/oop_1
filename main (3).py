# Наследование - классы могут наследовать атрибуты и методы из других классов

# Класс пользователь
class User:
    def __init__(self, fullname, login, password, email):
        self._fullname = fullname 
        self._login = login 
        self._password = password 
        self._email = email
    # геттеры
    @property
    def fullname(self):
        return self._fullname
    @property
    def login(self):
        return self._login
    @property
    def password(self):
        return self._password
    @property
    def email(self):
        return self._email
    # сеттеры
    @fullname.setter
    def fullname(self,new_fullname):
        self._fullname = new_fullname
        return self._fullname
        
user = User('Ivan','ivan89','1234','ivan89@ivan.ru')

print(user.fullname)
user.fullname = 'Ivan Ivanov'
print(user.fullname)
# Создаём класс наследник - MANAGER
class Manager(User):
    def __init__(self, fullname, login, password, email, department):
        # наследование метода __init__
        super().__init__(fullname, login, password, email)
        self._department = department    
    # геттеры
    @property
    def department(self):
        return self._department
    @property
    def password(self):
        return self._password

    # сеттер
    @password.setter
    def password(self,new_password):
        self._password = new_password
        return self._password
        
        
manager = Manager('Peter','petya99','1234','petya@petya.petya','Бухгалтерия')

print(manager.email)
print(manager.department)
manager.fullname = 'Peter Petrow'
print(manager.fullname)
manager.password = '4321'
print(manager.password)

# класс предок/родитель ROOT - в линукс системах - это администратор
class Root(Manager):
    def __init__(self, fullname, login, password, email, department):
            super().__init__(fullname, login, password, email, department)
    # Добавить сеттры
    @login.setter
    def login(self,new_login):
        self._login = new_login
        return self._login
    @email.setter
    def email(self,new_email):
        self._email = new_email
        return self._email
    @department.setter
    def department(self,new_department):
        self._department = new_department
        return self._department
    
        
        
# добавить класс
class NewRoot:
    def __init__(self, params):
        self.params = params
    def name(self):
        print "Вывод атрибута", self.params
            
            








        