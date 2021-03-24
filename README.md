## This is a technical task that I made as part of a test

# Control the filling and draining of beds in vertical farm
This project simulates controlling the filling and draining in a [vertical farm](https://en.wikipedia.org/wiki/Vertical_farming).
The filling and draining executed through opening and closing valves of beds.
The communication is carried out using MQTT protocol(an implemantation of a publish/subscriber model).


# Motivation
This project done as a technical task to review my skills. 
When writing the code I followed the **SOLID** software design principles:
1. Single Responsibility Principle
2. Entities Open for extension, Close to modification
3. Liskov substitution principle (I didn't had to use inhertiance during this test)
4. Interface segregation principle
5. Dependency inversion principle

# Structure
This is a brief of the code structure.
Here are the different parts of the projects: 
* FarmController
* Communicator
* Farm model
* Bed model

## FarmController: 
FarmController controls and monitor the farm according to the instructions and the info he recieves the simulator (via the MQTT broker).

## Communicator
Communicatoer can provide information about messages that recieved from the broker. FarmController instance use the communicator to get info about the messages the FarmController recieves from the broker.
The motivation for the communicator is to decouple the communication logic out of the controller. And so, in case of changes in the communication protocols the
the FarmController code kept without changes. Changes will be limited to the communicator

## Farm model
Farm model is a model of a vertical form. It provides the controller info about the farm.
The farm model holds 2D list of the beds.
The farm also holds a DiGraph(python implemantation of directional graph).
The purpose of holding a directional graph is to help in finding water flow paths in the farm. 

## Node Model
Node model is modeling a bed in a vertical farm. The model provides the controller information about the bed status such as: water_level, valve_state etc.

# Folders and files structure
The folders structure of the project should be as follow:
*Note: Currently I still have issues with creating the packages properly. 
Until I will solve the issues all the files are under model folder*
```
app
    ├── controller
    |   └── __init__.py
    │   └── farm__controller.py
    │   
    ├── models
    |    └── __init__.py
    |    └── farm.py
    |    └── node.py
    |    └── communicator.py
    |
    ├── services
    |    └── __init__.py
    |    └── mqtt_client.py
    |    └── utils.py
    |    └── logger.py
    |    └── debugger.py
    |
    ├── tests
    |    └── __init__.py
    |    └── unit_tests_communicator.py
    |    └── unit_tests_farm_controller.py
    |
    ├── sam-client.py

```
# Tests
Currently there are tests for farm_controller and the communicator.
The tests are quick & dirty unit_tests 

# Issues

1. Issue with the packages.
2. The MQTT client - I have to improve my understanding
3. Unit tests. Currently there are minimal tests for necessary parts of the code, and they are not 'by the book'
4. Styling: I need to review the code and adjust it according PEP-8 code styling and convention
5. Node Model: The model is functional. There are some parts of the code that are not well-written and need to be removed 
6. Farm: remove edges from nodes on the same level
