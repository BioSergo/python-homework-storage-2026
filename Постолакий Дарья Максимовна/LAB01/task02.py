#!/usr/bin/env python3
COURSES = ("Физика", "История", "Химия", "Ботаника", "Английский")

def read_grade(course):
    while True:
        subject = input(f"{course}: ")
        if not subject.isdigit(): #.lstrip('-')
            print("Это не целое/не положительное число(или не число), попробуйте снова")
            continue
        grade = int(subject)
        if 3 <= grade <= 5:
            return grade
        print("Оценка должна быть от 3 до 5")

def students_and_grades():
    students = {}
    count = int(input("Сколько студентов? "))
    for i in range(count):
        while True:
            name = input("Имя студента: ")
            if name in students:
                print(f"Ученика с таким именем уже записали. Попробуйте другое имя")
                continue
            else:
                break
        grades = [read_grade(course) for course in COURSES]
        students[name] = grades
    return students

if __name__ == '__main__':
    students = students_and_grades()
    all_grades = []
    for grades in students.values():
        all_grades.extend(grades)
    if not all_grades:
        print("Оценок нет")
    else:
        average = sum(all_grades) / len(all_grades)
        print(f"\nСредний балл по всем студентам: {average:.2f}")
        print(f"Минимальная оценка: {min(all_grades)}")
        print(f"Максимальная оценка: {max(all_grades)}")
