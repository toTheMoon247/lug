import pylab
import matplotlib 
import networkx as nx
from node import Node

class Farm:

	def __init__(self, levels, rows):
		self.levels = levels
		self.rows = rows
		self.G = nx.DiGraph()
		self.nodes = []
		self.source = None
		self.sink = None

	def init_nodes(self):
		
		# Outsource me to add_node_to_farm(level, row, 'source')
		source = Node(1, 'source', 204, 0, 204, None)
		self.G.add_node(source)
		self.source = source
		
		input('Building the levels...')

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
		# Build edges from source to all nodes
		self.build_edges_from_source()

		for level in self.nodes:
			input(f'level = {level}')
			for node in level:
				input(f'node = {node}')
				# Build edges from node out to all nodes in its level and in lower levels
				self.build_edges_from(node)

		return


	def build_edges_from(self, node):
		# build edges to the same level nodes
		level_index = 1
		for level in self.nodes:
			# input(f'# build_edges_from # level_index = {level_index}, node.level = {node.level}')
			level_index += 1
			for current_node in level:
				self.G.add_edge(self.source, current_node)

		# build edges for each lower level nodes
		
		# build edges to the sink
		input(f'build edges from {node} to the sink')
		self.G.add_edge(node, self.sink)
		# input(f'build_edges_from: row = {node.row}, level = {node.level}')
		return

	def build_edges_from_source(self):
		for level in self.nodes:
			for node in level:
				self.G.add_edge(self.source, node)
		return

	def print_farm(self):
		nx.draw(self.G, with_labels = 1)
		pylab.show()
		return

farm = Farm(2, 2)
farm.init_nodes()
farm.init_edges()
farm.print_farm()
