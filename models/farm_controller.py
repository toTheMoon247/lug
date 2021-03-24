from farm import Farm

class FarmController:

	def __init__(self, farm, communicator):

		self.farm = farm
		self.communicator = communicator
		
		# TODO add logger and communicator
		self.logger = None


	def process(self, topics, value ):
		print(f'processing message: {topics} {value}')

		# for all other messages: fetch the bed label and the message value
		if self.communicator.is_empty_bed_msg(topics, value):
			bed_label  = self.communicator.get_bed_label(topics)
			if bed_label != 'A1':
				return
			bed = self.farm.get_node_by_label(bed_label)
			self.logger.log('process ------>> I need to empty A1')
			self.empty_bed(bed, value)
			return

		if self.communicator.is_fill_bed_msg(topics, value):
			# print(f'processing message: {topics} {value} is_fill_bed_msg')
			bed_label  = self.communicator.get_bed_label(topics)
			if bed_label != 'A1':
				return
			bed = self.farm.get_node_by_label(bed_label)
			self.logger.log('process ------>> I need to fill A1')
			self.fill_bed(bed, value)
			return

		if self.communicator.is_update_water_level_msg(topics, value):
			# print(f'processing message: {topics} {value} is_update_water_level_msg')
			bed_label  = self.communicator.get_bed_label(topics)
			if bed_label != 'A1':
				return
			bed = self.farm.get_node_by_label(bed_label)
			self.logger.log('process ------>> I need to update A1 and close it if its full')
			self.update_water_level(bed, value)
			return


		return


	# TODO: refactor me
	def set_client(self, client):
		self.communicator.client = client
		return True


	def set_logger(self, logger):
		self.logger = logger
		return True
	########################### PRIVATE ######################################################


	def empty_bed(self, bed, target):
		# update the bed target (just in case)
		bed.set_control_target(target)
		# check if the bed is empty
		if bed.is_empty() == False:
			self.logger.log(f'FarmController/empty_bed---> I am not doing anything at the moment!')
			self.close_valve(bed)
		# if the bed is not empty, publish 'open' to the broker 
		return


	def fill_bed(self, bed, target):
		# update the bed target
		bed.set_control_target(target)
		# if the bed water level is not full open valve(and in the future:open the valve in case it's not opened)
		if bed.is_water_level_in_target() == False:
			self.logger.log('FarmController/fill_bed ---> I am not doing anything at the moment')
			return
			self.logger.log(f'A1 target was changed to fill and water_level are {bed.get_water_level}')
			self.logger.log(f'FarmController---> I am opening A1 valve because water are not in target and need to fill it!')
			self.open_valve(bed)
		return


	def update_water_level(self, bed, level):
		# update the farm with the current level
		bed.set_water_level(level)
		# if bed is full --> close the valve
		if bed.is_water_level_in_target() == True:
			print(f'FarmController---> I am closing A1 valve because water are in target')
			self.close_valve(bed)
		return


	def open_valve(self, bed):
		return self.set_valve(bed.get_label(), 'open')


	def close_valve(self, bed):
		return self.set_valve(bed.get_label(), 'close')


	def set_valve(self, bed_label, valve_state):
		return self.communicator.set_valve(bed_label, valve_state)