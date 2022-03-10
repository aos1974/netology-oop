# импортируем исходные классы Студент (Student) и Преодаватель (Teacher)
from classes import Student, Teacher

# определяем новый класс преподавателей - Лекторы
class Lecturer(Teacher):

    # только читает лекции
    reviewer = False

# определяем новый класс преподавателей - Эксперты
class Reviewer(Teacher):

    # только проверяет работы
    reviewer = True

# 
# Основная программа
#

# инициализируем список студентов - экземпляр класса Student
students = []
students.append(Student('Ivan', 'The Grate', 'male'))
students[0].append_finished_cources('Git')
students[0].append_current_cources('Python')

students.append(Student('Olga', 'Zakharova', 'female'))
students[1].append_finished_cources('Marketing')
students[1].append_current_cources('Python')

# инициализируем Преподавателей - экземпляры классов Lecturer и Reviewer
lecturer1 = Lecturer('Isaak', 'Hill', ['Pythons philosofy', 'Python'])
reviewer1 = Reviewer('Bill', 'Collins', ['Git', 'Python'])

# выставляем оценки всем студентам (одинаковые)
for student in students:
    reviewer1.set_grades(student, 'Git', [5, 5, 5, 5, 5])
    reviewer1.set_grades(student, 'Python', [5, 5, 5])

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

print('Teacher ->', reviewer1.name, reviewer1.surname)
print('Cources ->', reviewer1.cources)
print('Lector ->', not reviewer1.reviewer)