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

	def init_nodes(self):
		source = Node(1, 'source', 204, 0, 204, None)
		self.G.add_node(source)
		input('Building the levels...')

		# Outsoure me to a function
		nodes = []
		for level_index in range(1, self.levels + 1):
			current_level = []
			for row_index in range(1, self.rows + 1): 
				node = Node(row_index, level_index, 100, 20, 30, 'empty')
				self.G.add_node(node)
				current_level.append(node)
			nodes.append(current_level)	
		input(nodes)

		sink = Node(1, 'sink', 204, 0, 204, None)
		self.G.add_node(sink)

	def print_farm(self):
		nx.draw(self.G, with_labels = 1)
		pylab.show()
		return

farm = Farm(2, 2)
farm.init_nodes()
farm.print_farm()
