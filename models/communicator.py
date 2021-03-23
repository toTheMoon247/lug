# Communicator instance can get messages that recieved from LettUs Grow broker
# and provide information about the messages
class Communicator:


	def __init__(self, client):
		# if you want to test farm_controller ----> use mock client in the communicator
		self.client = client
		# i am not sure that communicator need to hold farm_controller. 
		# for now i will keep it commented
		# self.farm_controller = farm_controller 


	# message: sam/meta/score 0
	def is_meta_msg(self, message):
		return self.message_topic(message, 1) == 'meta' 


	# message: sam/bed-B2/valve open
	def is_valve_msg(self, message):
		return self.message_topic(message, 2) == 'valve'


	# message: sam/bed-B2/water_level 3
	def is_update_water_level_msg(self, message):
		return self.message_topic(message_topic, 2) == 'water_level'


	# message: sam/bed-A2/target Empty
	def is_empty_bed_msg(self, message):
		return self.message_topic(message, 2) == 'target' and self.get_message_value(message) == 'Empty'

	
	# message: sam/bed-A2/target Fill
	def is_fill_bed_msg(self, message):
		return self.message_topic(message, 2) == 'target' and self.get_message_value(message) == 'Fill'

	
	# message_value gets lettus-grow message and returns the message value as a string(!)
	# example 1: input = message: sam/bed-A2/target Empty ----> output = 'empty'
	# example 1: input = message: sam/bed-B2/water_level 3 ----> output = '3'. remember to cast it to int
	def get_message_value(self, message):
		return message.split()[2]


	# TODO: refactor this function. it is not well-written
	def get_bed_label(self, message):
		full_label = self.message_topic(message, 1)
		if full_label[0] == 'b':
			return f'{full_label[4]}{full_label[5]}'
		if full_label == 'tank' or full_label == 'sump':
			return full_label


	def set_bed_full_label(self, bed_label):
		if bed_label == 'tank' or bed_label == 'sump':
			return bed_label

		return f'bed-{bed_label}'


	def open_valve(self, bed_label, valve_state):
		full_label = self.set_bed_full_label(bed_label) 
		return self.client.publish(full_label, valve_state)

	################# PRIVATE ##########################
	
	# message_topic gets lettus-grow message and returns the message topic
	# by default message_topic returns the main topic
	# to get the first/second subtopic of the message you can send topic_level = 1/2/and so on...
	def message_topic(self, message, topic_level=0):
		# msg_structure for message: sam/bed-B2/valve open ---> ['message:', 'sam/bed-B2/valve', 'open']
		msg_structure = message.split()
		topics = msg_structure[1].split('/')
		return topics[topic_level]