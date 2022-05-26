from data_structures.hashtable import Hashtable
import re

def first_repeated_word(word):
    regex = re.compile('[^a-zA-Z ]')
    stripped = regex.sub('', word)
    words = stripped.lower().split()

    dictionary = set()

    for word in words:
        if word in dictionary:
            return word
        else:
            dictionary.add(word)
