# Word Counter
# This will prompt user for input and return the number of words

import re

count = 0

# Prompt string input from user
userInput = raw_input("Please enter a string:\n> ")

# Count words
userInput = userInput.lower().split()

for i, word in enumerate(userInput):
    word = re.sub(r'[^a-z0-9]', '', word)
    userInput[i] = word

for word in userInput:
    if len(word) != 0:
        count += 1

# Print the number of words to console
print "There were %s words found." % count