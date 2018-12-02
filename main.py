"""
python3 main.py -o collect -s sensor1 sensor2 -ename test3
"""


import Experiment
import Analysis
import argparse
parser = argparse.ArgumentParser()


arduinoPortName = '/dev/cu.usbmodem1421'
bayuRate = 115200


parser.add_argument("-o", "--option", help="define function from: [collect, visualize]")
parser.add_argument("-s", "--sensors", nargs='+',  help="list of sensors as defined in arduino code")
parser.add_argument("-ename", "--experimentName", help="name of experiment")
parser.add_argument("-alist", "--analysisList", nargs='+', help="names of experiments to analys")
parser.add_argument("-aname", "--analysisName", help="name of analysis")

arguments = parser.parse_args()
option = arguments.option

if option == 'collect':
	experimentName = arguments.experimentName
	sensors = arguments.sensors
	experiment = Experiment.Experiment(experimentName,sensors, arduinoPortName ,bayuRate)
	experiment.collectSampleData()
	experiment.saveData()

if option == 'analysis':
	experimentsToAnalyse = arguments.analysisList
	analysisName = arguments.analysisName

	
	analysis = Analysis.Analysis(experimentsToAnalyse)
	analysis.makePage({'type': 'lineChartSamples'}, show_=True)
	analysis.savePage(analysisName)
