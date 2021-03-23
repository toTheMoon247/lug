from farm import Farm

class FarmController:

	def __init__(self, farm, communicator):

		self.farm = farm
		self.communicator = communicator
		
		# TODO add logger and communicator
		self.logger = None


	def process_a_message(self, message):
		# ignore meta messages (messsage: sam/meta/#)
		if self.communicator.is_meta_msg(message):
			return

		# if it's valve messges - no action needed at the moment (but in the next step i will use it)
		if self.communicator.is_valve_msg(message):
			return

		# for all other messages: fetch the bed label and the message value
		bed_label  = self.communicator.get_bed_label(message)
		value  = self.communicator.get_message_value(message)
		
		bed = self.farm.get_node_by_label(bed_label)
		if self.communicator.is_empty_bed_msg(message):
			return self.empty_bed(bed, value)

		if self.communicator.is_fill_bed_msg(message):
			return self.fill_bed(bed, value)

		if self.communicator.is_update_water_level_msg(message):
			return self.update_water_level(bed, value)


	########################### PRIVATE ######################################################


	def empty_bed(self, bed, target):
		# update the bed target (just in case)
		bed.set_control_target(target)
		# check if the bed is empty
		if bed.is_empty() == False:
			self.close_valve(bed)
		# if the bed is not empty, publish 'open' to the broker 
		return


	def fill_bed(self, bed, target):
		# update the bed target
		bed.set_control_target(target)
		# if the bed water level is not full open valve(and in the future:open the valve in case it's not opened)
		if bed.is_water_level_in_target() == False:
			self.open_valve(bed)
		return


	def update_water_level(self, bed, level):
		# update the farm with the current level
		bed.set_water_level(level)
		# if bed is full --> close the valve
		if bed.is_water_level_in_target(bed) == True:
			self.close_valve(bed)
		return


	def open_valve(self, bed):
		return self.set_valve(bed.get_label(), 'open')


	def close_valve(self, bed):
		return self.set_valve(bed.get_label(), 'close')


	def set_valve(self, bed_label, valve_state):
		return self.communicator.open_valve(bed_label, valve_state)