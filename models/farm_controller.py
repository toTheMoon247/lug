
from farm import Farm

class FarmController:

	def __init__(self, farm, client):

		self.farm = farm
		self.client = client
		
		# TODO test
		self.logger = None
		self.communicator = None


def process_a_message(self, message):
	# if it's an action message:
		# Empty ---> (1) check if it's empty
		#			 (2) if not - empty the bed

		# Fill  ---> (1) check if bed is full
		# 			 (2) if not fill it (publish 'open' to the broker)

	# if it's a level message ---> (1) update_level
	#							   (2) if level is in the range('in target') switch off (publish 'close' to the broker)
	pass


def empty_bed(self, node, target):
	# update the bed target (just in case)
	self.farm.update_target(node, target)
	# check if the bed is empty
	if self.farm.bed_is_empty(node) == False:
		self.communicator.publish(node, 'open')
	# if the bed is not empty, publish 'open' to the broker 
	return


def fill_bed(self, node, target):
	# update the bed target
	self.farm.update_target(node, target)
	# check the bed is full
	if self.farm.bed_is_full(node) == False:
		self.communicator.publish(node, 'open')
	# if not full publish 'open' to the broker
	return


def update_bed_level(self, node, level):
	# update the farm with the current level
	self.farm.update_bed_level(node, leve)
	if farm.bed_is_full(node) == true
		self.communicator.publish(node, 'open')
	# check if the bed is in the range
	# if it's in the range publish 'close'


def publish:
	pass