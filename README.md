# measureKnit
Python / Arduino library for measuring and analysing analog sensor input from e-textiles

## Install

````pip install requirements.txt````

## Basics

The repo has two main components: `Experiments` and `Analysis`

### Expriments
To run an experiment run: `python -o collect -s sensors -ename ExperimentName - Experiment1`

where: `collect` defines that an expriment is to be run, `sensors` is a list of sensor names from the arduino code and `ExperimentName` is the name of the experiment.

Each experiment is comprised of `x` samples

### Analysis
To run an analysis run: `python -o analysis -aList Experiment1 Experiment2 -aName analysisName`

where: `analysis` defines that an analysis is to be run, `Experiment1 Experiment2` is a list of experiment names to be analysed and `aName` the name of the analysis