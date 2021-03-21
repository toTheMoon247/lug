from datetime import datetime
import time
from farm import Farm

class FarmController:

	def __init__(seld, farm, client):

		self.farm = farm
		self.client = client
		self.clock_start = datetime.now()
		
		# TODO
		self.logger = None
		self.communicator = None

farm = Farm(2, 2)
farm.print_farm_bluebrint()
# fc = FarmController
