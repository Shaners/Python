# Pig Latin
# This will prompt the user for a string and then convert it to pig latin

vowels = ['a','e', 'i', 'o', 'u', 'y']

# Prompt the user for a string
userInput = input("Please enter a string:\n> ")

# Convert input to Pig Latin
userInput = userInput.split()
for i, word in enumerate(userInput):
  for character in word:
    if character.lower() not in vowels:
      word += character
      word = word[1:]
    else:
      word += 'ay'
      break

  word = word.lower()
  userInput[i] = word

userInput[0] = userInput[0].capitalize()

# Print string as Pig Latin
print(' '.join(userInput) + '.')