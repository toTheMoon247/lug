# Control the filling and draining of beds in vertical farm
This project simulates controlling the filling and draining in a [vertical farm](https://en.wikipedia.org/wiki/Vertical_farming).
The filling and draining executed through opening and closing valves of beds.
The communication is carried out using MQTT protocol(an implemantation of a publish/subscriber model).

# Motivation
This project done as a technical task to review my skills

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
The purpose of holding a directional graph is to help in finding paths in the farm regarding the water flow. 

## Node Model
Node model is modeling a bed in a vertical farm. The model provides the controller information about the bed status such as: water_level, valve_state etc.

# Folders and files structure
The folders structure of the project should be as follow:
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
    ├── services
    |    └── communicator.py
    |    └── client.py
    |    └── utils.py
    |
    ├── sam-client.py

```
