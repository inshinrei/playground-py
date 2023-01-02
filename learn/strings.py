import sys
import unicodedata
from unicodedata import normalize, combining

START, END = ord(' '), sys.maxunicode + 1


def find(*query_words, start=START, end=END):
    query = {word.upper() for word in query_words}

    for code in range(start, end):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name and query.issubset(name.split()):
            print(f'U+{code:04X}\t{char}\t{name}')


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold()


def shave_marks(txt):
    normalized_txt = normalize('NFD', txt)
    shaved = ''.join(char for char in normalized_txt if not combining(char))
    return normalize('NFC', shaved)
