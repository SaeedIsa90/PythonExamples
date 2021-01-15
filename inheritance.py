class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_name(self):
        return self.name

    def make_sound(self):
        print('This Animal:', self.name, 'has no sound!!!!!')


class Dog(Animal):
    def make_sound(self):
        print('This Dog:', self.name, 'is barking')


class Cat(Animal):
    def __init__(self, name, age, color, eyes_color):
        super().__init__(name, age, color)
        self.eyes_color = eyes_color

    def make_sound(self):
        print('This Cat:', self.name, 'is meowing')

    def print_eyes_colors(self):
        print('This cat has eyes color:', self.eyes_color)


class Horse(Animal):
    def make_sound(self):
        print('This Horse:', self.name, 'is neighing')


cat = Cat('my cat', 11, 'white', 'green')
cat.make_sound()
cat.print_eyes_colors()

my_dog = Dog('my dog', 11, 'white')
my_dog.make_sound()
