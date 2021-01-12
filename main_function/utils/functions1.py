from definitions.class_example import Person

def get_persons(num):
    persons = []
    for i in range(num):
        print('Round: ', i)
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        age = int(input('Enter age: '))
        new_person = Person(first_name, last_name, age)
        persons.append(new_person)
    return persons

# Max function
def my_max(num1, num2):
    print('** FUNCTIONS1 ** MAX number between', num1, 'and', num2)
    if num1 > num2:
        return num1
    else:
        return num2


# Min function
def my_min(num1, num2):
    print('** FUNCTIONS1 ** MIN number between', num1, 'and', num2)
    if num1 > num2:
        return num2
    else:
        return num1
