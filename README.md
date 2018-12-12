# measureKnit
Python / Arduino library for measuring and analysing analog sensor input from e-textiles

## Requirements

````pip install requirements.txt````

### Arduino code
What is needed is an arduino set up where the sensors are connected to analog inputs and two buttons that are connected to digital inputs. The readings of sensors should be sent to the serial monitor as: `sensor_name: value` where sensor name is whatever you wish to call a given sensor and value is the reading coming in from the analog port.

Ports and bid rates are setup in the main.py function

## Basics

The repo has two main components: `Experiments` and `Analysis`

### Expriments
To run an experiment run: `python -o collect -s sensors -ename ExperimentName - Experiment1`

where: `collect` defines that an expriment is to be run, `sensors` is a list of sensor names from the arduino code and `ExperimentName` is the name of the experiment.

Each experiment is comprised of `x` samples that are defined by pressing one of the buttons on the arduino. The second button stops the experiment. The button presses sent to the serial monitor should be defined as `button: 1` and `button: 2`

### Analysis
To run an analysis run: `python -o analysis -aList Experiment1 Experiment2 -aName analysisName`

where: `analysis` defines that an analysis is to be run, `Experiment1 Experiment2` is a list of experiment names to be analysed and `aName` the name of the analysis