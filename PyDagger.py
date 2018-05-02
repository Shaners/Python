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
# Use of list #
# Use of dict #
# Use of function #
# Use of module #
# Can quit #

# To do:
# Room navigation
# Better Room descriptions
# picking up items
# equipping weapon
# locked room
# key and unlocked room

# parse input by word?
# push these globals to start fuction or to opening seq?

inventory = []
player = {'has_key': False, 'equip_weapon': False}
# convert rooms to a class maybe
rooms = [{'name': 'forest',
          'description': "\nYou enter a dense dewy forest.\n\nTo the East you see some ruins.\nTo the West you see pebbles leading to a cave.",
          'options': {'e': 2, 'w': 1}
         },
         {'name': 'cave',
          'description': "\nYou enter a dimly lit cave. Your eyes slowly adjust to the darkness.\n\nTo the North goes deeper into the cave.\nTo the East you see a lush forest.",
          'options': {'n': 3, 'e': 0}
         },
         {'name': 'ruins',
          'description': "",
          'options': {}
         },
         {'name': 'cove',
          'description': "",
          'options': {}
         },
         {'name': 'boss',
          'description': "",
          'options': {}
         }]

def toContinue(message):
    print(message)
    input("Press enter to continue... ")

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

def enterRoom(roomNumber): # lets do this by name, number is easier for now?
    print(rooms[roomNumber]['description'])
    print("What would you like to do?")
    choice = input("> ").lower()

    if choice == "help" or choice == "h":
        print("Here are the instructions:")
        instructions()
        enterRoom(roomNumber)
    elif choice == "inventory" or choice == "inv" or choice == "i":
        inventory_check()
        enterRoom(roomNumber)
    elif choice == 'quit' or choice == 'exit':
        exit(0)
    elif choice.startswith('go '):
      if choice[3] in rooms[roomNumber]['options']:
        enterRoom(rooms[roomNumber]['options'][choice[3]])
      else:
        print(f"Sorry you cannot '{choice}'.")
        enterRoom(roomNumber)
    else:
        print(f"I don't understand '{choice}', try using help if you are lost.")
        enterRoom(roomNumber)

def room3():
  print("\n  You enter some ancient ruins of a people you don't know.")
  print("\nYou can move North but a thick veil of mist blocks your vision.")
  print("\nTo the west you see a lush forest.\nWhat do you do?")


  elif choice == "go north":
    room4()
  elif choice == "go west":
    room1()


def room4():
  print("\n  You enter an over-grown cove. Waves lap a sandy grey beach.")
  print("\nTo the North you see an exit over-grown with thick vines.")
  print("\nTo the East you see ruins.\nTo the West you see a dark cave.")






  elif choice == "go north":
    room5()
  elif choice == "go west":
    room2()
  elif choice == "go east":
    room3()

  
def room5():
  print("\n  The air is filled with an electric energy. A spiky mossy giant ")
  print("turtle sits in the corner. Suddenly it rears back on it's hind legs")
  print("and begins to charge you.\nWhat do you do?")

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
  enterRoom(0)

def instructions():
  print("\n *********************************** ")
  print(" *********** Instructions ********** ")
  print(" *********************************** ")
  input("Press enter to continue... ")
  print("\n-Basic Movement-")
  print("To move around the world type:")
  print(" go east")
  print(" go west")
  print(" go north")
  print(" go south")
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