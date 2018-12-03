import os
import csv
import pandas as pd
from bokeh.palettes import Spectral11
from bokeh.io import output_file, show, save
from bokeh.layouts import column, gridplot
from bokeh.plotting import figure, output_file
from bokeh.models import ColumnDataSource, Legend, LegendItem


class Analysis(object):
	def __init__(self, experimentNames):
		self.experimentNames = experimentNames
		self.data = self.loadData(self.experimentNames)
		self.figures = []

	def makePage(self, opts, show_=True, rolling=False):	
		
		if opts['type'] == 'lineChartSamples':
			self.lineChartSamples(rolling)
			toDraw = []
			for experimentFigures in self.figures:
				figureChunks = self.chunkToPage(experimentFigures)
				toDraw.extend(figureChunks)
				gridPlot =True
			if gridPlot:
				self.page = gridplot(toDraw)
			if show_:
				show(self.page)
			

	def lineChartSamples(self, rolling):
		for experimentName, experimentData in self.data.items():
			experimentFigures = []
			for sampleName, sampleData in sorted(experimentData.items()):
				numlines=len(sampleData.columns)
				mypalette = Spectral11[0:numlines] 
				if rolling:
					sampleData = sampleData.rolling(2, min_periods=1).sum()
				columns = sampleData.columns.values
				p = figure(title='{ename} - {sname}'.format(ename=experimentName, sname=sampleName),plot_width=400, plot_height=250)
				
				legends_list = sampleData.columns.values
				xs = [sampleData.index.values]*numlines
				ys = [sampleData[name].values for name in sampleData]
				for (colr, leg, x, y ) in zip(mypalette, legends_list, xs, ys):
				    p.line(x, y, color= colr, legend= leg,line_width=2)	

				experimentFigures.append(p)
			self.figures.append(experimentFigures)

	def chunkToPage(self, experimentFigures):
		perRow = 3
		figureChunks = [experimentFigures[i:i + perRow] for i in range(0, len(experimentFigures), perRow)]
		for chunk in figureChunks:
			for i in range(1,3):
				try:
					chunk[i]
				except IndexError:
					chunk.append(None)	
		return figureChunks
	
	# def rollingAverage(self):
		

	def savePage(self, aname):
		output_file('analysis',aname+'.html')
		save(self.page, filename=os.path.join('analysis',aname+'.html'))

	def loadData(self, experimentNames):
		dataOut = {}
		for experiment in experimentNames:
			experimentData = {}
			for file in os.listdir(os.path.join('collectedData', experiment, 'raw') ):
				experimentData[file.replace('.csv', '')] = pd.read_csv(os.path.join('collectedData', experiment, 'raw', file), index_col='t')
			dataOut[experiment] = experimentData			
		return dataOut	
