#!/usr/bin/python3
import sys


# write new file
def riht(finalll):
    phile = open('uR_seCret_mesAage_m8.txt', 'w+')
    if not isinstance(finalll, list):
        phile.write(str(finalll) + ' ')
    else:
        for word in finalll:
            phile.write(str(word) + ' ')

    phile.write("\n")
    phile = open('uR_seCret_mesAage_m8.txt', 'r+')
    print(phile.read())
    phile.close()
    return



# append to file
def eppand(finalll):
    phile = open(sys.argv[1], 'a+')
    phile.write("\n\n")

    for word in finalll:
        phile.write(str(word) + ' ')

    phile.write("\n")
    phile = open(sys.argv[1], 'r+')
    print(phile.read())
    phile.close()
    return



# check for other arguments
def check_save(finalT):
    print('....scrambling....')
    print("Here's your encrypted message m8:")

    if len(sys.argv) > 2 and sys.argv[2] == '+@ap_pe#nd':
        print(f"Rando884433126 appended your translation to: {sys.argv[1]}\n")
        eppand(finalT)
    else:
        print("Rando884433126 also made the new file: uR_seCret_mesAage_m8.txt\n")
        riht(finalT)
    return



# translate file
def translateF():
    print("nice file, let's translate it")
    randF = open(sys.argv[1], 'r')

    translation = []
    for word in randF:
        newWord = 0
        for char in word:
            if char != ' ':
                newWord += ord(char)
            else:
                translation.append(newWord)
                newWord = 0

    translation.append(newWord)
    return check_save(translation)



# translate string
def translateS():
    print("nice string, let's translate it")
    
    translation = 0
    for char in b:
        translation += ord(char)
    
    return check_save(translation)



# check if file or string
def check_it():
    if '.rando884433126' in b:
        translateF()
    else:
        translateS()



# beginning of program
b = sys.argv[1]
if b:
    print('')
    check_it()
else:
    print('Whoa!! You need to supply an argument m8!!')