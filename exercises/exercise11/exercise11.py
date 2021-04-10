class Student:
    def __init__(self, id, name, age, grade):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def print_details(self):
        print('Student details, id', self.__id, '- name:', self.__name,
              '- age:', self.__age, '- grade:', self.__grade)


def find_max_grade(students):
    max_grade = 0
    for s in students:
        if s.get_grade() > max_grade:
            max_grade = s.get_grade()
    return max_grade


if __name__ == "__main__":

    students = []
    with open('students.txt') as fd:
        first_line = True
        for line in fd.readlines():
            if first_line:
                first_line = False
                continue
            details = line.split()
            student = Student(int(details[0]), details[1], int(details[2]), int(details[3]))
            students.append(student)

    # Find max grade
    max_grade = find_max_grade(students)

    # Print student details
    for s in students:
        if s.get_grade() == max_grade:
            s.print_details()
