# Old old code, redo this

# This is a Python-based game created by Shane Lister
# Version: 0.2.1
# Last updated on: Apr 24th, 2013

# To do 1.0
# ------
# Movement seems to work
# Test visited counter by printing dict on each movement, check
# Temp speed up wait times for testing ( no wait time? ), check
# Create inventory function, check
# Test inventory system
# Create equiping function, check
# Test equip system
# Alter player stats based on what is equiped, check
# Test player stats
# Create lock and key system
# Test lock and key system
# Create combine system ( or have key items auto combine for now )
# Test combine system
# Clean-up finalize 1.0
# Play testing

# To do 2.0
# ---------
# Replace areas with an area function ( or class? learn more about classes )
# Store instructions / help / any other long text in external file
# Reg expressions for processing user input
# Better written story
# Random monster encounters
# Random loot

# Imports exit and random modules
from sys import exit
import random, time

# Defining the weapon list
# Setting the values for each weapon
jag_steel = {'Name': 'Jagged Steel Blade', 'Damage': 10, 'Speed': 20, 'Critical': 10, 'Bleed': True, 'Venom': False}
baseball_bat = {'Name': 'Baseball Bat', 'Damage': 10, 'Speed': 15, 'Critical': 15, 'Bleed': False, 'Venom': False}
python_sword = {'Name': "Python's Sword", 'Damage': 20, 'Speed': 15, 'Critical': 20, 'Bleed': True, 'Venom': True}

# Defining the armor list
# Setting the values for each piece of armor
chrome_cap = {'Name': 'Chrome Skull Cap', 'Armor': 5}
scale_shirt = {'Name': 'Enameled Scale Shirt', 'Armor': 10}

# Defining the extra items list
items = ['Sword Hilt', 'Oil Lantern']

# Defining the keys
items = ["Python's Blade"]

# Sets up the inventory and equiped items
inventory = []
equiped = {'Weapon': 'Fists', 'Head': 'Nothing', 'Body': 'Nothing'}

def inventory_check():
if not inventory:
print "You have no items! Your inventory is empty"
else:
print str(inventory)

def equip_attempt(item):
if item not in inventory:
print "You don't have a %s so you can't equip one. Check your inventory." % item
else:
if item == "Jagged Steel Blade" or item == "Baseball Bat" or item == "Python's Sword":
equiped['Weapon'] = item
alter_stats(item)
print "You equip a %s!" % item
elif item == "Chrome Skull Cap":
equiped['Head'] = item
alter_stats(item)
print "You equip a %s!" % item
elif item == "Enameled Scale Shirt":
equiped['Body'] = item
alter_stats(item)
print "You equip a %s!" % item
else:
print "Sorry %s cannot be equipped." % item

# Create player stats
player_stats = {'Damage': 1, 'Speed': 1, 'Critical': 1, 'Bleed': False, 'Venom': False, 'Armor': 1}

def alter_stats(item):
if item == jag_steel['Name']:
player_stats['Damage'] = jag_steel['Damage'] + 1
player_stats['Speed'] = jag_steel['Speed'] + 1
player_stats['Critial'] = jag_steel['Crititcal'] + 1
player_stats['Bleed'] = jag_steel['Bleed']
player_stats['Venom'] = jag_steel['Venom']
elif item == baseball_bat['Name']:
player_stats['Damage'] = baseball_bat['Damage'] + 1
player_stats['Speed'] = baseball_bat['Speed'] + 1
player_stats['Critial'] = baseball_bat['Crititcal'] + 1
player_stats['Bleed'] = baseball_bat['Bleed']
player_stats['Venom'] = baseball_bat['Venom']
elif item == python_sword['Name']:
player_stats['Damage'] = python_sword['Damage'] + 1
player_stats['Speed'] = python_sword['Speed'] + 1
player_stats['Critial'] = python_sword['Crititcal'] + 1
player_stats['Bleed'] = python_sword['Bleed']
player_stats['Venom'] = python_sword['Venom']
elif item == chrome_cap['Name']:
player_stats['Armor'] = chrome_cap['Armor'] + 1
elif item == scale_shirt['Name']:
player_stats['Armor'] = scale_shirt['Armor'] + 1
else:
print "Error error this shouldn't happen. Cannot add stats of %S " % item

# Defining the enemy list
# Probably need to make this a dic with stats
# Removed for now
# enemy = ['Sand Crab', 'Snow Crab', 'Horned Jelly']

# Boss list, only one for now
# Probably needs stats
boss = ['Shade Wolf']

# Tracks where the player has visited and how many times
# Used to modify which area text is used
visited = {'stone_lake': 0, 'rivers_edge': 0, 'marsh': 0, 'desert_oasis': 0, 'bear_den': 0}

# Clears the screen by inserting about 52 newlines in about 2.6 sconds
def clear_screen():
for i in range(0, 25):
time.sleep( .1 )
print "\n "

# These are the instructions for playing the game
def instructions():
print "\n *********************************** "
print " *********** Instructions ********** "
print " *********************************** "
print "\n-Basic Movement-"
print "To move around the world type:"
print " Go east"
print " Go west"
print " Go north"
print " Go south"
print "This will move you in the compass direction you've indicated."
print "Please be aware that some areas may be blocked and you'll have"
print "to find a way around them using items you've collected.\n"
raw_input("Press enter to continue... ")
print "\n-Using Items-"
print "To use an item just type:"
print " Use item_name"
print "For example: Use marbles"
print "Items are used to various affects including unblocking areas.\n"
raw_input("Press enter to continue... ")
print "\n-Checking your Inventory-"
print "To view the items that you are carrying in your inventory type:"
print " Inventory, inv, or i"
print "This will return a list of all the items you are currently"
print "carrying and may be able to use to some affect.\n"
raw_input("Press enter to continue... ")
print "\n-Equiping Items-"
print "To equip an item type:"
print " Equip item_name"
print "For example: Equip stick"
print "You can only equip armor and weapons that you are currently"
print "carrying in your inventory. Weapons and armor when equiped"
print "alter your physical stats and make you more powerful.\n"
raw_input("Press enter to continue... ")
print "\n-Battling Enemies-"
print "Battles will happen automaticly when you encounter an enemy."
print "You will have 3 options in a fight:"
print " Attack"
print " Shout"
print " Flee"
print "Attacking will strike your enemy with your weapon to do damage."
print "Shouting will attempt to intimadate your enemy."
print "Fleeing will make an attempt to run away from the battle."
print "\nThe battle will end when you or your enemy has 0 health left."
print "The battle can also end if you or your enemy flees the battle."
print "You may get rewards after defeating an enemy."
raw_input("Press enter to continue... ")
print "\n-Combining Items-"
print "Some items may be combined by typing:"
print " Combine item_name with item_name"
print "For example: Combine meat with sandwich"
print "~You've created a meat sandwich!~"
print "Combining items can create new items that have different new"
print "properties. Please note not all items can be combined and in"
print "fact very few can."

# Defining each area which the character could move to
# Sets default value for displaying initial text
# stone_lake_init = True
# We don't want the full description to run every time, so if it has been displayed
# a certain number of times we'll go with a much shorter one
def stone_lake():
print visited
if visited['stone_lake'] == 0:
print " Damp air clings to your skin and you can feel hard round stones pressing"
print "into your back. It takes you a few moments but you soon realize that you"
print "aren't where you were when the world blackened."
time.sleep(0) # Zeroed for testing

if visited['stone_lake'] <= 4:
print "\n You appear to be in the middle of a dryed up lake bed lined with small"
print "smooth stones. Moist air fills your lungs and it smells as if it had"
print "recently rained but the stones are bone dry."
time.sleep(0) # Zeroed for testing
else:
print "\n You are at stone lake."
time.sleep(0) # Zeroed for testing

if 'Jagged Steel Blade' not in inventory or "Python's Sword" not in inventory:
print "\n A glint of silver catches your eye and you spot half a steel blade"
print "buried in the rocks."

if 'Oil Lantern' not in inventory:
print "\n You see an old red lantern rusting in places where the paint has"
print "peeled off. It may still work."

print "\n To the east you see a river's edge."
print " To the south you see some sand, which is strange."
    
    visited['stone_lake'] += 1
    
    print visited
    
    choice = raw_input("> ")
    choice = str.lower(choice)
    
    if choice == "help":
        # help logic here
        print "Here are the instructions:"
        instructions
        stone_lake()
    elif choice == "inventory" or choice == "inv" or choice == "i":
        # inventory logic here
        print inventory
        print "inventory! inventory!"
        stone_lake()
    elif choice == "go east":
        rivers_edge()
    elif choice == "go south":
        desert_oasis()
    elif choice == "get steel blade" or choice == "grab steel blade":
        inventory.append('Jagged Steel Blade')
        print "You grab the steel blade!"
        stone_lake()
    elif choice == "get oil lantern" or choice == "grab oil lantern" or choice == "get lantern" or choice == "grab lantern":
        inventory.append('Oil Lantern')
        print "You grab the lantern!"
        stone_lake()
    else:
        print "I don't understand '%s', maybe try using help?" % choice
        stone_lake()

def rivers_edge():
print visited

if visited['rivers_edge'] == 0:
print " new text here!!"
print ""
print ""
time.sleep(0) # Zeroed for testing

if visited['rivers_edge']<= 4:
print "\n The low rumbly rush of water over stone can be heard and the air"
print "is a bit colder here. The river banks are made from a dull grey sand."
print "Thousands of tiny diamonds in the sand sparkle when the light hits them"
print "just right giving a magical feeling to what would otherwise be an"
print "ordinary place. The river is moving too fast to be passable but you can"
print "make out small forms moving through the water, which you assume are some"
print "type of fish."
time.sleep(0) # Zeroed for testing
else:
print "\n You are at river's edge."
time.sleep(0) # Zeroed for testing

if 'Chrome Skull Cap' not in inventory:
print "\n You see what appears to be a medium sized rock but with an unatural"
print "metalic shine to it. Its surface is almost mirror like making it out of"
print "place."

print "\n To the South you see a swampy area."
print " To the West is stone lake."

    visited['rivers_edge'] += 1
    
    print visited
    
    choice = raw_input("> ")
    choice = str.lower(choice)
    
    if choice == "help":
        print "Here are the instructions:"
        instructions
        rivers_edge()
    elif choice == "inventory" or choice == "inv" or choice == "i":
        print inventory
        print "inventory! inventory!"
        rivers_edge()
    elif choice == "go west":
        stone_lake()
    elif choice == "go south":
        marsh()
    elif choice == "get rock" or choice == "grab rock":
        inventory.append('Chrome Skull Cap')
        print "You grab the chrome skull cap"
        rivers_edge()
    else:
        print "I don't understand '%s', maybe try using help?" % choice
        rivers_edge()

def marsh():
print visited

if visited['marsh'] == 0:
print " new text here!!"
print ""
print ""
time.sleep(0) # Zeroed for testing

if visited['marsh'] <= 4:
print "\n Your feet sink into the soft mossy ground. Big pools of mud and"
print "black water surround you. The air smells of sulfer and wood-rot. You"
print "see aged dropping trees covered in spider moss. It is humid and"
print "uncomfortable, your skin begins to itch."
time.sleep(0) # Zeroed for testing
else:
print "\n You are at the marsh."
time.sleep(0) # Zeroed for testing

if 'Sword Hilt' not in inventory or "Python's Sword" not in inventory:
print "\n You see out of the corner of your eye what appears to be a sword hilt"
print "covered in grit with moss growing up the side, slowly being swallowed up"
print "by the swamp."

print "\n To the North you see river's edge."
print " To the West you see a cliff you could climb down to reach desert oasis."
    print " You notice an ominous stone den marked in strange runes to the East."
    
    visited['marsh'] += 1
    
    print visited
    
    choice = raw_input("> ")
    choice = str.lower(choice)
    
    if choice == "help":
        print "Here are the instructions:"
        instructions
        marsh()
    elif choice == "inventory" or choice == "inv" or choice == "i":
        print inventory
        print "inventory! inventory!"
        marsh()
    elif choice == "go north":
        rivers_edge()
    elif choice == "go west":
        desert_oasis()
    elif choice == "go east":
        bear_den()
    elif choice == "get sword hilt" or choice == "grab sword hilt":
        inventory.append('Sword Hilt')
        print "You grab the Sword Hilt"
        marsh()
    else:
        print "I don't understand '%s', maybe try using help?" % choice
        marsh()
    
def desert_oasis():
print visited

if visited['desert_oasis'] == 0:
print " new text here!!"
print ""
print ""
time.sleep(0) # Zeroed for testing

if visited['desert_oasis'] <= 4:
print "\n You arrive at what appears to be a large hill of sand. This hill"
print "is very out of place seeing that it is surrounded by a lush forest."
print "The air seems remarkably drier here and warmer. There are a few cacti"
print "plants growing out of the sand."
time.sleep(0) # Zeroed for testing
else:
print "\n You are at the desert oasis."
time.sleep(0) # Zeroed for testing

if 'Baseball Bat' not in inventory:
print "\n You notice a wooden handle sticking part way out of the sand next to"
print "a cactus."

print "\n The forest is impassable to the West and South. A steep cliff is to the East."
print "It looks like you can only move North to stone lake."
    
    visited['desert_oasis'] += 1
    
    print visited
    
    choice = raw_input("> ")
    choice = str.lower(choice)
    
    if choice == "help":
        print "Here are the instructions:"
        instructions
        desert_oasis()
    elif choice == "inventory" or choice == "inv" or choice == "i":
        print inventory
        print "inventory! inventory!"
        desert_oasis()
    elif choice == "go north":
        stone_lake()
    elif choice == "get baseball bat" or choice == "grab baseball bat":
        inventory.append('Baseball Bat')
        print "You grab the Baseball Bat"
        desert_oasis()
    else:
        print "I don't understand '%s', maybe try using help?" % choice
        desert_oasis()
    
def bear_den():
print visited

if visited['bear_den'] == 0:
print " Running your finger over the carved runes you notice that one is a deeper"
print "than the others with serpentine scratchings surronding it. Perhaps this is"
print "how you get the large stone door to open?"
time.sleep(0) # Zeroed for testing

if visited['bear_den'] <= 4:
print "\n You enter the dim cave lit only by blue glowing runes and a sense of"
print "dread washes over you in a wave. You feel sick to your stomach and your"
print "heart beats against your chest, yelling at you to flee. You can hear the"
        print "slow drip of water on stone. A low growl echos through the cave and you"
        print "freeze in place and feel your stomach liquify."
        print "\n Blue glowing eyes flash in front of you and in complete silence a"
        print "giant dark wolf emerges from the shadows. Fresh blood drips from it's"
        print "teeth and for a half a second it looks directly into your eyes before"
        Print "it lunges towards you."
time.sleep(0) # Zeroed for testing
else:
print "\n You are at bear den."
time.sleep(0) # Zeroed for testing

if 'Enameled Scale Shirt' not in inventory:
print "\n You see a brillant white enamled scale shirt on a rock next to you."

print "\n The only way to exit the cave is to the west to the marsh."

    visited['bear_den'] += 1
    
    print visited
    
    choice = raw_input("> ")
    choice = str.lower(choice)
    
    if choice == "help":
        print "Here are the instructions:"
        instructions
        bear_den()
    elif choice == "inventory" or choice == "inv" or choice == "i":
        print inventory
        print "inventory! inventory!"
        bear_den()
    elif choice == "go west":
        marsh()
    elif choice == "get enameled scale shirt" or choice == "grab enameled scale shirt":
        inventory.append('Enameled Scale Shirt')
        print "You grab the Enameled Scale Shirt"
        bear_den()
    else:
        print "I don't understand '%s', maybe try using help?" % choice
        bear_den()
    
# Define the opening text function (should only run once per go)
def opening_sequence():
print "\n ===== "
print " == == "
print " = == "
print " = = "
print " = = "
print " = = "
print " =-\ /-- = "
print " = O* *O = "
print " = = "
print " = = "
print " = v-v = = "
print " =|== = = "
print " | = = "
print " __/ = = "
print " | = = "
print " | = = "
print " / \ = = == "
print " = = = == "
print " = = == =- "
print " = = = = "
print " = == = "
print " = = "
print " = = "
print " == = "
print " ====== \n"
print " P y t h o n 's B l a d e \n"
print " *************************************************"
print " ****************** Version 1.0 ******************"
print " *************************************************\n"
raw_input("Press enter to continue... ")
print "Welcome to Python's Blade a game created in Python by Shane Lister."
player_name = raw_input("What is your name? \n>")
print "If this is your first time playing I suggest you view the instructions / controls."
view_instructions = raw_input("Do you want to view the instructions? (Y or N): ")
if str.lower(view_instructions) == "y" or str.lower(view_instructions) == "yes":
instructions()
elif str.lower(view_instructions) == "n" or str.lower(view_instructions) == "no":
print "Ok we'll skip that but you can type help at any time to pull up the instructions."
else:
print "%s was not a valid answer to the question, so I am going to show you the instructions anyway." % view_instructions
instructions()

skip_open = raw_input("\nDo you want to skip the opening sequence?")
if skip_open == "y":
stone_lake()
else:
raw_input("\nPress enter to begin your game...")
clear_screen()
print " You are in golden yellow field. The sun beating down has warmed your skin"
print "and you have sweat beginning to form on your brow. There is a gentle breeze"
print "but not enough to cool you down. You look around at this rolling sea of golden"
print "grass stocks and wonder how you can get out of the heat. "
time.sleep(0) # Zeroed for testing
print "\n You notice a large tree providing shade a top a small hill and decide that"
print "it will be your next destination. As you make your way to the hill grass blades"
print "pull at your pants and you hear some slight rustling but ignore it for the time"
print "being."
time.sleep(0) # Zeroed for testing
print "\n As you enter the tree's shady heaven a cooling relief takes over your body"
print "and a sense of calmness takes over you. You lay down in the shade of the large"
print "tree and daze off into the distance, trying to put your thoughts together."
time.sleep(0) # Zeroed for testing
print '\n "Hey %s!"' %player_name
raw_input("You respond with:\n>")
print " Miaz ignoring your response continues."
print ' "Check this out. I found something neat!"'
print "You follow Miaz generally curious as to what he has found."
time.sleep(0) # Zeroed for testing
print "\n Miaz leads you to the other side of the small hill you had be relaxing on"
print "and shows you a hole that looks to be an entrance to a small cave. Without"
print "a second thought you both enter the small den to have a look around."
time.sleep(0) # Zeroed for testing
print "\n It's takes a while for your eyes to adjust to the darkness but eventually"
print "things start coming into detail. The roots of the large tree form a sort of"
print "over head dome and walls. The tangled roots somehow defying their natural"
print "inclination to dive straight down."
time.sleep(0) # Zeroed for testing
print "\n After a few moments of curiosty you begin to become bored with the place"
print "and your thoughts wander back to that shady hill and the peacefullness of"
print "it all."
time.sleep(0) # Zeroed for testing
print """\n "I found this today, pretty cool isn't it?" """
print " Miaz remarks as he continues to seek out the mysteries this place might"
print "hold."
raw_input("You respond with:\n>")
print "\n He looks a bit concerned response but suddenly the room flashes in a bright"
print "pale yellow colour."
print ' "What was that??"'
print " You look around for the source of the light but you see nothing. You and"
print "Miaz search and search but come up with nothing."
time.sleep(0) # Zeroed for testing
print "\n Just before you both give up another flash happens from a different part"
print "of the cave. And then another and another. Suddenly the cavern's interior"
print "is bathed in flashes of yellow light like a shower of shooting stars."
time.sleep(0) # Zeroed for testing
print "\n One flashing ember hands on your arm and it's legs tickle your skin. You"
print "now realize that they are a type of firefly and you must have stumbled into"
print "some sort of haven where they congregate during the day. Speaking to each"
print "other in their coded flashes."
time.sleep(0) # Zeroed for testing
print "\n You look up to tell Miaz of your discovery and before you can find him"
print "all the flashes stop, a wash of humidity and heat fall over you. You fight"
print "to hold on to the strands of your conciousness but in the end you are helpless"
print "and your heavy eyelids block the world as you lose it."
print " The world becomes dark."
print "\nYou see nothing, you hear nothing, the world is gone."
time.sleep(0) # Zeroed for testing
print "\n Your eyes start to open..."
stone_lake()

# Script starts to run here
opening_sequence()