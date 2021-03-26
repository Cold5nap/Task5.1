from sys import argv
from iter import DataIteration
import codecs
import re


def str_file(direct: str):
    data = ""
    try:
        file = codecs.open(direct, encoding='utf-8')
        data = file.read()
    except FileNotFoundError:
        print("not found file")
    return data


def add_rev_word_to_data(data: str, word: str):
    it_word = iter(DataIteration(word[::-1]))
    while True:
        try:
            data += next(it_word)
        except StopIteration:
            break
    return data


def is_letter(c: chr):
    if re.match(r'\w', c) is None:
        return False
    else:
        return True

#запихнуть в iter
#пара значений не слово и слово
def reversed_word_in_data(data: str):
    new_data = ""
    word = ""
    iterator = iter(DataIteration(data))
    while True:
        try:
            c = next(iterator)
            if is_letter(c):
                word += c
            else:
                if len(word) > 0:
                    new_data = add_rev_word_to_data(new_data, word)
                    word = ""
                new_data += c
        except StopIteration:
            break

    if len(word) > 0:
        new_data = add_rev_word_to_data(data, word)
    return new_data


# методы, на чарах
def main():
    direct = "input\input" + argv[1] + ".txt"
    old_data = str_file(direct)
    new_data = reversed_word_in_data(old_data)

    print("Исходный текст:")
    print(old_data)
    print("Новый текст:")
    print(new_data)


# 23
if __name__ == '__main__':
    main()
