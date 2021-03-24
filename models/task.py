import time
import paho.mqtt.client as mqtt
from farm_controller import FarmController
from communicator import Communicator
from farm import Farm
from logger import Logger


# do not change
HOST = 'ec2-35-177-59-107.eu-west-2.compute.amazonaws.com'
PORT = 16237
USER = 'sam'
PASSWD = 'jNyFi9UeVNglDfxyLJQR'

time.sleep(5)
#############################################################################

# create a communicator
c = Communicator('mock')
# create 'Easy' level farm
farm = Farm(2, 2)
# create a FarmController instance
fc = FarmController(farm, c)

#############################################################################
# if you dont see a "connection successfull" message. email chelsee imediatly
# becuase this should definatly work
def on_connect(client, userdata, flags, rc):
    print("Connection Succesfull")


def message_recieved(client, userdata, message):
    value = message.payload.decode()
    fc.process(message.topic, value)

    # print(f'messsage: {message.topic} {value}')


def valve_opened(client, userdata, message):
    value = message.payload.decode()
    print(f'\nvalve {message.topic} successfully set to {value}\n')


def mode_set(client, userdata, message):
    value = message.payload.decode()
    print(f'\nmode successfully set to {value}\n')


client = mqtt.Client()
client.username_pw_set(USER, PASSWD)
client.on_connect = on_connect
client.connect(HOST, PORT, keepalive=60)
#############################################################################
# set client to be the mqtt client
fc.set_client(client)

logger = Logger()
fc.set_logger(logger)

############################### start the loop ##############################
client.loop_start()

client.subscribe(f'{USER}/#')
client.message_callback_add(f"{USER}/#", message_recieved)
client.message_callback_add(f"{USER}/meta/mode", mode_set)

# calling set mode restarts the simulation
client.publish(f"{USER}/meta/mode/set", 'easy')
#client.publish(f"{USER}/meta/mode/set", 'medium')
#client.publish(f"{USER}/meta/mode/set", 'hard')

# wait one sec after setting mode to ensure restart has completed
time.sleep(2)

# open some valves and what the water flow :)
client.message_callback_add(f"{USER}/#/valve", valve_opened)

# client.publish(f"{USER}/tank/valve/set", 'open')
# client.publish(f"{USER}/bed-A1/valve/set", 'open')
time.sleep(2)
#client.publish(f"{USER}/bed-A1/valve/set", 'close')
# sam/A1/valve/set close


tick = 2
while True:
	time.sleep(2)
	print(f'\n **** tick {tick} ****')
	
	if tick == 3:
		print('publishig A1...')
		client.publish(f"{USER}/bed-A1/valve/set", 'open')

	if tick == 4:
		print('publishig tank ...')
		client.publish(f"{USER}/tank/valve/set", 'open')
	
	# recieve new messages
		# recieve messages about the water-level
		# recieve messages about the target
		# recieve messages about the score
	# send updates to the farm
	# get updates from the farm
	# update the broker
	tick += 1

client.loop_stop()