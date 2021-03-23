from communicator import Communicator


# these are quick & dirty unit tests for Communicator class (see communicator.py)
# not by the book, but good enough for now


input(f'Welcome to communicator unit tests. Press any key to continue...')
farm_controller = 'mock'
c = Communicator(farm_controller)

valve_message = 'message: sam/bed-B2/valve open'
update_water_level_message = 'messsage: sam/bed-B2/water_level 3'
empty_message = 'message: sam/bed-A2/target Empty'
fill_message = 'message: sam/bed-B2/target Fill'
tank_water_level_message = 'messsage: sam/tank/water_level 783'

# test for is_valve_msg
print('\nis_valve_msg tests...')
# test result should be true
print(f'is_valve_message for {valve_message} is: {c.is_valve_msg(valve_message)}')
# test result should be false
print(f'is_valve_message for {empty_message} is: {c.is_valve_msg(empty_message)}')


# test for is_empty_bed_msg (should be true)
print('\nis_empty_msg tests...')
print(f'is_empty_messsage for {empty_message} is: {c.is_empty_bed_msg(empty_message)}')


# test for is_fill_bed_msg (should be true)
print('\nis_fill_msg tests...')
print(f'is_fill_messsage for {fill_message} is: {c.is_fill_bed_msg(fill_message)}')


# test for get_message_value
print('\nget_message_value tests...')
print(f'get_message_value for {empty_message} is: {c.get_message_value(empty_message)}')

# test for get_bed_label
print('\nget_bed_label tests...')
print(f'get_bed_label for {empty_message} is: {c.get_bed_label(empty_message)}')
print(f'get_bed_label for {tank_water_level_message} is: {c.get_bed_label(tank_water_level_message)}')
