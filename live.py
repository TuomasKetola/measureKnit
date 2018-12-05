import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-s", "--sensors", nargs='+',  help="list of sensors as defined in arduino code")
parser.add_argument("-ename", "--ExperimentName", help="define function from: [collect, visualize]")

arguments = parser.parse_args()

global sensorNames
sensorNames = arguments.sensors
experimentName = arguments.ExperimentName

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = [[] for x in sensorNames]
ys = []



def animate(i, xs, ys):
	all_data = []
	for sensorName in sensorNames:	
		with open(os.path.join('collectedData',experimentName, sensorName+'.csv'), 'r') as in_:
			reader = csv.reader(in_)
			try:
				sensorData = [[int(x) for x in lst ]for lst in list(reader)]
				all_data.append((sensorData, sensorName))		
			except ValueError:
				return	
	ax.clear()
	try:
		for sensorData in all_data:
			ys = [x[1] for x in sensorData[0]]
			xs = [x[0] for x in sensorData[0]]	
			xs = xs[-200:]
			ys = ys[-200:]
			ax.plot(xs, ys, label=sensorData[1])
			ax.legend(loc="upper right")
	except IndexError:
		pass		

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=50)
plt.show()    