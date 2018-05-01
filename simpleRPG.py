# It's no doubt that this code is dumb and needs to be redone

#Simple RPG - RPG Mechanics Tester
#On-going project to investigate RPG mechanics, test them out, and attempt to make them fun for non-rpg players.
#
#** Please note that this is part of a learning exercise **
#
#To do:
#Lay out plans for this repo (goals, language)
#Plan stages and phases
#Version 1.0
#
#2 characters
#2 properties (Hitpoints, Speed)
#Hitpoints: When 0 or below character is considered dead
#Speed: Determines who attacks first
#Determines who attacks first and splits into two loops
#Loops until one character's hitpoints reach zero
#Plans
#Functions
#
#Death Check
#Winner Check
#Damage Calculation
#Features
#
#Random stats ( in a range )
#Finds first attacker ( looks at player speed )
#Weapon choices
#Armor choices
#Power choices
#Alter stats based on choices
#Loops until Death Check = true
#Adjusted chance for one player to win to make it funner for them

import random

critmiss = 0

# Checks if either character is dead
def deathchk(hp1, hp2):
	if hp1 <= 0 or hp2 <= 0:
		return True
	else:
		return False
		
# Sets the winner and loser
def winlose(hp1, hp2):
	if hp1 <= 0:
		return atk1
	elif hp2 <= 0:
		return atk2
	else:
		print "?? Error no one has died yet, this should not have been called."

# Calculates if attack lands and how much damage it does
def damage(atk, defen, STR, osp, oarm, obleed, crit):
	# clears out these values, in case they had been previously set
	critmiss = 0
	tmpbleed = 0
	# if the defender is bleeding generate bleed value
	if obleed:
		tmpbleed = random.randrange(1, 4)
	# finds if the attack misses
	if random.randrange(0, 100) < (10 + osp):
		# if the attack misses, finds if it critically misses
		if random.randrange(0, 100) < 15:
			critmiss = random.randrange(1, 5)
			print "**~~ Critical Miss!! ~~**"
			print "%s hurts themselves and takes %d points of damage." % (atk, critmiss)
			return 0
		# if it doesn't critically miss then must just miss
		else:
			print "~~WOOSH~~ %s misses!" % atk
			return 0
	# finds if the the hit is a critical hit
	elif random.randrange(0, 100) < (15 + crit):
		tmpdmg = (random.randrange(22, 33) + STR) - oarm
		if tmpdmg < 0:
			tmpdmg = 0
		print "*!!Critical Strike!!*"
		if tmpbleed > 0:
			print "%s strikes for %d points of damage." % (atk, tmpdmg),
			tmpdmg = tmpdmg + tmpbleed
			print "%s bleeds for %d damage." % (defen, tmpbleed)
		else:
			print "%s stikes for %d points of damage!" % (atk, tmpdmg)			
		return tmpdmg
	# if not a miss or crit must be a normal hit
	else: 
		tmpdmg = (random.randrange(1, 20) + STR) - oarm
		if tmpdmg < 0:
			tmpdmg = 0
		if tmpbleed > 0:
			print "%s strikes for %d points of damage." % (atk, tmpdmg),
			tmpdmg = tmpdmg + tmpbleed
			print "%s bleeds for %d damage." % (defen, tmpbleed)
		else:
			print "%s strikes for %d points of damage." % (atk, tmpdmg)
		return tmpdmg

CharA = "Sally"
CharB = "Shane"

raw_input("\n*** %s vs %s!! *** \nPress enter to calculate stats: \n" % (CharA, CharB))

# Sets player A and B's initial health, speed, strength, and armor
Ahp = random.randrange(51, 115)
print "%s has %d hitpoints." % (CharA, Ahp)
Asp = random.randrange(15, 60)
print "%s is %d fast." % (CharA, Asp)
aSTR = 1
aARM = 1
aBleed = False
aCrit = 1

Bhp = random.randrange(51, 100)
print "%s has %d hitpoints." % (CharB, Bhp)
Bsp = random.randrange(1, 50)
print "%s is %d fast." % (CharB, Bsp)
bSTR = 0
bARM = 0
bBleed = False
bCrit = 0

# Finds who has better initial stats, lets user know
if (Ahp + Asp) > (Bhp + Bsp):
	beststats = "Nice stats %s!" % CharA
else:
	beststats = "Nice stats %s!" % CharB

raw_input("\n%s\nPress enter to continue:\n" % beststats)				

WeapList = ["a) Sword: +dmg", "b) Axe: +bleed", "c) Great Axe: +crit", "d) Great Sword: ++dmg, -sp", "e) Bow: +sp"]
printWeap = "\n".join(WeapList)

AweapChoice = raw_input("%s, please choose your weapon: \n%s\n>" % (CharA, printWeap))
BweapChoice = raw_input("%s, please choose your weapon: \n%s\n>" % (CharB, printWeap))

ArmorList = ["a) Leather: +arm", "b) Chainmail: +arm, -sp", "c) Plate Armor: ++arm, --sp", "d) Magic Armor: +sp", "e) Shield: ++arm, --crit"]
printArmor = "\n".join(ArmorList)

AarmorChoice = raw_input("%s, please choose your armor: \n%s\n>" % (CharA, printArmor))
BarmorChoice = raw_input("%s, please choose your armor: \n%s\n>" % (CharB, printArmor))

PowerList = ["a) Health Boost: +hp", "b) Redbull: +sp", "c) Strength Boost: +STR", "d) Magic Shield: +ARM"]
printPower = "\n".join(PowerList)

ApowerChoice = raw_input("%s, please choose your power: \n%s\n>" % (CharA, printPower))
BpowerChoice = raw_input("%s, please choose your power: \n%s\n>" % (CharB, printPower))

# Evaluate player A's weapon choice, alter stats
if str.lower(AweapChoice) == "a":
	aSTR = aSTR + random.randrange(3, 10)
	print "\n%s chose the sword!" % CharA
elif str.lower(AweapChoice) == "b":
	aSTR = aSTR + random.randrange(2, 7)
	bBleed = True
	print "\n%s chose the axe!" % CharA
elif str.lower(AweapChoice) == "c":
	aSTR = aSTR + random.randrange(2, 10)
	aCrit = random.randrange(5, 15)
	print "\n%s chose the Great Axe!" % CharA
elif str.lower(AweapChoice) == "d":
	aSTR = aSTR + random.randrange(3, 17)
	Asp = Asp - random.randrange(1, 10)
	if Asp <= 0:
		Asp = 0
	print "\n%s chose the Great Sword!" % CharA
elif str.lower(AweapChoice) == "e":
	aSTR = aSTR + random.randrange(1, 8)
	Asp = Asp + random.randrange(5, 15)
	print "\n%s chose the bow." % CharA
else:
	print "Not a good idea, no weapon selected for %s." % CharA

# Evaluate player B's weapon choice, alter stats
if str.lower(BweapChoice) == "a":
	bSTR = bSTR + random.randrange(3, 10)
	print "\n%s chose the sword!" % CharB
elif str.lower(BweapChoice) == "b":
	bSTR = bSTR + random.randrange(2, 7)
	aBleed = True
	print "\n%s chose the axe!" % CharB
elif str.lower(BweapChoice) == "c":
	bSTR = bSTR + random.randrange(2, 10)
	bCrit = random.randrange(5, 15)
	print "\n%s chose the Great Axe!" % CharB
elif str.lower(BweapChoice) == "d":
	bSTR = bSTR + random.randrange(3, 17)
	Bsp = Bsp - random.randrange(1, 10)
	if Bsp <= 0:
		Bsp = 0
	print "\n%s chose the Great Sword!" % CharB
elif str.lower(BweapChoice) == "e":
	bSTR = bSTR + random.randrange(1, 8)
	Bsp = Bsp + random.randrange(5, 15)
	print "\n%s chose the bow." % CharB
else:
	print "Not a good idea, no weapon selected for %s." % CharB

# Evaluate player A's armor choice, alter stats
if str.lower(AarmorChoice) == "a":
	aARM = aARM + random.randrange(2, 6)
	print "\n%s chose leather armor." % CharA
elif str.lower(AarmorChoice) == "b":
	aARM = aARM + random.randrange(3, 9)
	Asp = Asp - random.randrange(3, 6)
	if Asp <= 0:
		Asp = 0
	print "\n%s chose chainmail armor." % CharA
elif str.lower(AarmorChoice) == "c":
	aARM = aARM + random.randrange(4, 14)
	Asp = Asp - random.randrange(4, 9)
	if Asp <= 0:
		Asp = 0
	print "\n%s chose plate armor." % CharA
elif str.lower(AarmorChoice) == "d":
	aARM = aARM + random.randrange(1, 5)
	Asp = Asp + random.randrange(5, 15)
	print "\n%s chose the magic armor." % CharA
elif str.lower(AarmorChoice) == "e":
	aARM = aARM + 10
	aCrit = aCrit - 15
	if aCrit <= 0:
		aCrit = 0
	print "\n%s chose the shield." % CharA
else:
	print "Not a good idea, no armor selected for %s." % CharA

# Evaluate player B's armor choice, alter stats
if str.lower(BarmorChoice) == "a":
	bARM = bARM + random.randrange(2, 6)
	print "\n%s chose leather armor." % CharB
elif str.lower(BarmorChoice) == "b":
	bARM = bARM + random.randrange(3, 9)
	Bsp = Bsp - random.randrange(3, 6)
	if Bsp <= 0:
		Bsp = 0
	print "\n%s chose chainmail armor." % CharB
elif str.lower(BarmorChoice) == "c":
	bARM = bARM + random.randrange(4, 14)
	Bsp = Bsp - random.randrange(4, 9)
	if Bsp <= 0:
		Bsp = 0
	print "\n%s chose plate armor." % CharB
elif str.lower(BarmorChoice) == "d":
	bARM = bARM + random.randrange(1, 5)
	Bsp = Bsp + random.randrange(5, 15)
	print "\n%s chose the magic armor." % CharB
elif str.lower(BarmorChoice) == "e":
	bARM = bARM + 10
	bCrit = bCrit - 15
	if bCrit <= 0:
		bCrit = 0
	print "\n%s chose the shield." % CharB
else:
	print "Not a good idea, no armor selected for %s." % CharB

# Evaluate player A's power choice, alter stats
if str.lower(ApowerChoice) == "a":
	Ahp = Ahp + random.randrange(10, 25)
	print "\n%s chose health boost." % CharA
elif str.lower(ApowerChoice) == "b":
	Asp = Asp + random.randrange(10, 15)
	print "\n%s chose a redbull!" % CharA
elif str.lower(ApowerChoice) == "c":
	aSTR = aSTR + random.randrange(7, 10)
	print "\n%s chose strength boost." % CharA
elif str.lower(ApowerChoice) == "d":
	aARM = aARM + random.randrange(7, 10)
	print "\n%s chose the magic shield." % CharA
else:
	print "Not a good idea, no power selected for %s." % CharA

# Evaluate player B's power choice, alter stats
if str.lower(BpowerChoice) == "a":
	Bhp = Bhp + random.randrange(10, 25)
	print "\n%s chose health boost." % CharB
elif str.lower(BpowerChoice) == "b":
	Bsp = Bsp + random.randrange(10, 15)
	print "\n%s chose a redbull!" % CharB
elif str.lower(BpowerChoice) == "c":
	bSTR = bSTR + random.randrange(7, 10)
	print "\n%s chose strength boost." % CharB
elif str.lower(BpowerChoice) == "d":
	bARM = bARM + random.randrange(7, 10)
	print "\n%s chose the magic shield." % CharB
else:
	print "Not a good idea, no power selected for %s." % CharB
	
# If player A is faster set them as attack 1, else player B is attacker 1
if Asp >= Bsp:
	atk1 = CharA
	atk1hp = Ahp
	atk1STR = aSTR
	atk1ARM = aARM
	atk1sp = Asp
	atk1crit = aCrit
	atk1bleed = aBleed
	atk2 = CharB
	atk2hp = Bhp
	atk2STR = bSTR
	atk2ARM = bARM
	atk2sp = Bsp
	atk2crit = bCrit
	atk2bleed = bBleed
else:
	atk1 = CharB
	atk1hp = Bhp
	atk1STR = bSTR
	atk1ARM = bARM
	atk1sp = Bsp
	atk1crit = bCrit
	atk1bleed = bBleed
	atk2 = CharA
	atk2hp = Ahp
	atk2STR = aSTR
	atk2ARM = aARM
	atk2sp = Asp
	atk2crit = aCrit
	atk2bleed = aBleed

print "\n%s attacks first!" % atk1

# Runs a loop until one player is dead
while not deathchk(atk1hp, atk2hp):
	raw_input("\n**Press enter to start the round**\n")
	dmg = damage(atk1, atk2, atk1STR, atk2sp, atk2ARM, atk2bleed, atk1crit)
	if dmg > 0:
		atk2hp = atk2hp - dmg
		if atk2hp < 0:
			atk2hp = 0
		print "%s has %d health remaining.\n" % (atk2, atk2hp)
	elif critmiss > 0:
		atk1hp = atk1hp - critmiss
	if not deathchk(atk1hp, atk2hp):
		dmg = damage(atk2, atk1, atk2STR, atk1sp, atk1ARM, atk1bleed, atk2crit)
		if dmg > 0:
			atk1hp = atk1hp - dmg
			if atk1hp < 0:
				atk1hp = 0
			print "%s has %d health remaining.\n" % (atk1, atk1hp)
		elif critmiss > 0:
			atk2hp = atk2hp - critmiss
			
loser = winlose(atk1hp, atk2hp)
print "%s has been defeated!!\n" % loser