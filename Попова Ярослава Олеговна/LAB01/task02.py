COURSES = ("Высшая математика", "Ботаника низших растений", "Физика", "Дискретная математика", "ОРГ")

def statistic(students_dict):
	all_grades = []
	for  grades_list in students_dict.values():
		all_grades.extend(grades_list)

	average = sum(all_grades) / len(all_grades)
	maximum = max(all_grades)
	minimum = min(all_grades)

	return average, maximum, minimum

if __name__ == '__main__':
	students = {}
	while True:
		student_name = input("Для выхода из цикла нажмите Enter. Введите имя студента:")

		if student_name in students:
			print("Студент с таким именем уже есть. Введите другое.")
			continue

		if student_name == "":
			break

		while True:
			courses = ", ".join(COURSES)

			print(f"Порядок курсов: {courses}")
			grades = input(f"Введите {len(COURSES)} оценок через пробел: ")
			grades_list = grades.split()

			if len(grades_list) != len(COURSES):
				print(f"Ошибка! Введите {len(COURSES)} оценок")
				continue

			student_grades = []
			try:
				for g in grades_list:
					mark = int(g)
					if not (3 <= mark <= 5):
						raise ValueError
					student_grades.append(mark)

				students[student_name] = student_grades
				break
			except ValueError:
				print("Ошибка! Оценки должны быть целыми числами в диапозоне от 3 до 5")

	if not students:
		print("Данные отсутствуют.")
	else:
		avg, mx, mn = statistic(students)
		print(f"Средний балл: {avg:.2f}")
		print(f"Максимальные оценки: {mx}")
		print(f"Минимальные оценки: {mn}")
