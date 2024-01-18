# Have a python dictionary that has a key/value that represents a word and its defination
# Collect a word as the user input
# Check if the word is in the dictionary
# Print the word defination
from PyDictionary import PyDictionary

dictionary = PyDictionary()
print("PYTHON ENGLISH DICTIONARY")
print("--------------------------")

while True:
    word = input("Enter your word: ");
    if word == "":
        break
    print(dictionary.meaning(word),"\n")