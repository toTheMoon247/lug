# Communicator instance can get messages that recieved from LettUs Grow broker
# and provide information about the messages
class Communicator:


	def __init__(farm_controller)
		self.farm_controller = farm_controller


	# messsage: sam/bed-B2/valve open
	def is_valve_msg(messsage):
		return self.message_topic(messsage, 2) == 'valve'


	# messsage: sam/bed-B2/water_level 3
	def is_update_water_level_msg(messsage):
		return self.message_topic(message_topic, 2) == 'water_level'


	# messsage: sam/bed-A2/target Empty
	def is_empty_bed_msg:
		return self.message_topic(messsage, 2) == 'target' and msg_value('empty')

	
	# messsage: sam/bed-A2/target Empty
	def is_fill_bed_msg:
		return self.message_topic(messsage, 2) == 'target' and msg_value('fill')

	
	# message_value gets lettus-grow message and returns the message value as a string(!)
	# example 1: input = messsage: sam/bed-A2/target Empty ----> output = 'empty'
	# example 1: input = messsage: sam/bed-B2/water_level 3 ----> output = '3'. remember to cast it to int
	def get_message_value(messsage):
 		pass


 	def get_bed_label(messsage):
 		return self.messsage_topic(messsage, 1)


	################# PRIVATE ##########################
	
	# message_topic gets lettus-grow message and returns the message topic
	# by default message_topic returns the main topic
	# to get the first/second subtopic of the message you can send topic_level = 1/2/and so on...
	def message_topic(self, messsage, topic_level=0):
		pass

