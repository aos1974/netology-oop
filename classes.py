# =====================================================
# Подключаемый (импортируемый) модуль classes
# определяет основные классы студентов и преподавателей
# =====================================================

# определение объекта Студент
class Student:

    # инициализация объекта, с передачей ФИО и пола
    def __init__ (self, name, surname, gender):
        
        self.name = name
        self.surname = surname
        self.gender = gender
        
        # оконченные и изучаемые студенотом курсы
        self.finished_cources = []
        self.current_cources = []

        # оценки, в формате cource, score
        self.grades = {}  

        return
    
    # добавление пройденых курсов
    def append_finished_cources(self, cource):

        # удаляем курс из текущих (изучаемых)
        if cource in self.current_cources:
            self.current_cources.remove(cource)

        # добавляем курс в пройденные
        self.finished_cources.append(cource)        
        return

    # добавление изучаемых (новых) курсов
    def append_current_cources(self, cource):
        
        if cource not in self.current_cources:
            self.current_cources.append(cource)        
        
        return

    # установка оценок за курс
    def set_grades (self, cource, grades):

        # если студент изучает предмет, то выставляем оценки
        if cource in self.current_cources:
            self.grades[cource] = grades            

        return

# определение объекта преподователь
class Teacher:

    # инициализация объекта, с передачей ФИО и пола
    def __init__ (self, name, surname, courses = []):

        self.name = name
        self.surname = surname

        # список преподаваемых курсов
        self.cources = courses

        return
    
    # выставление оценок студентам
    def set_grades(self, the_student, cource, grades):

        # если преподаватель преподает курс, тогда он выставляет оценки
        if isinstance(the_student, Student) and cource in self.cources:
            the_student.set_grades(cource, grades)

        return

