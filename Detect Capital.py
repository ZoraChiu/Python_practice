"""
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:

:All letters in this word are capitals, like "USA".
:All letters in this word are not capitals, like "leetcode".
:Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

TEST CASE: 123, a123, 1abc, ABC, abc, 1AC,   ,
With error handling: to check if it is not characters, numbers, space, no entry.
"""


def detect_capital():
    restart = True
    while restart:
        restart = False
        word = input("Please input a word")
        if word.isalpha() and (word.isupper() or word.islower()):
            print(True)
        elif word.isalpha() and word[0].isupper() and word[1:].islower():
            print(True)
        elif word.isalpha() is False:
            print("Please input characters")
            restart = True
        else:
            print(False)


detect_capital()

