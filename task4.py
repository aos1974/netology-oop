# импортируем исходные классы Студент (Student) и Преодаватель (Teacher)
from classes import Student, Teacher
from statistics import mean

# определяем новый класс Студентов, которые могут выставлять оценки Лекторам
class ActiveStudent(Student):

    # выставление оценок Лекторам
    def set_grades_2_lecturers(self, the_lecturer, cource, grade):

        # если студент изучает курс, тогда он выставляет оценки
        if isinstance(the_lecturer, Lecturer) and cource in self.current_cources:
            the_lecturer.set_grades_from_students(cource, grade)

        return
    
    # вычисление средней оценки
    def get_average_grade(self):

        aver_grade = 0
        cnt = 0

        # берем среднюю оценку по всем изучаемым курсам
        for grade in self.grades:
            aver_grade += sum(self.grades.get(grade))
            cnt += len(self.grades.get(grade))
        
        aver_grade = aver_grade / cnt

        return aver_grade
    
    # меняем "магический" метод __str__
    def __str__(self) -> str:

        s = (f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.get_average_grade():.1f}
        Курсы в процессе изучения: {self.current_cources}
        Завершенные курсы: {self.finished_cources}
        ''')

        return s
    
    # реализуем функции сравнения класса ActiveStudent
    # сравниваем среднюю оценку по предметам

    # проверка что объект является class ActiveStudent
    def isactivestudent(self, other: object) -> bool:
        
        # проверяем что other - это объект класса ActiveStudent
        if not isinstance(other, ActiveStudent):
            raise TypeError('Объект должен быть типа class ActiveStudent')

        return True

    # функция "равно"
    def __eq__(self, other: object) -> bool:

        if self.isactivestudent(other):
            res = (self.get_average_grade() == other.get_average_grade())

        return res
    
    # функция "меньше"
    def __lt__(self, other: object) -> bool:

        if self.isactivestudent(other):
            res = (self.get_average_grade() < other.get_average_grade())

        return res

    # функция "меньше или равно"
    def __le__(self, other: object) -> bool:

        if self.isactivestudent(other):
            res = (self.get_average_grade() <= other.get_average_grade())

        return res

# определяем новый класс преподавателей - Лекторы
class Lecturer(Teacher):

    # только читает лекции
    reviewer = False
    
    # инициализация объекта, с передачей ФИО и пола
    def __init__ (self, name, surname, courses = []):

        super().__init__(name, surname, courses)

        # оценки Лектора, в формате cource, score
        self.grades = {}  

        return

    # выставление оценок студентам Лектор делать не может
    def set_grades(self, the_student, cource, grades):

        return False
    
    # установка оценок за курс от студентов
    def set_grades_from_students (self, cource, grade):

        # если Лектор преподает предмет, то выставляем оценки
        if cource in self.cources:
            if self.grades.get(cource) == None:
                self.grades[cource] = []
            self.grades.get(cource).append(grade)           

        return

    # вычисление средней оценки
    def get_average_grade(self):

        aver_grade = 0
        cnt = 0

        # берем среднюю оценку по всем преподаваемым курсам
        for grade in self.grades:
            aver_grade += sum(self.grades.get(grade))
            cnt += len(self.grades.get(grade))
        
        aver_grade = aver_grade / cnt

        return aver_grade
    
    # меняем "магический" метод __str__
    def __str__(self) -> str:

        s = (f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.get_average_grade():.1f}
        ''')

        return s

    # реализуем функции сравнения класса Lecturer
    # сравниваем среднюю оценку за лекции

    # проверка что объект является class Lecturer
    def islecturer(self, other: object) -> bool:
        
        # проверяем что other - это объект класса ActiveStudent
        if not isinstance(other, Lecturer):
            raise TypeError('Объект должен быть типа class Lecturer')

        return True

    # функция "равно"
    def __eq__(self, other: object) -> bool:

        if self.islecturer(other):
            res = (self.get_average_grade() == other.get_average_grade())

        return res
    
    # функция "меньше"
    def __lt__(self, other: object) -> bool:

        if self.islecturer(other):
            res = (self.get_average_grade() < other.get_average_grade())

        return res

    # функция "меньше или равно"
    def __le__(self, other: object) -> bool:

        if self.islecturer(other):
            res = (self.get_average_grade() <= other.get_average_grade())

        return res

# определяем новый класс преподавателей - Эксперты
class Reviewer(Teacher):

    # только проверяет работы
    reviewer = True

    # меняем "магический" метод __str__
    def __str__(self) -> str:

        s = (f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        ''')

        return s
        
#
# Функции подсчета средних оценок
#

# средняя оценка всех студентов в разрезе курса обучения
def all_students_average(students: list, cource: str):

    avg = 0
    cnt = 0

    for student in students:
        if cource in student.current_cources:
            avg += mean(student.grades.get(cource))
            cnt += 1

    avg = avg / cnt

    return avg

# средняя оценка всех лекторов в разрезе преподаваемых курсов
def all_lecturers_average(lecturers: list, cource: str):

    avg = 0
    cnt = 0

    for lec in lecturers:
        if cource in lec.cources:
            avg += mean(lec.grades.get(cource))
            cnt += 1

    avg = avg / cnt

    return avg

# 
# Основная программа
#

# инициализируем список студентов - экземпляр класса Student
students = []
students.append(ActiveStudent('Ivan', 'The Grate', 'male'))
students[0].append_finished_cources('First step in programming')
students[0].append_current_cources('Python')
students[0].append_current_cources('Git')

students.append(ActiveStudent('Olga', 'Zakharova', 'female'))
students[1].append_finished_cources('Marketing')
students[1].append_current_cources('Python')

# инициализируем Преподавателей - экземпляры классов Lecturer и Reviewer
lecturer1 = Lecturer('Isaak', 'Hill', ['Pythons philosofy', 'Python'])
lecturer2 = Lecturer('Don', 'Chitas', ['Git', 'Python'])
reviewer1 = Reviewer('Bill', 'Collins', ['Git', 'Python'])

# выставляем оценки всем студентам (одинаковые)
for student in students:
    reviewer1.set_grades(student, 'Git', [4, 5, 9, 5])
    reviewer1.set_grades(student, 'Python', [5, 5, 5, 9, 10])

# студенты выставляют оценки лектору
for student in students:
    for cource in student.current_cources:
        student.set_grades_2_lecturers(lecturer1, cource, 9)
        student.set_grades_2_lecturers(lecturer2, cource, 4)

# отчет

print('Студенты:')
for student in students:
    print(student)

# сравниваем студентов
if students[0] < students[1]:
    print(f'Студент {students[0].name} {students[0].surname} учится хуже студента {students[1].name} {students[1].surname}')
elif students[0] == students[1]:
    print(f'Студенты {students[0].name} {students[0].surname} и {students[1].name} {students[1].surname} учатся одинаково.')
else:
    print(f'Студент {students[0].name} {students[0].surname} учится лучше студента {students[1].name} {students[1].surname}')

# средняя оценка за курс Python
print(f'\nСредняя оценка всех студентов за курс Python {all_students_average(students, "Python")}')

print('\nЛекторы:')
print(lecturer1)
print(lecturer2)

if lecturer1 > lecturer2:
    print(f'Лектор {lecturer1.name} {lecturer1.surname} лучше лектора {lecturer2.name} {lecturer2.surname}\n')
else:
    print(f'Лектор {lecturer2.name} {lecturer2.surname} лучше лектора {lecturer1.name} {lecturer1.surname}\n')

# средняя оценка за курс Python
print(f'Средняя оценка всех лекторов за курс Python {all_lecturers_average([lecturer1, lecturer2], "Python")}')

print('Эксперты:')
print(reviewer1)
