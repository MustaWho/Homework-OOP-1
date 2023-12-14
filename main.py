import math


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0

    def rate_lector(self, lector, course, grade_lector):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress\
                and grade_lector in range(0, 11):
            if course in lector.grades_lector:
                lector.grades_lector[course] += [grade_lector]
            else:
                lector.grades_lector[course] = [grade_lector]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        return self.average_score < other.average_score
    def __gt__(self, other):
        return self.average_score > other.average_score
    def __eq__(self, other):
        return self.average_score == other.average_score

    def __str__(self):
        score = []
        for i in self.courses_in_progress:
            for x in self.grades[i]:
                score.append(x)
        self.average_score = round(sum(score) / len(score), 2)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_score}\n'\
               f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lector = {}
        self.average_score = 0

    def __str__(self):
        score = []
        for i in self.courses_attached:
            for x in self.grades_lector[i]:
                score.append(x)
        self.average_score = round(sum(score) / len(score), 2)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_score}'

    def __lt__(self, other):
        return self.average_score < other.average_score
    def __gt__(self, other):
        return self.average_score > other.average_score
    def __eq__(self, other):
        return self.average_score == other.average_score


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def comparison_rate(class1, class2):
    if class1.average_score > class2.average_score:
        print(f'{class1.name} {class1.surname} имеет средний балл {class1.average_score} выше чем у '
              f'{class2.name} {class2.surname} со средним баллом {class2.average_score}')
    elif class1.average_score == class2.average_score:
        print(f'{class1.name} {class1.surname} имеет средний балл {class1.average_score} такой же как у '
              f'{class2.name} {class2.surname}  со средним баллом {class2.average_score}')
    else:
        print(f'{class1.name} {class1.surname} имеет средний балл {class1.average_score} ниже чем у '
              f'{class2.name} {class2.surname}  со средним баллом {class2.average_score}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

student_2 = Student('Max', 'Rith', 'your_gender')
student_2.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Mike', 'Roven')
cool_lecturer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(student_2, 'Python', 10)
cool_reviewer.rate_hw(student_2, 'Python', 8)
cool_reviewer.rate_hw(student_2, 'Python', 8)

best_student.rate_lector(cool_lecturer, 'Python', 10)
best_student.rate_lector(cool_lecturer, 'Python', 7)

print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)
print()
print(student_2)
print()
comparison_rate(best_student, student_2)
comparison_rate(student_2, best_student)
print()
print(student_2 > best_student)
