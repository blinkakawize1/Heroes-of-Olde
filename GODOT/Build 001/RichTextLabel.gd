extends RichTextLabel

var player_save= 'user://player_save.save'
var player = {
'name': '',
'race':'',
'archetype':'',
'gender':'',
'title':'',
'guild':'',
'age':'',
'body type':'',
'height':'',
'hair length':'',
'hair type':'',
'facial hair':'',
'hair color':'',
'skin tone':'',
'bio':'',
'spouse':'',
'pet':'',

'level':'',
'health':'',
'mana':'',
'energy':'',
'skills':'',
'spells':'',
'inventory':'',
'quests':'',

'strength':'',
'constitution':'',
'dexterity':'',
'stamina':'',
'knowledge':'',
'wisdom':'',

'equipment':'',

'head':'',
'torso':'',
'hands':'',
'legs':'',
'feet':'',
'left hand':'',
'right hand':'',
'accessory 1':'',
'acessory 2':'',
'accessory 3':'',

'mount':'',
'm_accessory 1':'',
'm_accessory 2':'',

'masteries':'',

'weapon proficiency':''}

var inputNumber = ''
var q1 = 0
var q2 = 0
var q3 = 0
var q4 = 0
var q5 = 0
var q6 = 0
var q7 = 0
var q8 = 0
var q9 = 0
var q10 = 0
var q11 = 0
var q12 = 0
var q13 = 0

var races = ['Human', 'Dwarf', 'Elf', 'Halfling', 'Half-giant']
var genders = ['Male', 'Female']

func _on_lineEdit_startMenu(new_text):
	inputNumber = int(new_text)
	
	if inputNumber == 1:
			clear()
			add_text("""Choose your character's race.

1. Human
2. Dwarf
3. Elf
4. Halfling
5. Half-giant""")

			q2 = 1
			$'../LineEdit'.disconnect('text_entered', self, '_on_lineEdit_startMenu')
			$'../LineEdit'.connect('text_entered', self, '_on_lineEdit_characterCreation')


func _on_lineEdit_characterCreation(new_text):
	inputNumber = int(new_text)
	
	if q1:
		clear()
		add_text("""Choose your character's race.

1. Human
2. Dwarf
3. Elf
4. Halfling
5. Half-giant""")

		q2 = 1
		
	elif q2:
		if inputNumber-1 in range(races.size()):
			player['race'] = races[inputNumber-1]
			clear()
			add_text("""Choose your character's gender.
			
1. Male
2. Female
3. Go back""")

			q2 = 0
			q3 = 1
			
	elif q3:
		if inputNumber-1 in range(genders.size()):
			player['gender'] = genders[inputNumber-1]
			clear()
			add_text("""Assign your character's attribute points.

Available: 30

Strength: Determine's how much melee damage you can inflict with a standard attack.
Constitution: Determines your health points and your resistance to melee attacks.
Dexterity: Determines your chance to hit with any weapon, how much ranged attack damage you can inflict, your critical hit chance, and your chance to dodge.
Stamina: Determines your energy points.
Knowledge: Determines how much magic damage you can inflict.
Wisdom: Determines your resistance to magic damage and your mana points.

1. Go back""")
			q3 = 0
			q4 = 1
		
		elif inputNumber == 3:
			q3 = 0
			q1 = 1
			
	elif q4:
		clear()
		add_text("""Would you like to customize your character?

1. Yes
2. No
3. Go back""")
		q4 = 0
		q5 = 0

func save_player():
	var file = File.new()
	file.open(player_save, File.WRITE)
	file.store_var(player)
	file.close()

func load_score():
	var file = File.new()
	file.open(player_save, File.READ)
	player = file.get_var()
	file.close()
