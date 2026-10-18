#!/usr/bin/env python3
import string
VOWEL_LETTERS = set("аеёиоуыэюяaeiouy")
PUNCTUATION = set(string.punctuation) | set("—–…«»")

def separating_words_and_punct(text):
    result = []
    current = ""
    for symbol in text:
        if symbol.isalpha():
            current += symbol
        else:
            if current:
                result.append(current)
                current = ""
            if symbol in PUNCTUATION:
                result.append(symbol)
    if current:
        result.append(current)
    return tuple(result) # Кортеж из слов и знаков препинания

def count_unique_words(words):
    unique_words = [w.lower() for w in words if w.isalpha()]
    return len(set(unique_words)) # Кол-во уникальных слов

def count_chars(text):
    vowels = consonants = punctuation = 0
    for element in text.lower():
        if element in VOWEL_LETTERS:
            vowels += 1
        elif element.isalpha():
            consonants += 1
        elif element in PUNCTUATION:
            punctuation += 1
    return vowels, consonants, punctuation # Кол-во гласных, согласных, знаков препинания

if __name__ == '__main__':
    text = input("Напишите одно или несколько предложений:\n ")
    words = separating_words_and_punct(text)
    unique = count_unique_words(words)
    vowels, consonants, punctuation = count_chars(text)
    print(f"Кортеж: {words}")
    print(f"Уникальных слов: {unique}")
    print(f"Гласных: {vowels}")
    print(f"Согласных: {consonants}")
    print(f"Знаков препинания: {punctuation}")
