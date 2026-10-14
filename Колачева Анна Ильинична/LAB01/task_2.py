#!/usr/bin/env python3

SUBJECTS: list[str] = ("Структуры данных", 
            "Высшая математика",
              "Физика",
                "Ботаника высших растений",
                  "Органическая химия", 
                  "Английский язык")


def valid_mark(subject: str, student: str) -> int:
    while True:
        try:
            mark: int = int(input(f'Введите оценку {student} по  предмету {subject} (оценка может быть "3", "4", "5")\n'))
            if 3 <= mark <= 5:
                return mark
            else:
                print('Оценка не входит в диапазон от 3 до 5, попробуйте ещё раз\n')
        except ValueError:
            print('Оценка не целое число, попробуйте ещё раз\n')  
        

def raschot(base: dict[str , dict[str, int]]) -> None:
    #первый блок 

    sum_dict: dict[str, int] = {}
    counts_dict: dict[str, int] = {}

    for marks in base.values():
        for sub, mark in marks.items():
            sum_dict[sub] = sum_dict.get(sub, 0) + mark
            counts_dict[sub] = counts_dict.get(sub, 0) + 1
    print('1. Средний балл по предметам\n')
    print(*(f"{sub}: {sum_dict[sub] / counts_dict[sub]:.2f}" for sub in SUBJECTS if sub in sum_dict),
    sep="\n")

    #второй блок

    students_status = {}

    for stud, st_marks in base.items():
        sr_ball = sum(st_marks.values()) / len(st_marks)
        students_status[stud] = sr_ball
        print(f'{stud} - {sr_ball:.2f}')

    #третий блок
     
    best_student, max_sr_ball = max(students_status.items(), key=lambda x: x[1])
    Fy_student, min_sr_ball = min(students_status.items(), key=lambda x: x[1])

    print(f'Лучший студент: {best_student} ({max_sr_ball:.2f})')
    print(f'Студент с самым низким средним баллом: {Fy_student} ({min_sr_ball:.2f})')
    


if __name__ == "__main__":
    Stu_sub_mark: dict[str , dict[str, int]] = {}

    while True:
        student: str = input('Введите ФИО студента(если хотите перейти к подсчету введите "стоп"):\n').strip()

        if student.lower() == "стоп" :
            break

        if student in Stu_sub_mark:
            print('Оценки по данному студенту уже записаны, введите другое ФИО')
            continue

        all_marks: dict[str, int] = {}

        for sub in SUBJECTS:
            all_marks[sub] = valid_mark(sub, student)

        Stu_sub_mark[student] = all_marks
        print(f'Студент {student} добавлен!\n')

    raschot(Stu_sub_mark)
