from farm_controller import FarmController
from communicator import Communicator
from farm import Farm


# to create unit tests for farm_controller it's recommended to use MockClient
# use it as follow:  create a Communicator object using a MockClient object
# use the Communicator object when creating a FarmController object
class MockClient:


	def __init__(self):
		return


	def publish(self, message_topic, message_payload):
		print(f'\nvalve {message_topic} successfully set to {message_payload}\n')


# these are quick & dirty unit tests for farm controller
########################################################
# create a mock client for the communicator
client = MockClient()
# create communicator
c = Communicator(client)
# create farm
farm = Farm(2, 2)
# create farn_controller
fc = FarmController(farm, c)

# mock message from the broker
print('test for empty bed meesage... should not publish anything')
empty_bed_A2 = 'message: sam/bed-A2/target Empty'
fc.process_a_message(empty_bed_A2)


print('\ntest for fill bed meesage...') 
print('The message should print: messsage: sam/bed-A2/valve/set open should produce')
fill_bed_A2 = 'message: sam/bed-A2/target Fill'
fc.process_a_message(fill_bed_A2)