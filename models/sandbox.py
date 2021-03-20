import pylab
import matplotlib 
import networkx as nx

class Person(object):
	"""docstring for Person"""
	def __init__(self, arg):
		super(Person, self).__init__()
		self.arg = arg

	def __repr__(self):
		input('Is it printing the name or the adress in the memory...?')
		return self.arg

dan = Person('Dan')
# print(dan)
G = nx.DiGraph()
G.add_node(dan)
nx.draw(G, with_labels = 1)
pylab.show()