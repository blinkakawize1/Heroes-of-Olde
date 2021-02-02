extends Node

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

var previous_prompt = null
var current_prompt = start_prompt
var user_input = null

func go_back():
	current_prompt = previous_prompt
	render_screen()

var start_prompt = {'text': "Welcome to Heroes of Olde.",
					'options_text': ["Create character", "Load character"],
					'options_actions': [create_character(), load_character()],
					'single_action': null}
					
func create_character():
	render_screen()
	
func load_character():
	print("create character")
	
var race_prompt = {'text': "Choose your character's race.",
					'options_text': ["Human", "Dwarf", "Elf", "Halfling", "Half-giant", "Go back"],
					'options_actions': [assign_race()]}

func assign_race():
	player['race'] = race_prompt['options_text'][user_input]
	render_screen()
	
func render_screen():
	previous_prompt = current_prompt
	$Control/Panel/RichTextLabel.clear()
	$Control/Panel/RichTextLabel.add_text(current_prompt['text'])
	
	var index = 1
	for element in current_prompt['options_text']:
		$Control/Panel/RichTextLabel.add_text(index, element)
		index += 1

func _on_LineEdit_return(content):
	if content.is_valid_integer():
		user_input = int(content) - 1
	else:
		user_input = content - 1
		
	if user_input in range(current_prompt['options_text'].size()):
		if current_prompt['options_text'][user_input] == "Go back":
			go_back()
			return
		elif current_prompt['options_actions'].size() > 1:
			current_prompt['options_actions'][user_input]
			render_screen()
		else:
			current_prompt['options_actions']
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
	
