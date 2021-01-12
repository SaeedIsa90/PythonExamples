from utils.functions1 import my_max, get_persons


if __name__ == '__main__':
    print('Im in main file')
    persons = get_persons(2)
    val = my_max(persons[0].get_age(), persons[1].get_age())
    print('Results is:', val)
