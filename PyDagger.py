# old old code, redo this

# Imports exit and random modules
from sys import exit
import random, time

# Requirements:
# 5 rooms, check
# 1 lock
# 1 key
# 1 monster, check
# 1 trap
# 1 treasure
# 1 weapon
# Ability to die, check
# Ability to win, check
# Use of list, check
# USe of dict, check
# Use of function, check
# Use of module, check

# To do:
# Room navigation, check
# Room descriptions, check
# picking up items
# equipping weapon
# locked room
# key and unlocked room

inventory = []

player = {'has_key': False, 'equip_weapon': False}

def inventory_check():
  if not inventory:
    print "You have no items! Your inventory is empty."
    raw_input("Press enter to continue... ")
  else:
    print str(inventory)
    raw_input("Press enter to continue... ")

def equip_attempt(item):
  if item not in inventory:
    print "You don't have a %s so you can't equip one. Check your inventory." % item
  elif item == "sword":
    player['equip_weapon'] = True
    print "Your ", item, " has been equipped."
  else:
    print "%s is not something you can equip." % item

def room1():
  print "\n  You enter a dense dewy forest. \nTo the East you see some ruins."
  print "To the West you see pebbles leading to a cave.\nWhat do you do?"

  choice = raw_input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print "Here are the instructions again:"
    instructions()
    room1()
  elif choice == "inventory" or choice == "inv" or choice == "i":
    inventory_check()
    room1()
  elif choice == "go north" or choice == "go south":
    print "Sorry you cannot %s." % choice
    room1()
  elif choice == "go east":
    room3()
  elif choice == "go west":
    room2()
  else:
    print "I don't understand '%s', try using help if you are lost." % choice
    room1()
  
def room2():
  print "\n  You enter a dimly lit cave. Your eyes slowly adjust to the"
  print " darkness. \nTo the North goes deeper into the cave. \nTo the East you"
  print " see a lush forest.\nWhat do you do?"

  choice = raw_input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print "Here are the instructions again:"
    instructions()
    room2()
  elif choice == "inventory" or choice == "inv" or choice == "i":
    inventory_check()
    room2()
  elif choice == "go west" or choice == "go south":
    print "Sorry you cannot %s." % choice
    room2()
  elif choice == "go north":
    room4()
  elif choice == "go east":
    room1()
  else:
    print "I don't understand '%s', try using help if you are lost." % choice
    room2()

def room3():
  print "\n  You enter some ancient ruins of a people you don't know."
  print "\nYou can move North but a thick veil of mist blocks your vision."
  print "\nTo the west you see a lush forest.\nWhat do you do?"

  choice = raw_input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print "Here are the instructions again:"
    instructions()
    room3()
  elif choice == "inventory" or choice == "inv" or choice == "i":
    inventory_check()
    room3()
  elif choice == "go east" or choice == "go south":
    print "Sorry you cannot %s." % choice
    room3()
  elif choice == "go north":
    room4()
  elif choice == "go west":
    room1()
  else:
    print "I don't understand '%s', try using help if you are lost." % choice
    room3()

def room4():
  print "\n  You enter an over-grown cove. Waves lap a sandy grey beach."
  print "\nTo the North you see an exit over-grown with thick vines."
  print "\nTo the East you see ruins.\nTo the West you see a dark cave."

  choice = raw_input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print "Here are the instructions again:"
    instructions()
    room4()
  elif choice == "inventory" or choice == "inv" or choice == "i":
    inventory_check()
    room4()
  elif choice == "go south":
    print "Sorry you cannot %s." % choice
    room4()
  elif choice == "go north":
    room5()
  elif choice == "go west":
    room2()
  elif choice == "go east":
    room3()
  else:
    print "I don't understand '%s', try using help if you are lost." % choice
    room4()
  
def room5():
  print "\n  The air is filled with an electric energy. A spiky mossy giant "
  print "turtle sits in the corner. Suddenly it rears back on it's hind legs"
  print "and begins to charge you.\nWhat do you do?"

  choice = raw_input("> ")
  choice = str.lower(choice)

  if choice == "help" or choice == "h":
    print "Here are the instructions again:"
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
  print "You've defeated the were-turtle and won your freedom!"
  raw_input("Press enter to exit... ")
  exit(0)
  
def dead(cause):
  print "Uh oh,", cause, "A'int that a stick in the mud."
  raw_input("Press enter to exit... ")
  exit(0)

def opening_sequence():
  instructions()  
  room1()

def instructions():
  print "\n *********************************** "
  print " *********** Instructions ********** "
  print " *********************************** "
  raw_input("Press enter to continue... ")
  print "\n-Basic Movement-"
  print "To move around the world type:"
  print " Go east"
  print " Go west"
  print " Go north"
  print " Go south"
  raw_input("Press enter to continue... ")
  print "\n-Checking your Inventory-"
  print "To view the items that you are carrying in your inventory type:"
  print " Inventory, inv, or i"
  print "This will return a list of all the items you are currently"
  print "carrying.\n"
  raw_input("Press enter to continue... ")
  print "\n-Equiping Items-"
  print "To equip an item type:"
  print " Equip item_name"
  print "For example: Equip stick"
  print "You can only equip armor and weapons that you are currently"
  print "carrying in your inventory."
  raw_input("Press enter to continue... ")

opening_sequence()