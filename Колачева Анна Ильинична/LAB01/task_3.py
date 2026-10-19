#!/usr/bin/env python3

import string

GLASN = "eyuioaуеыаоэяию"

def validation_word(word):
    word = word.strip()
    for el in word:
        if el.isdigit():
            return False 
    return True 

schotchik = {'znaki': 0, 'glas': 0, 'sogl': 0}

def count_symbols(text):

    for i in text.lower():
        if i in GLASN:
            schotchik['glas'] += 1
        elif i.isalpha(): 
            schotchik['sogl'] += 1
        elif i in string.punctuation:
            schotchik['znaki'] += 1


if __name__ == "__main__":
    
    while True:
        user_input = input("Enter the sentence (if you want to add number of sth in your sent., please, write it by word):\n ")
        string_p = user_input.split()

        error = False

        for word in string_p:
            if not validation_word(word):
                print(f'there is figure in word "{word}", try again!\n')
                error = True
                break

        if not error:
            clean_words = [] 
            
            for word in string_p:
                cleaned_w = word.strip(string.punctuation).lower()
               
                if len(cleaned_w) > 0: 
                    clean_words.append(cleaned_w)
            
            unic_words = set(clean_words)
            words_tuple = tuple(clean_words)
            break

    count_symbols(user_input)

    print(f'The number of unic words in sentence is: {len(unic_words)}\n')
    print("-"*17)
    print(f'The number of vowels: {schotchik['glas']}')
    print(f'The number of consonants: {schotchik['sogl']}')
    print(f'The number of punctuation: {schotchik['znaki']}')
