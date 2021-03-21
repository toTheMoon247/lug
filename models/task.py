import time
import paho.mqtt.client as mqtt
import random

# do not change
HOST = 'ec2-35-177-59-107.eu-west-2.compute.amazonaws.com'
PORT = 16237
USER = 'sam'
PASSWD = 'jNyFi9UeVNglDfxyLJQR'


# if you dont see a "connection successfull" message. email chelsee imediatly
# becuase this should definatly work
def on_connect(client, userdata, flags, rc):
	print("Connection Succesfull")


def message_recieved(client, userdata, message):
	value = message.payload.decode()
	print(f'messsage: {message.topic} {value}')


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
client.loop_start()

client.subscribe(f'{USER}/#', 1)
client.message_callback_add(f"{USER}/#", message_recieved)
client.message_callback_add(f"{USER}/meta/mode", mode_set)

# calling set mode restarts the simulation
client.publish(f"{USER}/meta/mode/set", 'easy')
# client.publish(f"{USER}/meta/mode/set", 'medium')
#client.publish(f"{USER}/meta/mode/set", 'hard')

# wait one sec after setting mode to ensure restart has completed

# open some valves and what the water flow :)
time.sleep(1)
client.message_callback_add(f"{USER}/#/valve", valve_opened)
time.sleep(1)
print('******************** publishing... ***************************')
client.publish(f"{USER}/tank/valve/set", 'open')
client.publish(f"{USER}/bed-B2/valve/set", 'open')

print('\n\n')

tick = 2
while True:
	print( f'##### tick {tick} ####')
	if tick == 6:
		client.publish(f"{USER}/bed-B1/valve/set", 'open')
	if tick == 9:
		client.publish(f"{USER}/tank/valve/set", 'close')
	if tick == 10:
		client.publish(f"{USER}/bed-A1/valve/set", 'open')
	time.sleep(2)
	print('\n')
	tick += 1

	# client.publish(f"{USER}/bed-B1/valve/set", 'open')

client.loop_stop()