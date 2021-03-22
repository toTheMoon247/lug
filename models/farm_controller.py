
from farm import Farm

class FarmController:

	def __init__(self, farm, client):

		self.farm = farm
		self.client = client
		
		# TODO test
		self.logger = None
		self.communicator = None


def process_a_message(self, message):
	# ignore meta messages (messsage: sam/meta/#)
	if self.communicator.is_meta_msg(message):
		return

	# if it's valve messges - no action needed at the moment (but in the next step i will use it)
	if self.communicator.is_valve_msg(message):
		return

	# for all other messages: fetch the bed label and the message value
	bed  = self.communicator.extract_bed_label_from_msg(message)
	value  = self.communicator.extract_value_label_from_msg(message)
	
	if self.communicator.is_water_level_msg(message):
		return self.update_bed_level_and_publish_accordingly(bed, value)

	if self.communicator.is_target_message(message):
		return self.set_target_bed_and_publish_accordingly(bed, value)


	# if it's an action message:
		# Empty ---> (1) check if it's empty
		#			 (2) if not - empty the bed

		# Fill  ---> (1) check if bed is full
		# 			 (2) if not fill it (publish 'open' to the broker)

	# if it's a level message ---> (1) update_level
	#							   (2) if level is in the range('in target') switch off (publish 'close' to the broker)


def set_target_bed_and_publish_accordingly(self, bed, target):
	# update the bed target (just in case)
	self.farm.update_target(bed, target)
	# check if the bed is empty
	if self.farm.is_bed_target(bed, target) == False:
		self.communicator.publish(bed, 'open')
	# if the bed is not empty, publish 'open' to the broker 
	return


def update_bed_level_and_publish_accordingly(self, node, level):
	# update the farm with the current level
	self.farm.update_bed_water_level(node, leve)
	if farm.bed_is_full(node) == True
		self.communicator.publish(node, 'close')
	# check if the bed is in the range
	# if it's in the range publish 'close'


def publish:
	pass