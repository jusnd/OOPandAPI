class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0
    
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0
    
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade()}')
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_student_grade(students, course):
    grades = [grade for student in students if course in student.grades for grade in student.grades[course]]
    return round(sum(grades) / len(grades), 1) if grades else 0

def average_lecturer_grade(lecturers, course):
    grades = [grade for lecturer in lecturers if course in lecturer.grades for grade in lecturer.grades[course]]
    return round(sum(grades) / len(grades), 1) if grades else 0

students = [
    Student('Ruoy', 'Eman', 'male'),
    Student('Anna', 'Smith', 'female')
]

lecturers = [
    Lecturer('John', 'Doe'),
    Lecturer('Emily', 'Davis')
]

reviewers = [
    Reviewer('Some', 'Buddy'),
    Reviewer('Alice', 'Brown')
]

students[0].courses_in_progress += ['Python']
students[1].courses_in_progress += ['Python']

lecturers[0].courses_attached += ['Python']
lecturers[1].courses_attached += ['Python']

reviewers[0].courses_attached += ['Python']
reviewers[1].courses_attached += ['Python']

reviewers[0].rate_hw(students[0], 'Python', 10)
reviewers[0].rate_hw(students[0], 'Python', 9)
reviewers[1].rate_hw(students[1], 'Python', 8)
reviewers[1].rate_hw(students[1], 'Python', 7)

students[0].rate_lecturer(lecturers[0], 'Python', 10)
students[1].rate_lecturer(lecturers[1], 'Python', 9)

print(students[0])
print(students[1])
print(lecturers[0])
print(lecturers[1])
print(reviewers[0])
print(reviewers[1])

print(f'Средняя оценка за ДЗ по Python: {average_student_grade(students, "Python")}')
print(f'Средняя оценка за лекции по Python: {average_lecturer_grade(lecturers, "Python")}')
