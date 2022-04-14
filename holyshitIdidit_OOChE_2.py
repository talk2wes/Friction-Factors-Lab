# from tkinter import font
# from cmath import log
# from turtle import width
# from cProfile import label
# from statistics import LinearRegression
from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from cmath import log
from re import I
from struct import unpack
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import matplotlib.font_manager as fm
from pylab import cm
from sklearn.linear_model import LinearRegression

print("\n\n\n")

class ChEplot:
	
	def loadCSV(self, filename: str, names: list, indepVars):
		# if indepVars < 1 or indepVars > len(names): return
		self.data = np.loadtxt(filename, unpack=True, delimiter=',',skiprows=0)	
		# if indepVars > len(self.data): self.data = none; return
		self.dataLabels = names
		self.indepVars = indepVars
	
	@staticmethod
	def	rSquared(x, y):
		x = x.reshape((-1,1))
		y_reg = LinearRegression().fit(x,y)
		return y_reg.score(x,y)
	
	def printAllRSquared(self, precision=3):
		for fn in range(1, len(self.data)):
			for var in range(0, self.indepVars):
				rSquared = ChEplot.rSquared(self.data[0],self.data[fn])
				rstr = "R^2 = %1." + str(precision) + "f" 
				print( rstr % rSquared, "\t", self.dataLabels[fn], \
					"with respect to", self.dataLabels[0])
	
	def plotData(self, width, height):
		self.figure = plt.figure(figsize=(width, height))
		L, B, W, H = [0.15, 0.1, 0.80, 0.85]
		self.figure.axis = []
		self.figure.axis.append(self.figure.add_axes([L, B, W, H]))
		#find a way to exclude data
		for var in range(0, self.indepVars):
			for fn in range(self.indepVars, len(self.data)):
				print("fn = ", fn, "len = ",len(self.data) )
				x = self.data[var]
				y = self.data[fn]
				# mkr = self.dataMarkers[fn - self.indepVars]
				lbl = self.dataLabels[fn - self.indepVars]
				clr = self.dataColors[fn - self.indepVars]
				# print(clr)
				self.figure.axis[var].plot(x,y,'.',label=lbl,color=clr)

	def plotLRegLines(self, width=0.5, style='-'):
		for var in range(0, self.indepVars):
			for fn in range(self.indepVars, len(self.data)):
				m, b = np.polyfit(self.data[0],self.data[fn],1)
				y = (m * self.data[0]) + b
				self.figure.axis[var].plot(self.data[0], y, linewidth=width ,linestyle=style)

	#THIS IS ALL FOR THE PLOTTING OF RAW DATA
	def setDataStyles(self, styles: list):
		self.lineStyles = styles

	#idk what this param is
	def setDataMarkers(self, markers: list):
		# self.dataMarkers = markers
		pass

	def	setDataColors(self, colors: list):
		self.dataColors = colors 

	def setDataLabels(self, labels: list[str]):
		self.dataLabels = labels

	#Plot parameters	
	def setAxisLabels(self, x: str, y:str, indepVar=0, xpadding=5, ypadding=5):
		print(x, " \t\t", y)
		self.figure.axis[indepVar].set_xlabel(x,labelpad=xpadding)
		self.figure.axis[indepVar].set_ylabel(y,labelpad=ypadding)

	def showPlot(self):
		plt.show() 
	
	def setTics(self, _size=4, _width=1, _direction='in'):
		self.figure.axis[0].xaxis.set_tick_params(which='major', size=_size, width=_width, direction=_direction, top='on')
		self.figure.axis[0].xaxis.set_tick_params(which='minor', size=_size, width=_width, direction=_direction, top='on')

		self.figure.axis[0].yaxis.set_tick_params(which='major', size=_size, width=_width, direction=_direction, right='on')
		self.figure.axis[0].yaxis.set_tick_params(which='minor', size=_size, width=_width, direction=_direction, right='on')
	
	def showLegend(self, x=0.01, y=0.01, width=1, height=1, _loc='lower left', frame=True,_fontSize=10):
		plt.legend(bbox_to_anchor=(x,y, width, height), loc=_loc, frameon=frame, fontsize=_fontSize)
	
	def changeFont(self, font='Alvenir', size=10, linewidth=0.9):
		mpl.rcParams['font.family'] = font
		plt.rcParams['font.size'] = size 
		plt.rcParams['axes.linewidth'] = linewidth 

	
	def savePlot(self, filename="poop.png", _dpi=900, _transparent=False, _bbox_inches='tight'):
		# plt.savefig(filename, dpi=_dpi, transparent=_transparent, bbox_inches=_bbox_inches)
		plt.savefig('loglog_frictionFactor.png', dpi=900, transparent=False, bbox_inches='tight')


# print(type(logRe))

indepVars = 1
dataNames = ["Log_10(Reynold's Number)", "Log_10(Friction Factor)[Eqn 6]", \
	"Log_10(Friction Factor)[Eqn15]", "Log_10(Friction Factor)[Eqn16]"]
plot = ChEplot()
plot.loadCSV('logRe_logf.csv', dataNames, indepVars)
plot.printAllRSquared()
# plot.setDataMarkers(['.','.','.'])
plot.setDataLabels(["Fanning $\mathcal{f}$", "$\mathcal{Re}<2*10^3$",\
	 "$2100<\mathcal{Re} < 10^5$"] )
plot.setDataColors(['b','g','r'])

plot.plotData(6,6)
plot.plotLRegLines()
plot.setAxisLabels("$Log_{10}(\mathcal{Re})$", "$Log_{10}(\mathcal{f})$")
plot.setTics()
plot.showLegend()
plot.changeFont()
plot.showPlot()
	