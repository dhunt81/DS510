##################################
### Created: June 30, 2025
### Author: Devin Hunt
### DS510 Assignment 5 Part A
### Description: This program counts the number of times words appear in an ASCII file.
### Inputs: input.txt
### Packages: string, io
### Output: console output of words and frequency counts
### References: some snippits of code and logic borrowed from code snippets by Loren Rhodes and Gerald Kruse
##################################

import io
import string

# Define a file variable to hold the file of interest
file = io.open("input.txt", 'rt')
# Read in the entire contents of the file into a rawText variable
rawText = file.read()
# Close the file since we are done with it
file.close()

# convert string to lower case and then split by blank spaces
rawWords = rawText.lower().split()

# Use default punctions from string.punctuation and remove ' and - from the list
removeChar = string.punctuation.replace("'", '').replace("-", "")

# Remove punctuation from the words as noted above. This is done by ignoring punctuation using the translate function
table = str.maketrans('', '', removeChar)
strippedWords = [w.translate(table) for w in rawWords]

# Take the cleaned up words and put them into a dictionary mapping the word and the count
wordCount = {}
for w in strippedWords:
    if w not in wordCount:
        wordCount[w] = 1
    else:
        wordCount[w] += 1

# print out the contents of the dictionary
maxLen = len(max(wordCount, key=len))
for key, value in wordCount.items():
    print("word:" , key.ljust(maxLen) , "freq:" , value)


''' Sample Test Run
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 5\\Assignment 5A - Hunt.py"
word: hi        freq: 1
word: there     freq: 1
word: this      freq: 1
word: is        freq: 1
word: a         freq: 1
word: sample    freq: 2
word: file      freq: 2
word: and       freq: 2
word: isn't     freq: 1
word: it        freq: 3
word: nice      freq: 2
word: we'd      freq: 1
word: like      freq: 1
word: to        freq: 1
word: read      freq: 1
word: in        freq: 2
word: all       freq: 1
word: the       freq: 2
word: words     freq: 1
word: count     freq: 1
word: their     freq: 1
word: frequency freq: 1
word: if        freq: 1
word: works     freq: 1
word: would     freq: 1
word: be        freq: 1
>>>


'''