# TODO: outsource me to utils
def print_node_status(node):
	node.print_status()
	return


# TODO: outsource me to utils
def letters_to_numbers(c):
	return ord(c) - 64


# TODO: outsource me to utils
def numbers_to_letters(n):
	return chr(ord('@')+ n)

class Node:

	def __init__(self, row, level, capacity, target_min, target_max, control_target, water_level=0, valve_state='close'):
		self.row = row
		self.level = level
		self.capacity = capacity,
		self.target_min = target_min
		self.target_max = target_max
		self.control_target = control_target
		self.water_level = water_level
		self.valve_state = valve_state
		self.label = self.set_label(numbers_to_letters((self.row)), self.level)


	def set_label(self, row, level):
		if level == 'source': 
			return f'source'
		if level == 'sink': 
			return f'sink'
		return f'{row}{level}'


	def __str__(self):
		return self.label


	def __repr__(self):
	    return self.__str__()


	def print_status(self):
		print(f'{self.label} status:')
		print(f'control_target = {self.control_target}')
		print(f'water_level = {self.water_level}')
		print(f'valve_state = {self.valve_state}')


############## PUBLIC Interface ###########################
	def get_label(self):
		return self.label


	def set_control_target(self, target):
		print(f'Node/set_control_target ----> I am updating the target to be {target}')
		self.control_target = target
		return True


	def is_empty(self):
		return self.water_level == 0


	def is_water_level_in_target(self):
		level = int(self.water_level)
		is_in_target = level >= self.target_min and level <= self.target_max
		print(f'Node/set_control_target ----> I am checking if water_level in target for A1. result = {is_in_target}')
		return is_in_target

	def set_water_level(self, water_level):
		print(f'Node/set_control_target ----> I am updating the water level to {water_level}')
		self.water_level = water_level
		return True

	def get_water_level(self):
		return self.water_level