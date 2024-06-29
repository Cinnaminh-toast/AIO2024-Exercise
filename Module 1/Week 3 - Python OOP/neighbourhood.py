class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_yob(self):
        return self._yob

    def set_yob(self, yob):
        self._yob = yob

    def describe(self):
        print("Person - Name: {} - YoB: {}".format(self._name, self._yob))


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = grade

    def describe(self):
        print("Student - Name: {} - YoB: {} - Grade: {}".format(self._name, self._yob, self._grade))

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def get_specialist(self):
        return self._specialist

    def set_specialist(self, specialist):
        self._specialist = specialist

    def describe(self):
        print("Doctor - Name: {} - YoB: {} - Specialist: {}".format(self._name, self._yob, self._specialist))

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def get_subject(self):
        return self._subject

    def set_subject(self, subject):
        self._subject = subject

    def describe(self):
        print("Teacher - Name: {} - YoB: {} - Subject: {}".format(self._name, self._yob, self._subject))

class Ward:
    def __init__(self, name):
        self._name = name
        self._list_of_persons = []
    
    def add_person(self, person):
        self._list_of_persons.append(person)

    def describe(self):
        for person in self._list_of_persons:
            person.describe()

    def count_doctor(self):
        number_of_doctor = 0
        for person in self._list_of_persons:
            if isinstance(person, Doctor):
                number_of_doctor += 1

        return number_of_doctor

    def sort_age(self):
        self._list_of_persons.sort(key=lambda person: person.get_yob(), reverse=True)

    def compute_average(self):

        list_of_yob_teachers = []
        for person in self._list_of_persons:
            if isinstance(person, Teacher):
                list_of_yob_teachers.append(person.get_yob())
        return sum(list_of_yob_teachers)/len(list_of_yob_teachers)
