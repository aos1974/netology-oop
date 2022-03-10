# импортируем исходные классы Студент (Student) и Преодаватель (Teacher)
from classes import Student, Teacher

# определяем новый класс Студентов, которые могут выставлять оценки Лекторам
class ActiveStudent(Student):

    # выставление оценок Лекторам
    def set_grades_2_lecturers(self, the_lecturer, cource, grade):

        # если студент изучает курс, тогда он выставляет оценки
        if isinstance(the_lecturer, Lecturer) and cource in self.current_cources:
            the_lecturer.set_grades_from_students(cource, grade)

        return

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


# определяем новый класс преподавателей - Эксперты
class Reviewer(Teacher):

    # только проверяет работы
    reviewer = True

# 
# Основная программа
#

# инициализируем список студентов - экземпляр класса Student
students = []
students.append(ActiveStudent('Ivan', 'The Grate', 'male'))
students[0].append_finished_cources('Git')
students[0].append_current_cources('Python')

students.append(ActiveStudent('Olga', 'Zakharova', 'female'))
students[1].append_finished_cources('Marketing')
students[1].append_current_cources('Python')

# инициализируем Преподавателей - экземпляры классов Lecturer и Reviewer
lecturer1 = Lecturer('Isaak', 'Hill', ['Pythons philosofy', 'Python'])
reviewer1 = Reviewer('Bill', 'Collins', ['Git', 'Python'])

# выставляем оценки всем студентам (одинаковые)
for student in students:
    reviewer1.set_grades(student, 'Git', [5, 5, 5, 5, 5])
    reviewer1.set_grades(student, 'Python', [5, 5, 5])

# студенты выставляют оценки лектору
for student in students:
    for cource in student.current_cources:
        student.set_grades_2_lecturers(lecturer1, cource, 9)

# отчет
for student in students:
    print('Student ->', student.name, student.surname, ':')   
    print('Finished ->', student.finished_cources)
    print('Current ->', student.current_cources)
    print('Scores ->', student.grades)
    print('')

print('Teacher ->', lecturer1.name, lecturer1.surname)
print('Cources ->', lecturer1.cources)
print('Lector ->', not lecturer1.reviewer)
print('Scores ->', lecturer1.grades)

print('Teacher ->', reviewer1.name, reviewer1.surname)
print('Cources ->', reviewer1.cources)
print('Lector ->', not reviewer1.reviewer)