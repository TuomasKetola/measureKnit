from serial import Serial
import os
import pandas as pd

class Experiment:
	
	def __init__(self, experimentName,  sensors, arduinoPort, bayuRate):
		self.experimentName = experimentName
		self.sensors = sensors
		self.arduinoPort = arduinoPort
		self.bayuRate = bayuRate
		self.sampleNr = 1
		self.experimentData = list()
		for folder in ['raw', 'figures', 'visualisations']:
			os.makedirs(os.path.join('collectedData', experimentName, folder), exist_ok=True)


	def collectSampleData(self):
		
		dataDict = dict()
		arduino = Serial(self.arduinoPort, self.bayuRate, timeout=.1)
		save = False
		while True:
			dataFromArduino = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
			if ': ' in dataFromArduino.decode():
				
				sensorName, reading =   tuple(dataFromArduino.decode().split(': '))
				if sensorName == 'button' and reading == '2':
					print ('Experiment over')
					break	

				elif sensorName == 'button' and reading == '1':
					if not save:
						print ('Collecting data')
						save = True
					elif save:
						print ('Finished collecting sample', self.sampleNr)
						self.sampleNr += 1
						self.experimentData.append(dataDict)
						save = False

				elif save and sensorName in self.sensors:

					try:
						dataDict[sensorName].append(reading)
					except KeyError:
						dataDict[sensorName] = [reading]
		
	
	def saveData(self):
		for i in range(len(self.experimentData)):
			sampleData =  pd.DataFrame.from_dict(self.experimentData[i])
			sampleData.to_csv(os.path.join('collectedData',self.experimentName, 'raw', 'sample_'+str(i+1)+'.csv'), index_label='t')


