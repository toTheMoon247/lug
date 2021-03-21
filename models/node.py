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
		self.label = self.set_label(self.row_number_to_char(self.row), self.level)

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

	def row_number_to_char(self, row):
		converter = {
		        1: "A",
		        2: "B",
		        3: "C",
		        4: "D",
		        5: "E",
		        6: "F",
		        7: "G",
		        8: "H",
		        9: "I",
		        10: "J",
		        11: "K",
		        12: "L"
		    }
		return converter[row]

	def print_status(self):
		print(f'{self.label} status:')
		print(f'control_target = {self.control_target}')
		print(f'water_level = {self.water_level}')
		print(f'valve_state = {self.valve_state}')

	def get_label(self):
		return self.label

a1 = Node(1, 1, 100, 20, 30, 'empty')
a1.print_status()
# source = Node('A', 'source', 100, 20, 30, 'empty')
# a1 = Node(3, 1, 100, 20, 30, 'empty')
# a1.print_label()
