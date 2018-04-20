# Vowel Counter
# This will prompt the user to enter a string and then provide a count of the vowels

vowels = ['a','e', 'i', 'o', 'u', 'y']
count = 0

# Prompt string input from user
userInput = raw_input("Please enter a string:\n> ")

# Iterate over each character and if vowl increase count by one
for character in userInput:
    if character.lower() in vowels:
        count += 1

# Print the number of vowels to console
print "There were %s vowels found." % count