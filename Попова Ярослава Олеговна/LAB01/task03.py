VOWELS = "аеёиоуыэюя"
CONSONANTS = "бвгджзйклмнпрстфхцчшщ"
PUNCTUATION = ".,!?;:-()"

def parse_text(text):
	words_tuple = tuple(text.split())
	unique_count = len(set(words_tuple))

	vowels = 0
	consonants = 0
	punctuation = 0

	for t in text.lower():
		if t in VOWELS:
			vowels += 1
		elif t in CONSONANTS:
			consonants += 1
		elif  t in PUNCTUATION:
			punctuation += 1
	return unique_count, vowels, consonants, punctuation

if __name__ == '__main__':
	user_text = input("Введите строку слов, разделенных пробелами: ")

	u_words, v_count, c_count, p_count = parse_text(user_text)
	print(f"Количество уникальных слов: {u_words}")
	print(f"Гласных букв: {v_count}")
	print(f"Согласных букв: {c_count}")
	print(f"Знаков препинания: {p_count}")
