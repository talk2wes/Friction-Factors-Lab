#Wesley Johanson
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.font_manager as fm
from sklearn.linear_model import LinearRegression

class ChEplot:

	def __init__(self):
		self.figure=None
		self.dataLabels=None
		self.fnLabels=None
		self.numDataVars=None
		self.numDataFns=None
		self.numDataSets=None
		self.data=None
	#Data 
	def loadCSV(self, filename: str, names: list, indepVars):
		# if indepVars < 1 or indepVars > len(names): return
		self.data = np.loadtxt(filename, unpack=True, delimiter=',',skiprows=0)	
		# if indepVars > self.numDataSets: self.data = none; return
		self.dataLabels = names
		self.numDataVars = indepVars
		self.numDataSets = len(self.data) 
		self.numDataFns = self.numDataSets - self.numDataVars

	def plotData(self, width, height):
		self.figure = plt.figure(figsize=(width, height))
		L, B, W, H = [0.15, 0.1, 0.80, 0.85]
		self.figure.axis = []
		self.figure.axis.append(self.figure.add_axes([L, B, W, H]))
		#find a way to exclude data
		for var in range(0, self.numDataVars):
			for fn in range(self.numDataVars, self.numDataSets):
				x = self.data[var]
				y = self.data[fn]
				lbl = self.fnLabels[fn - self.numDataVars]
				clr = self.dataColors[fn - self.numDataVars]
				self.figure.axis[var].plot(x,y,'.',label=lbl,color=clr)
	
	def segmentData(self):
		pass

	#Linear Regression
	@staticmethod
	def	rSquared(x, y):
		x = x.reshape((-1,1))
		y_reg = LinearRegression().fit(x,y)
		return y_reg.score(x,y)

	def plotLRegLines(self, width=0.5, style='-', color='b'):
		for var in range(0, self.numDataVars):
			for fn in range(self.numDataVars, self.numDataSets):
				m, b = np.polyfit(self.data[0],self.data[fn],1)
				y = (m * self.data[0]) + b
				self.figure.axis[var].plot(self.data[0], y, \
					color=self.LRegLineColors[fn-self.numDataVars], \
						linewidth=width ,linestyle=style)
	
	def setLRegLineColors(self, colors=[]):
		self.LRegLineColors = colors

	def printAllRSquared(self, precision=5):
		for fn in range(self.numDataVars, self.numDataSets):
			for var in range(0, self.numDataVars):
				rSquared = ChEplot.rSquared(self.data[0],self.data[fn])
				rStr = "R^2 = %1." + str(precision) + "f" 
				rStr = rStr % rSquared
				print( f"{rStr:<15}{self.dataLabels[fn-self.numDataVars]:<30}{'with respect to':<20}{self.dataLabels[var]:<10}")
	
	#Plot parameters	
	def setDataStyles(self, styles: list):		self.lineStyles = styles
	def	setDataColors(self, colors: list): 	self.dataColors = colors; self.setLRegLineColors(colors);
	def setFnLabels(self, labels: list[str]):	self.fnLabels = labels

	def setAxisLabels(self, x: str, y:str, indepVar=0, xpadding=5, ypadding=5):
		self.figure.axis[indepVar].set_xlabel(x,labelpad=xpadding)
		self.figure.axis[indepVar].set_ylabel(y,labelpad=ypadding)

	def setTicProps(self, _size=4, _width=1, _direction='in'):
		self.figure.axis[0].xaxis.set_tick_params(which='major', size=_size, width=_width, direction=_direction, top='on')
		self.figure.axis[0].xaxis.set_tick_params(which='minor', size=_size, width=_width, direction=_direction, top='on')
		self.figure.axis[0].yaxis.set_tick_params(which='major', size=_size, width=_width, direction=_direction, right='on')
		self.figure.axis[0].yaxis.set_tick_params(which='minor', size=_size, width=_width, direction=_direction, right='on')
	
	def setNumTics(self, delta_x=0.1, delta_y=0.1, x_subTics=3, y_subTics=3):
		self.figure.axis[0].xaxis.set_major_locator(mpl.ticker.MultipleLocator(delta_x))
		self.figure.axis[0].xaxis.set_minor_locator(mpl.ticker.MultipleLocator(delta_x/x_subTics))
		self.figure.axis[0].yaxis.set_major_locator(mpl.ticker.MultipleLocator(delta_y))
		self.figure.axis[0].yaxis.set_minor_locator(mpl.ticker.MultipleLocator(delta_y/y_subTics))

	
	def showLegend(self, x=0.01, y=0.01, width=1, height=1, _loc='lower left', frame=True,_fontSize=10):
		plt.legend(bbox_to_anchor=(x,y, width, height), loc=_loc, frameon=frame, fontsize=_fontSize)
	
	def changeFont(self, font='Alvenir', size=10, linewidth=0.9):
		mpl.rcParams['font.family'] = font
		plt.rcParams['font.size'] = size 
		plt.rcParams['axes.linewidth'] = linewidth 

	#Presentation	
	def showPlot(self): plt.show() 

	def savePlot(self, filename="poop.png", _dpi=900, _transparent=False, _bbox_inches='tight'):
		plt.savefig(filename, dpi=_dpi, transparent=_transparent, bbox_inches=_bbox_inches)
	
	def close(self): plt.close(self.figure)

	