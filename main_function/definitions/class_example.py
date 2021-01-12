class Person:
    def __init__(self, first_name, last_name, age):
        self.firstName = first_name
        self.lastName = last_name
        self.age = age

    def set_last_name(self, val):
        self.lastName = val

    def print_details(self):
        print('Your first name is:', self.firstName, ' and your last name is: ', self.lastName,
              ' and your age is: ', self.age)

    def multiply_age(self, num):
        self.age = self.age * num

    def get_age(self):
        return self.age
