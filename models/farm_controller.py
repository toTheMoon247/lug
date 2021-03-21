
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


def empty(self, node, target):
	pass


def fill(self, node, target):
	# update the bed target
	# check the bed is full
	# if not full publish 'open' to the broker
	return


def update_level(self, node, level)
	# update the farm with the current level
	# check if the bed is in the range
	# if it's in the range publish 'close'

