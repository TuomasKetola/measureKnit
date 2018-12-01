import csv
import pandas as pd
import os
import OSCListen


def csvWrite(path, lst):
	with open(path, 'wb') as in_:
		writer = csv.writer()
		writer.writerows(['time', 'value']+lst)




experimentName = 'testtest'
dataDir = 'collectedData'
portsToListen = ['port1']
for folder in ['raw', 'figures', 'visualisations']:
	os.makedirs(os.path.join(dataDir, experimentName, folder), exist_ok=True)
listener1 = OSCListen.Listener(portsToListen, '/dev/cu.usbmodem1421',115200)

data = listener1.listenToPorts()

# data = {'port1': ['1', '2', '2', '2', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '9', '26', '34', '27', '11', '4', '3', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2'], 'port2': ['1', '2', '2', '2', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '9', '26', '34', '27', '11', '4', '3', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']}
experimentData =  pd.DataFrame.from_dict(data)
experimentData.to_csv(os.path.join(dataDir,experimentName, 'raw', 'rawData.csv'), index_label='t')