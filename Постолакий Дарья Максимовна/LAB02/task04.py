#!/usr/bin/env python3


VOWELS = ("а","е","ё","и","о","у","ы","э","ю","я","a","e","i","o","u")

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in VOWELS:
            count += 1
    return count

def filter_strings_with_vowels(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, str) and count_vowels(value) >= 3:
            result[key] = value
    return result

if __name__ == '__main__':
    result_user = filter_strings_with_vowels(greeting="Привет мир", animal="кот", number=42, fruit="апельсин", drink="молоко", items=[1, 2, 3])
    print(result_user)
