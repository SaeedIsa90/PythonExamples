class Person:
    def __init__(self, first_name, last_name, age):
        self.__firstName = first_name
        self._lastName = last_name
        self.age = age
        self.__full_name = ''
        self.__update_full_name()

    def set_first_name(self, val):
        if type(val) != str or val == "":
            raise ValueError('First name can not be empty')
        self.__firstName = val
        self.__update_full_name()

    def get_first_name(self):
        return self.__firstName

    def set_last_name(self, val):
        if type(val) != str or val == "":
            raise ValueError('Last name can not be empty')
        self._lastName = val
        self.__update_full_name()

    def get_last_name(self):
        return self._lastName

    def __update_full_name(self):
        self.__full_name = self.__firstName + " " + self._lastName

    def get_age(self):
        return self.age

    def print_full_name(self):
        print(self.__full_name)

p = Person('Saeed', 'Isa', 100)

p.age = 'Isa120'

p.print_full_name()

p.set_first_name('Said')
p.print_full_name()
