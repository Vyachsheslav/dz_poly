class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lectuer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
   
    def average_hw(self):
        count = 0
        for grades_key in self.grades:
            count += len(self.grades[grades_key])
        self.average_hw = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_hw

    def __str__(self):
        fio = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_hw()}'
        return fio

    def __lt__(self, other):
        if not isinstance(other, Lectuer):
            print('Not a Lectuer!')
            return
        return self.average_hw() < other.average_hw()
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    
    def __str__(self):
        fio = f'Имя: {self.name}\nФамилия: {self.surname}'
        return fio


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_hw(self, lectuer, course, grade):
        if isinstance(lectuer, Lectuer) and course in self.courses_in_progress and course in lectuer.courses_attached and 0< grade <=10:
            if course in lectuer.grades:
                lectuer.grades[course] += [grade]
            else:
                lectuer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_hw(self):
        count = 0
        for grades_key in self.grades:
            count += len(self.grades[grades_key])
        self.average_hw = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_hw
    
    def __str__(self):
        fio = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_hw()}\nКурсы в процессе изучения: {(", ".join(self.courses_in_progress))}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return fio

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_hw() < other.average_hw()


        
    
def average_mark(persons, course):
    total = 0
    quantity = len(persons)
    for person in persons:
        if course not in person.grades:
            quantity -= 1
            continue
        else:
            total += (sum(person.grades[course]) / len(person.grades[course]))
    return round((total / quantity), 2)





    

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в программирование']
 

one_student = Student('Reny', 'Kell', 'male')
one_student.courses_in_progress += ['PHP']
one_student.courses_in_progress += ['Python']
one_student.finished_courses += ['OOP']

cool_lectuer = Lectuer('Some', 'Buddy')
cool_lectuer.courses_attached += ['Python']

good_teach = Lectuer('Grey', 'Feros')
good_teach.courses_attached += ['Python']


nice_reviewer = Reviewer('Jon', 'Kelly')
nice_reviewer.courses_attached += ['Python']
nice_reviewer.courses_attached += ['PHP']

bad_reviewer = Reviewer('Jon', 'Kelly')
bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['PHP']



best_student.rate_hw(cool_lectuer, 'Python', 5)
best_student.rate_hw(cool_lectuer, 'Python', 5)
best_student.rate_hw(cool_lectuer, 'Python', 8)


best_student.rate_hw(good_teach, 'Python', 5)
best_student.rate_hw(good_teach, 'Python', 7)
best_student.rate_hw(good_teach, 'Python', 9)





nice_reviewer.rate_hw(one_student, 'PHP', 7)
nice_reviewer.rate_hw(one_student, 'Python', 5)
nice_reviewer.rate_hw(one_student, 'Python', 7)

 
nice_reviewer.rate_hw(best_student, 'Python', 10)
nice_reviewer.rate_hw(best_student, 'Python', 10)
nice_reviewer.rate_hw(best_student, 'Python', 10)
 
students_list = [best_student, one_student]
letcuer_list = [cool_lectuer, good_teach]

# print(average_mark(students_list, 'Python'))
# print(average_mark(letcuer_list, 'Python'))

# print(one_student)
# print(good_teach)
# print(cool_lectuer)
# print(good_teach > cool_lectuer)
# print(nice_reviewer)
# print(cool_lectuer)