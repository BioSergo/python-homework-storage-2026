DELIMER = ','

def repdigits(numbers):
	seen = set()
	clones = set()

	for num in numbers:
		if num in seen:
			clones.add(num)
		else:
			seen.add(num)
	return clones

if __name__ == '__main__':
	while True:
		user_answer = input("Введите последовательность чисел через запятую: ")
		user_answer = user_answer.replace(",", " ")
		user_answer = user_answer.split()

		numbers  = []
		try:
			for num in user_answer:
				numbers.append(int(num))
			break
		except ValueError:
			print("Ошибка! Введите только целые числа.")

	result = repdigits(numbers)
	if len(result) == 0:
		print("Повторяющихся элементов в последовательности нет!")
	else:
		print(f"Повторяющиеся элементы в последовательности присутствуют! {result}")
