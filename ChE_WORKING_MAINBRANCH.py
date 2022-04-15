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
		#Counting Elements
		self.numDataVars=None
		self.numDataFns=None
		self.numDataSets=None
		self.data=None
		self.fxns2plot=None

	#Data setter/getter/modifier functions
	# def loadCSV(self, filename: str,folder=None, names=None, indepVars=1, skip=0):
	# 	"""Loads each column of data from the CSV file into a row of a numpy
	# 	array stored in self.data
		
	# 	'names' is a list of names for the data sets in each col of the CSV"""
	# 	self.data = np.loadtxt(filename, unpack=True, \
	# 											delimiter=',',skiprows=skip)	
	# 	if names is not None: self.dataLabels = names
	# 	self.numDataVars = indepVars
	# 	self.numDataSets = len(self.data) 
	# 	self.numDataFns = self.numDataSets - self.numDataVars


			#Data 
	def loadCSV(self, filename: str, names: list, indepVars):
		"""Loads each column of data from the CSV file into a row of a numpy
	 	array stored in self.data
		
	 	'names' is a list of names for the data sets in each col of the CSV"""
		# if indepVars < 1 or indepVars > len(names): return
		self.data = np.loadtxt(filename, unpack=True, delimiter=',',skiprows=0)	
		# if indepVars > self.numDataSets: self.data = none; return
		self.dataLabels = names
		self.numDataVars = indepVars
		self.numDataSets = len(self.data) 
		self.numDataFns = self.numDataSets - self.numDataVars
		
	def segmentData(self):
		pass

	#Printers
	def	printAllData(self):
		print( 
			"\n",self.figure
			,"\n",self.dataLabels
			,"\n",self.fnLabels
			,"\n",self.numDataVars
			,"\n",self.numDataFns
			,"\n",self.numDataSets
			,"\n",self.data
			,"\n",self.fxns2plot)


		pass

	def	printData(self):
		"print all data points in self.data"
		print(self.data)

	def printMeans(self):
		"Prints the  mean value of each row vector in self.data"
		for i in range(0, self.numDataSets):
			outputStr = "the mean of "
			if self.dataLabels[i] is not None:
				outputStr += self.dataLabels[i]
			outputStr += "\t\tis " + str(np.mean(self.data[i])) 
			
	#Setters	
	def setDataLabel(self, names):
		"""
		Stores a list of strings into the instance, where each str in the list 
		is the name of the corresponding column in the CSV file
		"""
		self.dataLabels = names
	
	def setData(self, data: list, vars=1, ):
		"Replaces Data and performs same operations as loadCSV"
		self.data = data
		self.numDataVars = vars
		self.numDataSets = len(self.data)
		self.numDataFns = self.numDataSets - self.numDataVars

	def setIndepVars(self, vars):
		"Vars are the first arrays in the self.data matrix"
		self.setIndepVars = vars

	#Plotting
	def plotData(self, width, height, fxns2graph=None):
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
	
	def plotLRegLines(self, width=0.5, style='-', color='b'):
		for var in range(0, self.numDataVars):
			for fn in range(self.numDataVars, self.numDataSets):
				m, b = np.polyfit(self.data[0],self.data[fn],1)
				y = (m * self.data[0]) + b
				self.figure.axis[var].plot(self.data[0], y, \
					color=self.LRegLineColors[fn-self.numDataVars], \
						linewidth=width ,linestyle=style)
	
	def plotErrorBars(self):
		pass
	
	#Linear Regression & Statistics
	@staticmethod
	def	rSquared(x, y):
		x = x.reshape((-1,1))
		y_reg = LinearRegression().fit(x,y)
		return y_reg.score(x,y)
		
	def setLRegLineColors(self, colors=[]):
		self.LRegLineColors = colors

	def printAllRSquared(self, precision=5):
		for fn in range(self.numDataVars, self.numDataSets):
			for var in range(0, self.numDataVars):
				rSquared = ChEplot.rSquared(self.data[0],self.data[fn])
				rStr = "R^2 = %1." + str(precision) + "f" 
				rStr = rStr % rSquared
				if rStr is None: print("Error_0")	
				if self.dataLabels is None: print("Error_1")	
				print( f"{rStr:<15}{self.dataLabels[fn-self.numDataVars]:<30}{'with respect to':<20}{self.dataLabels[var]:<10}")
	
	# def confInterv(self)
	
	#Plot: Setters
	def setFxns2Plot(self, fxns):
		self.fxns2plot = fxns

	def setDataStyles(self, styles: list):	
		self.lineStyles = styles
	def	setDataColors(self, colors: list): 	
		self.dataColors = colors 
		self.setLRegLineColors(colors)
	def setFnLabels(self, labels: list[str]):	
		self.fnLabels = labels

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

	#Plot Features	
	def showLegend(self, x=0.01, y=0.01, width=1, height=1, _loc='lower left', frame=True,_fontSize=10):
		plt.legend(bbox_to_anchor=(x,y, width, height), loc=_loc, frameon=frame, fontsize=_fontSize)
	
	def changeFont(self, font='Alvenir', size=10, linewidth=0.9):
		mpl.rcParams['font.family'] = font
		plt.rcParams['font.size'] = size 
		plt.rcParams['axes.linewidth'] = linewidth 

	#Presentation and saving the generated images	
	def showPlot(self): 
		"Shows the figure"
		plt.show() 

	def savePlot(self, filename="poop.png", _dpi=900, _transparent=False, _bbox_inches='tight'):
		"Saves the Figure(graph) made to a file"
		plt.savefig(filename, dpi=_dpi, transparent=_transparent, bbox_inches=_bbox_inches)
	
	def close(self): 
		"Close the figure(window) that we were plotting in"
		plt.close(self.figure)

	