"""
Classes used for listerning to OSC streams
"""
from serial import Serial

class Listener():
	"""Is an object that listens to given port"""
	def __init__(self, portLst, arduinoPort, bayuRate):
		
		self.portLst = portLst
		self.arduinoPort = arduinoPort
		self.bayuRate = bayuRate


	def listenToPorts(self):
		pass


	def listenToPorts(self):
		dataDict = dict()
		arduino = Serial(self.arduinoPort, self.bayuRate, timeout=.1)
		save = False
		while True:
			dataFromArduino = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
			if ': ' in dataFromArduino.decode():
				
				sourceName, reading =   tuple(dataFromArduino.decode().split(': '))
				if sourceName == 'button':
					if not save:
						save = True
					elif save:
						return dataDict

				elif save:
					try:
						dataDict[sourceName].append(reading)
					except KeyError:
						dataDict[sourceName] = [reading]

					

	# def parseIncoming(self):
		
# raise SerialException('read failed: {}'.format(e))
# serial.serialutil.SerialException: read failed: [Errno 6] Device not configured
