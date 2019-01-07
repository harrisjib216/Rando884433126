#!/usr/bin/python3
import sys


# translate file
def translateF():
    print("nice file, let's translate it")
    randF = open(sys.argv[1], 'r')

    translation = []
    i = 0
    for word in randF:
        newWord = 0
        for char in range(i, len(word), 1):
            if char != ' ':
                newWord += ord(word[char])
            else:
                i += 1
        
        translation.append(newWord)

    print(translation)
    return



# translate string
def translateS():
    print("nice string, let's translate it")
    return



# check if file or string
def check_it():
    if ".rando884433126" in b:
        translateF()
    else:
        translateS()



# beginning of program
b = sys.argv[1]
if b:
    check_it()
else:
    print("Whoa!! You need to supply an argument m8!!")