extends Node

var player_save= '/home/wize1/text based rpg/builds/godot/build 001/profiles/player_save.save'
var player = {
'name': '',
'race': '',
'gender': '',
'title': '',
'guild': '',
'age': '',
'body_type': '',
'height': '',
'hair_length': '',
'hair_type': '',
'facial_hair': '',
'hair_color': '',
'skin_tone': '',
'bio': '',
'spouse': '',
'pet': '',

'level': '',
'health': '',
'mana': '',
'energy': '',
'skills': '',
'spells': '',
'inventory': '',
'quests': '',

'strength': '',
'constitution': '',
'dexterity': '',
'stamina': '',
'knowledge': '',
'wisdom': '',

'head': '',
'torso': '',
'hands': '',
'legs': '',
'feet': '',
'left_hand': '',
'right_hand': '',
'accessory_1': '',
'acessory_2': '',
'accessory_3': '',

'mount': '',
'm_accessory 1': '',
'm_accessory 2': '',

'masteries': '',

'weapon_proficiency': ''}

var start_prompt = {'text': "Welcome to Heroes of Olde.",
					'options_text': ["Create character", "Load character"],
					'func': funcref(self, 'startPrompt_func'),
					'previous_prompt': null,
					'next_prompt': null}

func startPrompt_func():
	if current_prompt['options_text'][user_input] == "Create character":
		start_prompt['next_prompt'] = 'race_prompt'
	elif current_prompt['options_text'][user_input] == "Load character":
		start_prompt['next_prompt'] = 'load_prompt'
		load_player()
		load_prompt['text'] = """Do you want to load this character?

Name: {0}
Race: {1}
Gender: {2}
Age: {3}
Body type: {4}
Height: {5}
Hair length: {6}
Hair type: {7}
Facial hair: {8}
Hair color: {9}
Skin tone: {10}""".format([player['name'], player['race'], player['gender'],
						  player['age'], player['body_type'], player['height'],
						  player['hair_length'], player['hair_type'], player['facial_hair'],
						  player['hair_color'], player['skin_tone']])
		
	
var race_prompt = {'text': "Choose your character's race.",
					'options_text': ["Human", "Dwarf", "Elf", "Halfling", "Half-giant", "Go back"],
					'func': funcref(self, 'racePrompt_func'),
					'previous_prompt': 'start_prompt',
					'next_prompt': 'gender_prompt'}

func racePrompt_func():
	player['race'] = race_prompt['options_text'][user_input]
	
var gender_prompt = {'text': "Choose your character's gender.",
					 'options_text': ["Male", "Female", "Go back"],
					 'func': funcref(self, 'genderPrompt_func'),
					 'previous_prompt': 'race_prompt',
					 'next_prompt': 'customize_prompt'}

func genderPrompt_func():
	player['gender'] = gender_prompt['options_text'][user_input]
	
var customize_prompt = {'text': "Would you like to customize your character?",
						'options_text': ["Yes", "No", "Go back"],
						'func': funcref(self, 'customizePrompt_func'),
						'previous_prompt': 'gender_prompt',
						'next_prompt': 'age_prompt'}

func customizePrompt_func():
	if current_prompt['options_text'][user_input] == "Yes":
		name_prompt['previous_prompt'] = 'skinTone_prompt'
		current_prompt['next_prompt'] = 'age_prompt'
	elif current_prompt['options_text'][user_input] == "No":
		name_prompt['previous_prompt'] = 'customize_prompt'
		current_prompt['next_prompt'] = 'name_prompt'
		

var age_prompt = {'text': "What is your character's age?",
				  'options_text': ["Young", "Mature", "Old", "Go back"],
				  'func': funcref(self, 'agePrompt_func'),
				  'previous_prompt': 'customize_prompt',
				  'next_prompt': 'bodyType_prompt'}

func agePrompt_func():
	player['age'] = age_prompt['options_text'][user_input]

var bodyType_prompt = {'text': "What is your character's body type?",
					   'options_text': ["Muscular", "Fat", "Thin", "Average", "Go back"],
					   'func': funcref(self, 'bodyTypePrompt_func'),
					   'previous_prompt': 'age_prompt',
					   'next_prompt': 'height_prompt'}

func bodyTypePrompt_func():
	player['body_type'] = bodyType_prompt['options_text'][user_input]
	
var height_prompt = {'text': "What is your character's height?",
					   'options_text': ["Short", "Average", "Tall", "Go back"],
					   'func': funcref(self, 'heightPrompt_func'),
					   'previous_prompt': 'bodyType_prompt',
					   'next_prompt': 'hairLength_prompt'}

func heightPrompt_func():
	player['height'] = height_prompt['options_text'][user_input]
	
var hairLength_prompt = {'text': "What is your character's hair length?",
					   'options_text': ["Bald", "Short", "Long", "Go back"],
					   'func': funcref(self, 'hairLengthPrompt_func'),
					   'previous_prompt': 'height_prompt',
					   'next_prompt': 'hairType_prompt'}

func hairLengthPrompt_func():
	player['hair_length'] = hairLength_prompt['options_text'][user_input]
	if player['hair_length'] == "Bald":
		facialHair_prompt['previous_prompt'] = 'hairLength_prompt'
		hairLength_prompt['next_prompt']= 'facialHair_prompt'
	else:
		facialHair_prompt['previous_prompt'] = 'hairType_prompt'
		hairLength_prompt['next_prompt']= 'hairType_prompt'

var hairType_prompt = {'text': "What is your character's hair type?",
					   'options_text': ["Straight", "Curly", "Wavy", "Afro", "Braids", "Dreadlocks", "Go back"],
					   'func': funcref(self, 'hairTypePrompt_func'),
					   'previous_prompt': 'hairLength_prompt',
					   'next_prompt': 'facialHair_prompt'}

func hairTypePrompt_func():
	player['hair_type'] = hairType_prompt['options_text'][user_input]

var facialHair_prompt = {'text': "What is your character's facial hair?",
					   'options_text': ["Mustache", "Short beard", "Long beard", "Mutton chops",
										"Goatee", "Soul patch", "None", "Go back"],
					   'func': funcref(self, 'facialHairPrompt_func'),
					   'previous_prompt': 'hairType_prompt',
					   'next_prompt': 'hairColor_prompt'}

func facialHairPrompt_func():
	player['facial_hair'] = facialHair_prompt['options_text'][user_input]
	if player['hair_length'] == "Bald" and player['facial_hair'] == "None":
		skinTone_prompt['previous_prompt'] = 'facialHair_prompt'
		facialHair_prompt['next_prompt'] = 'skinTone_prompt'
	else:
		skinTone_prompt['previous_prompt'] = 'hairColor_prompt'
		facialHair_prompt['next_prompt'] = 'hairColor_prompt'
	
var hairColor_prompt = {'text': "What is your character's hair color?",
					   'options_text': ["Black", "Brown", "Blonde", "Red", "White", "Grey", "Go back"],
					   'func': funcref(self, 'hairColorPrompt_func'),
					   'previous_prompt': 'facialHair_prompt',
					   'next_prompt': 'skinTone_prompt'}

func hairColorPrompt_func():
	player['hair_color'] = hairColor_prompt['options_text'][user_input]
	
var skinTone_prompt = {'text': "What is your character's skin tone?",
					   'options_text': ["Pale", "Fair", "Tan", "Pink", "Yellow", "Red",
										"Brown", "Black", "Go back"],
					   'func': funcref(self, 'skinTonePrompt_func'),
					   'previous_prompt': 'hairColor_prompt',
					   'next_prompt': 'name_prompt'}

func skinTonePrompt_func():
	player['skin_tone'] = skinTone_prompt['options_text'][user_input]

var name_prompt = {'text': "What is your character's name?",
							'options_text': ["Go back"],
							'func': funcref(self, 'namePrompt_func'),
							'previous_prompt': 'skinTone_prompt',
							'next_prompt': 'save_prompt'}
						
func namePrompt_func():
	player['name'] = user_input
	save_prompt['text'] = """Do you want to save this character?

Name: {0}
Race: {1}
Gender: {2}
Age: {3}
Body type: {4}
Height: {5}
Hair length: {6}
Hair type: {7}
Facial hair: {8}
Hair color: {9}
Skin tone: {10}""".format([player['name'], player['race'], player['gender'],
						 player['age'], player['body_type'], player['height'],
						 player['hair_length'], player['hair_type'], player['facial_hair'],
						 player['hair_color'], player['skin_tone']])

var save_prompt = {'text': '',
					'options_text': ["Yes", "Go back"],
					'func': funcref(self, 'savePrompt_func'),
					'previous_prompt': 'name_prompt',
					'next_prompt': 'start_prompt'}

func savePrompt_func():
	save_player()

var load_prompt = {'text': '',
					'options_text': ["Yes", "Go back"],
					'func': funcref(self, 'loadPrompt_func'),
					'previous_prompt': 'start_prompt',
					'next_prompt': 'start_prompt'}
					
func loadPrompt_func():
	load_player()
							
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
		
var user_input = ''
func _on_LineEdit_return(content):
	$Control/Panel/LineEdit.clear()
	if content.is_valid_integer():
		user_input = int(content) - 1
	else:
		user_input = content
	
	if user_input in range(current_prompt['options_text'].size()):
		if current_prompt['options_text'][user_input] == "Go back":
			current_prompt = data_map[current_prompt['previous_prompt']]
			render_screen()
		else:
			current_prompt['func'].call_func()
			current_prompt = data_map[current_prompt['next_prompt']]
			render_screen()
			
	elif current_prompt == name_prompt:
		current_prompt['func'].call_func()
		current_prompt = data_map[current_prompt['next_prompt']]
		render_screen()
		

func save_player():
	var file = File.new()
	file.open(player_save, File.WRITE)
	file.store_var(player)
	file.close()

func load_player():
	var file = File.new()
	file.open(player_save, File.READ)
	player = file.get_var()
	file.close()

var data_map = {'start_prompt': start_prompt,
				'race_prompt': race_prompt,
				'gender_prompt': gender_prompt,
				'customize_prompt': customize_prompt,
				'age_prompt': age_prompt,
				'bodyType_prompt': bodyType_prompt,
				'height_prompt': height_prompt,
				'hairLength_prompt': hairLength_prompt,
				'hairType_prompt': hairType_prompt,
				'facialHair_prompt': facialHair_prompt,
				'hairColor_prompt': hairColor_prompt,
				'skinTone_prompt': skinTone_prompt,
				'name_prompt': name_prompt,
				'save_prompt': save_prompt,
				'load_prompt': load_prompt}

var current_prompt = data_map['start_prompt']
func _ready():
	$Control/Panel/LineEdit.grab_focus()
	render_screen()
