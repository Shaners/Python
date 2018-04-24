# Palindrome Checker
# This will prompt user for input and check to see if it is a palindrome

# Refactor idea - this is more complicated than it needs to be
# We should just reverse the string and then compare the two

import re

# Prompt string input from user
userInput = raw_input("Please enter a string:\n> ")

# Check if string is a palindrome
userInput = userInput.lower().split()
userInput = ''.join(userInput)
userInput = re.sub(r'[^a-z0-9]', '', userInput)

for character in userInput:
    if len(userInput) <= 1 :
        print "This is a palindrome!"
        break

    if character != userInput[len(userInput)-1]:
        print "This is not a palindrome."
        break

    userInput = userInput[1:]
    userInput = userInput[:-1]
