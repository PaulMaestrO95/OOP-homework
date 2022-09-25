class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __counting_grades(self):
        mid_grades_py = sum(self.grades['Python']) / len(self.grades['Python'])
        mid_grades_git = sum(self.grades['Git']) / len(self.grades['Git'])
        grades_py_git = (mid_grades_py + mid_grades_git) / len(self.grades)
        return round(grades_py_git, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return student_1.__counting_grades() > student_2.__counting_grades()

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: ' \
                       f'{self.__counting_grades()}\n' \
                       f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: ' \
                       f'{" ".join(self.finished_courses)}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def __calculation_grades(self):
        midle_grades_py = sum(self.course_grades['Python']) / len(self.course_grades['Python'])
        midle_grades_git = sum(self.course_grades['Git']) / len(self.course_grades['Git'])
        midle_grades_py_git = (midle_grades_py + midle_grades_git) / len(self.course_grades)
        return round(midle_grades_py_git, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return lecturer_1.__calculation_grades() < lecturer_2.__calculation_grades()

    def __str__(self):
        self.some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
                             f'{self.__calculation_grades()}'
        return self.some_lecturer


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.some_reviever = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return self.some_reviever


def average_students_grades(student, course):
    grade_lst = []
    for student in all_student:
        if course in student.grades:
            grade_lst += student.grades[course]
        else:
            return 'Ошибка'
        result_grades = sum(grade_lst) / len(grade_lst)
    return round(result_grades, 1)


def average_lecturer_grades(lecturer, course):
    list_grade = []
    for lecturer in all_lecturer:
        if course in lecturer.course_grades:
            list_grade += lecturer.course_grades[course]
        else:
            return 'Ошибка'
        result = sum(list_grade) / len(list_grade)
    return round(result, 1)


student_1 = Student('Василий', 'Васильев')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Files']

student_2 = Student('Иван', 'Иванов')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Files']

lecturer_1 = Lecturer('Иван', 'Васильевич')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Петр', 'Петрович')
lecturer_2.courses_attached += ['Python', 'Git']

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Git', 8)

student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Git', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 5)
student_2.rate_lecturer(lecturer_2, 'Git', 7)

some_reviewer = Reviewer('Джек', 'Лондон')
some_reviewer.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Александр', 'Пушкин')
reviewer_2.courses_attached += ['Python', 'Git']

some_reviewer.rate_hw(student_1, 'Python', 6)
some_reviewer.rate_hw(student_1, 'Python', 6)
some_reviewer.rate_hw(student_1, 'Python', 9)
some_reviewer.rate_hw(student_1, 'Git', 8)
some_reviewer.rate_hw(student_1, 'Git', 8)
some_reviewer.rate_hw(student_1, 'Git', 9)

some_reviewer.rate_hw(student_2, 'Python', 7)
some_reviewer.rate_hw(student_2, 'Python', 8)
some_reviewer.rate_hw(student_2, 'Python', 8)
some_reviewer.rate_hw(student_2, 'Git', 7)
some_reviewer.rate_hw(student_2, 'Git', 6)
some_reviewer.rate_hw(student_2, 'Git', 7)

all_student = [student_1, student_2]
all_lecturer = [lecturer_1, lecturer_2]

print('Student:')
print(student_1.__str__())
print(student_2.__str__())
print('Lecturer:')
print(lecturer_1.__str__())
print(lecturer_2.__str__())
print('Reviewer:')
print(some_reviewer.__str__())
print(reviewer_2.__str__())
print(f'Средняя оценка у Василия Васильева больше чем у Ивана Иванова?: {student_1.__lt__(student_2)}')
print(f'Средняя оценка у лектора Ивана Васильевича меньше чем у Петра Петровича?: {lecturer_1.__lt__(lecturer_2)}')
print(f"Средний бал среди студентов по курсу Python: {average_students_grades(all_student, 'Python')}")
print(f"Средний бал среди студентов по курсу Git: {average_students_grades(all_student, 'Git')}")
print(f"Средний бал среди лекторов за лекцию  Python: {average_lecturer_grades(all_lecturer, 'Python')}")
print(f"Средний бал среди лекторов за лекцию  Git: {average_lecturer_grades(all_lecturer, 'Git')}")
