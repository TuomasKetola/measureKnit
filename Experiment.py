from serial import Serial
import os
import pandas as pd
import csv

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


	def collectSampleData(self, live=True):
		dataDict = dict()
		allDataDict = dict()
		arduino = Serial(self.arduinoPort, self.bayuRate, timeout=.1)
		save = False
		t = 0
		tLast = 0
		while True:
			t += 1
			dataFromArduino = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
			if ': ' in dataFromArduino.decode():
				
				sensorName, reading = tuple(dataFromArduino.decode().split(': '))
				if sensorName == 'button' and reading == '2':
					print ('Experiment over')
					self.saveData()
					break	

				elif sensorName == 'button' and reading == '1':
					if not save:
						dataDict = {}
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
				try:
					allDataDict[sensorName].append([t,reading])
				except KeyError:
					allDataDict[sensorName] = [[t,reading]]		
					t += 1
				if t - tLast > 30:
					self.dumpLiveData(self.experimentName, self.sensors, allDataDict)

					tLast = t
	
	def dumpLiveData(self, experimentName ,sensors, allDataDict):
		with open(os.path.join('collectedData',self.experimentName, self.sensors[0]+'.csv'), 'w') as first, open(os.path.join('collectedData',self.experimentName, self.sensors[1]+'.csv'), 'w') as second,open(os.path.join('collectedData',self.experimentName, self.sensors[2]+'.csv'), 'w') as third:
			writer1 = csv.writer(first)
			writer2 = csv.writer(second)
			writer3 = csv.writer(third)
			writer1.writerows([x for x in allDataDict[self.sensors[0]][-400:]])
			writer2.writerows([x for x in allDataDict[self.sensors[1]][-400:]])
			writer3.writerows([x for x in allDataDict[self.sensors[2]][-400:]])				

	def saveData(self):
		for i in range(len(self.experimentData)):
			sampleData =  pd.DataFrame.from_dict(self.experimentData[i])
			sampleData.to_csv(os.path.join('collectedData',self.experimentName, 'raw', 'sample_'+str(i+1)+'.csv'), index_label='t')


