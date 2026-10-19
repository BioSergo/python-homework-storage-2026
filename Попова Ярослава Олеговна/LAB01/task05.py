def triangle_c(a, b):
	return (a**2 + b**2) ** 0.5

def triangle_b(a, c):
	return (c**2 - a**2) ** 0.5

if __name__ == '__main__':
	while True:
		user_answer = input("Что ищем? 1 - гипотенузу, 2 - катет, 3 - сегодня без математики: ")

		if user_answer == "3":
			break
		elif user_answer == "1":
			try:
				a = float(input("Введите 1 катет: "))
				b = float(input("Введите 2 катет: "))

				if a <= 0 or b <= 0:
					print("Ошибка! Катеты всегда положительны")
					continue

				result = triangle_c(a, b)
				print(f"Гипотенуза равна: {result:.3f}")

			except ValueError:
				print("Вводите только числа, даже дроби")

		elif user_answer == "2":
			try:
				a = float(input("Введите известный катет: "))
				c = float(input("Введите гипотенузу: "))

				if a <= 0 or c <= 0:
					print("Ошибка! Стороны не могут быть отрицательными")
					continue

				if a >= c:
					print("Ощибка! Гипотенуза всегда больше катета.")

				result = triangle_b(a, c)
				print(f"Катет равен: {result:.3f}")

			except ValueError:
				print("Вводите только числа, даже дроби")

		else:
			print("Ошибка! Выберите 1,2 или 3")
