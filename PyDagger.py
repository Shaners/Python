# old old code, redo this

# Imports exit and random modules
from sys import exit
import random, time

# Requirements:
# 5 rooms
# 1 lock
# 1 key
# 1 monster
# 1 trap
# 1 treasure
# 1 weapon
# Ability to die
# Ability to win
# Use of list
# Use of dict
# Use of function
# Use of module

# To do:
# Room navigation
# Room descriptions
# picking up items
# equipping weapon
# locked room
# key and unlocked room

inventory = []
player = {'has_key': False, 'equip_weapon': False}
rooms = [{'name': 'forest',
          'description': "You enter a dense dewy forest.\nTo the East you see some ruins.\nTo the West you see pebbles leading to a cave.",
          'options': ['east', 'west']},
         {'name': 'cave'},
         {'name': 'ruins'},
         {'name': 'cove'},
         {'name': 'boss'}]

def toContinue(message):
    print(message)
    input("Press enter to continue... ")

# Display inventory items to player
def inventory_check():
  if not inventory:
      toContinue("You have no items! Your inventory is empty.")
  else:
      toContinue(str(inventory))

def equip_attempt(item):
  if item not in inventory:
    print(f"You don't have a {item} so you can't equip one. Check your inventory.")
  elif item == "sword":
    player['equip_weapon'] = True
    print(f"Your {item} has been equipped.")
  else:
    print(f"{item} is not something you can equip.")

def enterRoom(roomNumber):
    print(rooms[roomNumber].description)
    print("What would you like to do?")
    choice = input("> ").lower()

    if choice == "help" or choice == "h":
        print("Here are the instructions:")
        instructions()
        enterRoom(roomNumber)
    elif choice == "inventory" or choice == "inv" or choice == "i":
        inventory_check()
        enterRoom(roomNumber)
    else:
        print(f"I don't understand '{choice}', try using help if you are lost.")
        enterRoom(roomNumber)

def room1():
  print("\nYou enter a dense dewy forest. \nTo the East you see some ruins.")
  print("To the West you see pebbles leading to a cave.\nWhat do you do?")

  choice = input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print("Here are the instructions again:")
    instructions()
    room1()
  elif choice == "inventory" or choice == "inv" or choice == "i":
    inventory_check()
    room1()
  elif choice == "go north" or choice == "go south":
    print(f"Sorry you cannot {choice}.")
    room1()
  elif choice == "go east":
    room3()
  elif choice == "go west":
    room2()
  else:
    print(f"I don't understand '{choice}', try using help if you are lost.")
    room1()
  
def room2():
  print("\n  You enter a dimly lit cave. Your eyes slowly adjust to the")
  print(" darkness. \nTo the North goes deeper into the cave. \nTo the East you")
  print(" see a lush forest.\nWhat do you do?")

  choice = input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print("Here are the instructions again:")
    instructions()
    room2()
  elif choice == "inventory" or choice == "inv" or choice == "i":
    inventory_check()
    room2()
  elif choice == "go west" or choice == "go south":
    print(f"Sorry you cannot {choice}.")
    room2()
  elif choice == "go north":
    room4()
  elif choice == "go east":
    room1()
  else:
    print("I don't understand '{choice}', try using help if you are lost.")
    room2()

def room3():
  print("\n  You enter some ancient ruins of a people you don't know.")
  print("\nYou can move North but a thick veil of mist blocks your vision.")
  print("\nTo the west you see a lush forest.\nWhat do you do?")

  choice = input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print("Here are the instructions again:")
    instructions()
    room3()
  elif choice == "inventory" or choice == "inv" or choice == "i":
    inventory_check()
    room3()
  elif choice == "go east" or choice == "go south":
    print(f"Sorry you cannot {choice}.")
    room3()
  elif choice == "go north":
    room4()
  elif choice == "go west":
    room1()
  else:
    print(f"I don't understand '{choice}', try using help if you are lost.")
    room3()

def room4():
  print("\n  You enter an over-grown cove. Waves lap a sandy grey beach.")
  print("\nTo the North you see an exit over-grown with thick vines.")
  print("\nTo the East you see ruins.\nTo the West you see a dark cave.")

  choice = input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print("Here are the instructions again:")
    instructions()
    room4()
  elif choice == "inventory" or choice == "inv" or choice == "i":
    inventory_check()
    room4()
  elif choice == "go south":
    print(f"Sorry you cannot {choice}.")
    room4()
  elif choice == "go north":
    room5()
  elif choice == "go west":
    room2()
  elif choice == "go east":
    room3()
  else:
    print(f"I don't understand '{choice}', try using help if you are lost.")
    room4()
  
def room5():
  print("\n  The air is filled with an electric energy. A spiky mossy giant ")
  print("turtle sits in the corner. Suddenly it rears back on it's hind legs")
  print("and begins to charge you.\nWhat do you do?")

  choice = input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print("Here are the instructions again:")
    instructions()
    room5()
  elif choice == "inventory" or choice == "inv" or choice == "i":
    inventory_check()
    room5()
  elif choice == "go south":
    room4()
  elif choice == "fight":
    win()
  else:
    dead("a turtle crushed you.")
  
def win():
  print("You've defeated the were-turtle and won your freedom!")
  input("Press enter to exit... ")
  exit(0)
  
def dead(cause):
  print(f"Uh oh, {cause} A'int that a stick in the mud.")
  input("Press enter to exit... ")
  exit(0)

def opening_sequence():
  instructions()  
  room1()

def instructions():
  print("\n *********************************** ")
  print(" *********** Instructions ********** ")
  print(" *********************************** ")
  input("Press enter to continue... ")
  print("\n-Basic Movement-")
  print("To move around the world type:")
  print(" Go east")
  print(" Go west")
  print(" Go north")
  print(" Go south")
  input("Press enter to continue... ")
  print("\n-Checking your Inventory-")
  print("To view the items that you are carrying in your inventory type:")
  print(" Inventory, inv, or i")
  print("This will return a list of all the items you are currently")
  print("carrying.\n")
  input("Press enter to continue... ")
  print("\n-Equiping Items-")
  print("To equip an item type:")
  print(" Equip item_name")
  print("For example: Equip stick")
  print("You can only equip armor and weapons that you are currently")
  print("carrying in your inventory.")
  input("Press enter to continue... ")

opening_sequence()