from farm import Farm

class FarmController:

	def __init__(self, farm, client):

		self.farm = farm
		self.client = client
		
		# TODO add logger and communicator
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
	
	if self.communicator.is_empty_bed_msg(message):
		return empty_bed(bed, value)

	if self.communicator.is_fill_bed_msg(message):
		return fill_bed(bed, value)

	if self.communicator.is_update_water_level_msg(message):
		return update_water_level(bed, value)


########################### PRIVATE ######################################################


def empty_bed(self, bed, target):
	# update the bed target (just in case)
	self.update_target(bed, target)
	# check if the bed is empty
	if self.farm.is_bed_empty(bed) == False:
		self.close_valve(bed)
	# if the bed is not empty, publish 'open' to the broker 
	return


def fill_bed(self, bed, target):
	# update the bed target
	self.update_target(bed, target)
	# if the bed water level is not full open valve(and in the future:open the valve in case it's not opened)
	if self.farm.is_water_level_in_target(bed) == False:
		self.open_valve(bed)
	return


def update_water_level(self, bed, level):
	# update the farm with the current level
	self.farm.update_bed_water_level(bed, level)
	# if bed is full --> close the valve
	if self.farm.is_water_level_in_target(bed) == True:
		self.close_valve(bed)
	return


def open_valve(bed):
	return self.set_valve(bed, 'open')


def close_valve(bed):
	return self.set_valve(bed, 'close')


def set_valve(bed, valve_state):
	return self.communicator.publish(bed, valve_state)