from data_structures.hashtable import Hashtable
import re

def first_repeated_word(word):
    regex = re.compile('[^a-zA-Z ]')
    stripped = regex.sub('', word)
    # can we tease out some relationship between length of string and what we'll end up with
    # will take more time and sub empty string
    # stripped string depends on how long the string is so it would scale with O(N)
    words = stripped.lower().split() # convert string to lower and split
    # O(N) dependent on input size

    dictionary = set()
    # storing in a set because mutable, iterable doesn't allow duplicate values


    for word in words:# O(N) because it will loop however long the words are
        if word in dictionary:
            # this will end the function and return the repeated word
            return word #(O)(1) just returning a word
            # if word not in set then add the word to th set
        else:
            dictionary.add(word) #(O)(1) space because it just adds a word

            #print statement is (O)(1) because it always just prints
