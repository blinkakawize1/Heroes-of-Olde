extends Node

var player_save= 'user://player_save.save'
var player = {
'name': '',
'race':'',
'gender':'',
'title':'',
'guild':'',
'age':'',
'body_type':'',
'height':'',
'hair_Length':'',
'hair_type':'',
'facial_hair':'',
'hair_color':'',
'skin_tone':'',
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
'left_hand':'',
'right_hand':'',
'accessory_1':'',
'acessory_2':'',
'accessory_3':'',

'mount':'',
'm_accessory 1':'',
'm_accessory 2':'',

'masteries':'',

'weapon_proficiency':''}

var user_input = null
var previous_prompt = null
var current_prompt = null

var start_prompt = {'text': "Welcome to Heroes of Olde.",
					'options_text': ["Create character", "Load character"],
					'options_actions': [funcref(self, 'create_character'), funcref(self, 'load_character')],
					'previous_prompt': null,
					'next_prompt': race_prompt}

func create_character():
	print("create character")
	
func load_character():
	print("load character")
	
var race_prompt = {'text': "Choose your character's race.",
					'options_text': ["Human", "Dwarf", "Elf", "Halfling", "Half-giant", "Go back"],
					'options_actions': [funcref(self, 'assign_race')],
					'previous_prompt': start_prompt,
					'next_prompt': gender_prompt}

func assign_race():
	player['race'] = race_prompt['options_text'][user_input]
	
var gender_prompt = {'text': "Choose your character's gender.",
					 'options_text': ["Male", "Female", "Go back"],
					 'options_actions': [funcref(self, 'assign_gender')],
					 'previous_prompt': race_prompt,
					'next_prompt': customize_prompt}

func assign_gender():
	player['gender'] = gender_prompt['options_text'][user_input]
	
var customize_prompt = {'text': "Would you like to customize your character?",
						'options_text': ["Yes", "No", "Go back"],
						'options_actions': [funcref(self, 'customize_character')],
						'previous_prompt': gender_prompt,
						'next_prompt': age_prompt}

func customize_character():
	print("customize character")

var age_prompt = {'text': "What is your character's age?",
				  'options_text': ["Young", "Mature", "Old", "Go back"],
				  'options_actions': [funcref(self, 'assign_age')],
				  'previous_prompt': customize_prompt,
				  'next_prompt': bodyType_prompt}

func assign_age():
	player['age'] = age_prompt['options_text'][user_input]

var bodyType_prompt = {'text': "What is your character's body type?",
					   'options_text': ["Muscular", "Fat", "Thin", "Average", "Go back"],
					   'options_actions': [funcref(self, 'assign_bodyType')],
					   'previous_prompt': age_prompt,
					   'next_prompt': height_prompt}

func assign_bodyType():
	player['body_type'] = bodyType_prompt['options_text'][user_input]
	
var height_prompt = {'text': "What is your character's height?",
					   'options_text': ["Short", "Average", "Tall", "Go back"],
					   'options_actions': [funcref(self, 'assign_height')],
					   'previous_prompt': bodyType_prompt,
					   'next_prompt': hairLength_prompt}

func assign_height():
	player['height'] = height_prompt['options_text'][user_input]
	
var hairLength_prompt = {'text': "What is your character's hair length?",
					   'options_text': ["Bald", "Short", "Long", "Go back"],
					   'options_actions': [funcref(self, 'assign_hairLength')],
					   'previous_prompt': height_prompt,
					   'next_prompt': hairType_prompt}

func assign_hairLength():
	player['hair_length'] = hairLength_prompt['options_text'][user_input]
	if player['hair_length'] == "Bald":
		facialHair_prompt['previous_prompt'] = hairLength_prompt
		hairLength_prompt['next_prompt']= facialHair_prompt
	else:
		facialHair_prompt['previous_prompt'] = hairType_prompt
		hairLength_prompt['next_prompt']= hairType_prompt

var hairType_prompt = {'text': "What is your character's hair type?",
					   'options_text': ["Straight", "Curly", "Wavy", "Afro", "Braids", "Dreadlocks", "Go back"],
					   'options_actions': [funcref(self, 'assign_hairType')],
					   'previous_prompt': hairLength_prompt,
					   'next_prompt': facialHair_prompt}

func assign_hairType():
	player['hair_type'] = hairType_prompt['options_text'][user_input]

var facialHair_prompt = {'text': "What is your character's facial hair?",
					   'options_text': ["Mustache", "Short beard", "Long beard", "Mutton chops",
										"Goatee", "Soul patch", "None", "Go back"],
					   'options_actions': [funcref(self, 'assign_facialHair')],
					   'previous_prompt': hairType_prompt,
					   'next_prompt': hairColor_prompt}

func assign_facialHair():
	player['facial_hair'] = facialHair_prompt['options_text'][user_input]
	if player['hair_length'] == "Bald" and player['facial_hair'] == "None":
		skinTone_prompt['previous_prompt'] = facialHair_prompt
		facialHair_prompt['next_prompt'] = skinTone_prompt
	else:
		skinTone_prompt['previous_prompt'] = hairColor_prompt
		facialHair_prompt['next_prompt'] = hairColor_prompt
	
var hairColor_prompt = {'text': "What is your character's hair color?",
					   'options_text': ["Black", "Brown", "Blonde", "Red", "White", "Grey", "Go back"],
					   'options_actions': [funcref(self, 'assign_hairColor')],
					   'previous_prompt': facialHair_prompt,
					   'next_prompt': skinTone_prompt}

func assign_hairColor():
	player['hair_color'] = hairColor_prompt['options_text'][user_input]
	
var skinTone_prompt = {'text': "What is your character's skin tone?",
					   'options_text': ["Pale", "Fair", "Tan", "Pink", "Yellow", "Red",
										"Brown", "Black", "Go back"],
					   'options_actions': [funcref(self, 'assign_skinTone')],
					   'previous_prompt': hairColor_prompt,
					   'next_prompt': name_prompt}

func assign_skinTone():
	player['skin_tone'] = skinTone_prompt['options_text'][user_input]

var name_prompt = {'text': "What is your character's name?",
							'options_text': ["Go back"],
							'options_actions': [funcref(self, 'assign_characterName')],
							'previous_prompt': skinTone_prompt,
							'next_prompt': save_prompt}
						
func assign_name():
	player['name'] = user_input
	
var save_prompt = {'text': "Do you want to save this character?",
							'options_text': ["Yes", "Go back"],
							'options_actions': [funcref(self, 'save_player')],
							'previous_prompt': name_prompt,
							'next_prompt': null}

func render_screen():
	$Control/Panel/RichTextLabel.clear()
	$Control/Panel/RichTextLabel.add_text(current_prompt['text'])
	$Control/Panel/RichTextLabel.add_text('\n')
	
	var index = 1
	for element in current_prompt['options_text']:
		$Control/Panel/RichTextLabel.add_text('\n')
		$Control/Panel/RichTextLabel.add_text(str(index, '. '))
		$Control/Panel/RichTextLabel.add_text(element)
		index += 1

func _on_LineEdit_return(content):
	$Control/Panel/LineEdit.clear()
	if content.is_valid_integer():
		user_input = int(content) - 1
	else:
		user_input = content
	
	if user_input in range(current_prompt['options_text'].size()):
		if current_prompt['options_text'][user_input] == "Go back":
			current_prompt = current_prompt['previous_prompt']
			render_screen()
		elif current_prompt['options_actions'].size() > 1:
			current_prompt['options_actions'][user_input].call_func()
			current_prompt = current_prompt['next_prompt']
			render_screen()
		else:
			current_prompt['options_actions'][0].call_func()
			current_prompt = current_prompt['next_prompt']
			render_screen()

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

func _ready():
	$Control/Panel/LineEdit.grab_focus()
	current_prompt = start_prompt
	render_screen()
