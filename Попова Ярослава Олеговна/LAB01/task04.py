TEXT_TO_NUM = {
    " ": "0", "А": "1 ", "Б": "2 ", "В": "3 ", "Г": "4 ", "Д": "5 ", "Е": "6 ", "Ё": "7 ",
    "Ж": "8 ", "З": "9 ", "И": "10 ", "Й": "11 ", "К": "12 ", "Л": "13 ", "М": "14 ",
    "Н": "15 ", "О": "16 ", "П": "17 ", "Р": "18 ", "С": "19 ", "Т": "20 ", "У": "21 ",
    "Ф": "22 ", "Х": "23 ", "Ц": "24 ", "Ч": "25 ", "Ш": "26 ", "Щ": "27 ", "Ъ": "28 ",
    "Ы": "29 ", "Ь": "30 ", "Э": "31 ", "Ю": "32 ", "Я": "33 "
}

NUM_TO_TEXT = {
    "0": " ", "1": "А", "2": "Б", "3": "В", "4": "Г", "5": "Д", "6": "Е", "7": "Ё",
    "8": "Ж", "9": "З", "10": "И", "11": "Й", "12": "К", "13": "Л", "14": "М",
    "15": "Н", "16": "О", "17": "П", "18": "Р", "19": "С", "20": "Т", "21": "У",
    "22": "Ф", "23": "Х", "24": "Ц", "25": "Ч", "26": "Ш", "27": "Щ", "28": "Ъ",
    "29": "Ы", "30": "Ь", "31": "Э", "32": "Ю", "33": "Я"
}

def encode_to_numbers(text):
    table = str.maketrans(TEXT_TO_NUM)
    return text.translate(table).strip()

def decode_to_text(numbers):
    parts = numbers.split()
    result_letters = []

    for num in parts:
        if num in NUM_TO_TEXT:
            result_letters.append(NUM_TO_TEXT[num])
        else:
            result_letters.append(num)
    return "".join(result_letters)

if __name__ == '__main__':
    print("Шифр: А=1, Б=2 ... Я=33. 0 - пробел")

    while True:
        user_input = input("Что делаем? 1 - Текст в цифры, 2 - Цифры в текст, 3 - ничего не делаем ")

        if user_input == "3":
            break
        elif user_input == "1":
            raw_text = input("Введите фразу на русском (ЗАГЛАВНЫМИ БУКВАМИ): ")
            result = encode_to_numbers(raw_text)
            print(f"Зашифрованная последовательность: {result}")
        elif user_input == "2":
            raw_code = input("Введите числа через пробел: ")
            result = decode_to_text(raw_code)
            print(f"Расшифрованная фраза: {result}")
        else:
            print("Ошибка! Введите 1, 2 или 3.")
