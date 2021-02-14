class Calculator:
    def __init__(self):
        self.__my_name = 'Amazing CALCULATOR'

    def who_am_i(self):
        print('Im the', self.__my_name)

    def change_my_name(self, to):
        self.__my_name = to

    @staticmethod
    def sub_numbers(a, b):
        return a - b

    @staticmethod
    def add_numbers(a, b):
        return a + b


res = Calculator.add_numbers(5, 6)
print(res)

res = Calculator.sub_numbers(3, 2)
print(res)

calc = Calculator()

res = calc.sub_numbers(5, 4)
print(res)
