import pylab
import matplotlib 
import networkx as nx
from node import Node

def print_node_status(node):
	node.print_status()
	return


def letters_to_numbers(c):
	return ord(c) - 64


def numbers_to_letters(n):
	return chr(ord('@')+ n) - 26


class Farm:

	def __init__(self, levels, rows):
		self.levels = levels
		self.rows = rows
		self.G = nx.DiGraph()
		self.nodes = []
		self.source = None
		self.sink = None

		self.init_nodes()
		self.init_edges()

	def init_nodes(self):
		
		print('Building the nodes...\n')
		# Outsource me to add_node_to_farm(level, row, 'source')
		source = Node(1, 'source', 204, 0, 204, None)
		self.G.add_node(source)
		self.source = source
		

		# Outsoure me to a function
		nodes = []
		for level_index in range(1, self.levels + 1):
			current_level = []
			for row_index in range(1, self.rows + 1): 
				# Outsource me to add_node_to_farm(level, row, 'bed')
				node = Node(row_index, level_index, 100, 20, 30, 'empty')
				self.G.add_node(node)
				current_level.append(node)
			nodes.append(current_level)	

		self.nodes = nodes
		
		# Outsource me to add_node_to_farm(level, row, 'sink')
		sink = Node(1, 'sink', 204, 0, 204, None)
		self.G.add_node(sink)
		self.sink = sink

	def init_edges(self):
		print('Building the edges...')
		print('---------------------')
		# Build edges from source to all nodes
		self.build_edges_from_source()

		# For each node build the edges that are going out from it 
		for level in self.nodes:
			for node in level:
				self.build_edges_from(node)

		return


	def build_edges_from(self, node):
		# build edges to the same level and lower nodes
		for level in self.nodes:
			for current_node in level:
				if node != current_node and node.level >= current_node.level:
					self.G.add_edge(node, current_node)
					print(f'added edge e({node},{current_node})')
	
		# build edges to the sink
		print(f'added edge e({node}, sink)\n')
		self.G.add_edge(node, self.sink)
		return

	def build_edges_from_source(self):
		for level in self.nodes:
			for node in level:
				self.G.add_edge(self.source, node)

		self.G.add_edge(self.source, self.sink)
		return

	def print_farm(self):
		nx.draw(self.G, with_labels = 1)
		pylab.show()
		return

	def print_farm_bluebrint(self):
		input('# Farm Blueprint #')
		print('------------------')
		nodes = self.nodes.copy()
		nodes.reverse()
		print(self.source)
		for level in nodes:
			print(level)
		print(self.sink)



	### Public interface ###
	########################
	
	# Function gets bed(node) label and return the node
	def get_node_by_label(self, node_label):
		if node_label == 'tank':
			return self.source
		if node_label == 'sump':
			return self.sink
		level = int(letters_to_numbers(node_label[0]))
		row = int(node_label[1])
		node = self.nodes[level - 1][row - 1]
		return node


	def update_target(node_label, target):
		pass

farm = Farm(2, 2)
input('printing nodes...')
# print(farm.nodes[0][0])
node = farm.get_node_by_label('sump')
node.print_status()
# node.print_node_status
# print_node_status(farm.source)
# farm.print_farm_bluebrint()
# input('\nand now the DiGraph...')
# farm.print_farm()
