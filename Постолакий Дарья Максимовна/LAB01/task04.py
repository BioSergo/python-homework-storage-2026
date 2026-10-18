#!/usr/bin/env python3
LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ALPHABET = {letter: i + 1 for i, letter in enumerate(LETTERS)}
SHIFR = {i + 1: letter for i, letter in enumerate(LETTERS)}

def encode_text(text): # Текст - числа
    result = []
    for word in text.lower().split():
        clean_word = word.strip(".,!?;:")
        punctuation = word[len(clean_word):]
        if clean_word.isdigit():
            result.append(clean_word)
            if punctuation:
                result.append(punctuation)
        else:
            for symbol in clean_word:
                if symbol in ALPHABET:
                    result.append(str(ALPHABET[symbol]))
                else:
                    result.append(symbol)
            result.append("_")
            if punctuation:
                result.append(punctuation)
    if result and result[-1] == "_":
        result.pop()
    return ' '.join(result)

def decode_text(text): # Числа - текст
    result = []
    for token in text.split():
        if token.isdigit():
            number = int(token)
            if number in SHIFR:
                result.append(SHIFR[number])
            else:
                result.append(token)
        elif token == "_":
            result.append(" ")
        else:
            result.append(token)
    return ' '.join(result)

if __name__ == '__main__':
    print("Выберите режим:\n1 — зашифровать текст (буквы - числа)\n2 — расшифровать числа (числа - буквы)")
    mode = input("Ваш выбор: ")
    if mode == '1':
        text = input("Введите текст(без цифр!): ")
        print("Результат:", encode_text(text))
    elif mode == '2':
        text = input("Введите числа через пробел: ")
        print("Результат:", decode_text(text))
    else:
        print("Неверный выбор режима")
