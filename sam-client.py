import time
import paho.mqtt.client as mqtt

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

client.subscribe(f'{USER}/#')
client.message_callback_add(f"{USER}/#", message_recieved)
client.message_callback_add(f"{USER}/meta/mode", mode_set)


# calling set mode restarts the simulation
client.publish(f"{USER}/meta/mode/set", 'easy')
# client.publish(f"{USER}/meta/mode/set", 'medium')
# client.publish(f"{USER}/meta/mode/set", 'hard')

# wait one sec after setting mode to ensure restart has completed
time.sleep(1)

# open some valves and what the water flow :)
client.message_callback_add(f"{USER}/#/valve", valve_opened)
# client.publish(f"{USER}/tank/valve/set", 'open')
# client.publish(f"{USER}/bed-A1/valve/set", 'open')
#client.publish(f"{USER}/bed-A1/valve/set", 'close')

# DELETE ME
# client.subscribe(f"{USER}/bed-A1/") 
# DELETE ME!

i = 0 
print ("\n\n\n")
print ("******* tick number", i)
while i <= 60:
	time.sleep(2)
	print ("******* end of tick number", i)
	print ("\n")
	i += 1
	print ("*******tick number", i)


client.loop_stop()
# while True:
#     time.sleep(1)

# client.loop_stop()
