# Rando884433126
The goal of this program is to practice some programming principles/
constructs. Rando884433126, first detects if you submitted a file ending 
in ".rando884433126" or if you submitted a string. Depending on which
program you ran (translate or decipher), Rando884433126 will then
translate your text or decipher it.


But how does Rando884433126 decipher your code??


Well, Rando884433126, is actually a language!! A very difficult one
actually. For now, Rando884433126, takes the ascii value for each 
character in the respective word and sums itself. If that doesn't
make sense, then... idk, use a different program...


Just kidding!
Here's an example.

> ummm, cipher my text please: "hello"
> I mean... i guess i'll help you: *****


I haven't actually got to the deciphering yet because as I wrote this code,
I figured that's like trying to decrypt sha256, so for now, you can't decipher :(



# decide if it's a file or string
python3 translate.py "hello"
python3 decipher.py "110044"                    -- in the works...

or

python3 translate.py hello.rando884433126
python3 decipher.py hello.rando884433126        -- in the works again....



# TRANSLATE
See "translate.py"



# PRINT
You can tell Rando884433126 to print or not print out your result.
I mean, personally I like to results cuz we're solution-oriented
'round here!! But you still have the option.

    # do not print to user
    python3 translate.py "hello" %no_print
    python3 decipher.py "110044" %no_print                   -- in the works...



# SAVE
Lastly, you can also tell Rando884433126 to save your translation
to a file or append it to your old file.
    
    python3 translate.py "hello" %append
    python3 decipher.py "110044" %new_file                   -- in the works...





translation = []
    for word in randF:
        newChars = []
        newWord = 0
        for char in word:
            if char != " ":
                newWord += ord(char)
        
        translation.append(newWord)
        print(translation)