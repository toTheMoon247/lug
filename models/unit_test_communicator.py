from communicator import Communicator

input(f'Welcome to communicator unit tests. Press any key to continue...')
farm_controller = 'mock'
c = Communicator(farm_controller)

valve_message = 'messsage: sam/bed-B2/valve open'
update_water_level_message = 'messsage: sam/bed-B2/water_level 3'
empty_message = 'messsage: sam/bed-A2/target Empty'
fill_message = 'messsage: sam/bed-B2/target Fill'


print(f'is_valve_messsage for {valve_message} is: {c.is_valve_msg(valve_message)}')
print(f'is_valve_messsage for {empty_message} is: {c.is_valve_msg(empty_message)}')