COURSES = ('Высшая математика', 'Ботаника', 'Физика', 'Английский язык', 'Структуры данных')

def valid_grade(s_name, course_name):
    while True:
        try:
            data = input(f'Введите оценку {s_name} по предмету {course_name}:\n')
            grade_value = int(data)
            if 3 <= grade_value <= 5:
                return grade_value
            else:
                print('Ошибка, оценка должна быть от 3 до 5 включительно!')
        except ValueError:
            print('Ошибка, вы ввели не целое число!')

if __name__ == "__main__":

    students_grades = {}

    while True:
        student_name = input('Введите имя студента (или Enter для завершения):\n')

        if student_name == '':
            print('Список студентов завершен')
            break

        name_key = student_name.lower()

        if name_key in students_grades:
            print('Оценки этого студента уже были записаны')
            continue

        one_student_grade = []
        for course in COURSES:
            grade = valid_grade(student_name, course)
            one_student_grade.append(grade)

        students_grades[name_key] = one_student_grade
        print(f'Оценки студента {student_name} сохранены')

    if students_grades:
        for i, course_name in enumerate(COURSES):
            grades_for_course = [grades[i] for grades in students_grades.values()]
            average_score = sum(grades_for_course) / len(grades_for_course)
            max_grade = max(grades_for_course)
            min_grade = min(grades_for_course)
            print(f'За предмет {course_name} средний балл - {average_score}, '
                  f'максимальная оценка - {max_grade}, '
                  f'минимальная оценка - {min_grade}')
            
