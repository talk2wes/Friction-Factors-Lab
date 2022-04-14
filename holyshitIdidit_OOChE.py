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





		
#Get Data
logRe, logEq6, logEq15, logEq16 = np.loadtxt('logRe_logf.csv', unpack=True, delimiter=',',skiprows=0)


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
plot.showPlot()
	
# print('NEW rs of 6 = ', plot.rSquared(logRe,logEq6))
# print('NEW rs of 15 = ', plot.rSquared(logRe,logEq15))
# print('NEW rs of 16 = ', plot.rSquared(logRe,logEq16))

#Make linear regression lines from data
lin_Re = logRe.reshape((-1,1))
eq6_LR= LinearRegression().fit(lin_Re, logEq6)
eq6_r_sq = eq6_LR.score(lin_Re, logEq6)

eq15_LR= LinearRegression().fit(lin_Re, logEq15)
eq15_r_sq = eq15_LR.score(lin_Re, logEq15)

eq16_LR= LinearRegression().fit(lin_Re, logEq16)
eq16_r_sq = eq16_LR.score(lin_Re, logEq16)
print('rsq6 = ', eq6_r_sq, '\trsq15=',eq15_r_sq, '\trsq16=',eq16_r_sq)



x = np.linspace(logRe.min(), logRe.max(), logRe.size)

m_6, b_6  = np.polyfit(logRe, logEq6, 1)
y_6 = m_6 * x + b_6
m_15, b_15  = np.polyfit(logRe, logEq15, 1)
y_15 = m_15 * x + b_15  
m_16, b_16  = np.polyfit(logRe, logEq16, 1)
y_16 = m_16 * x + b_16 

print("m_eq6\t",m_6,"m_eq15",m_15,"m_eq16",m_16)
print("b_eq6\t",b_6 ,"b_eq15\t",b_15 ,"b_eq16\t",b_16)

#Make Figure and plot it
fig = plt.figure(figsize=(6,6))
left, bottom, width, height = [0.15,0.1,0.80,.85] 
ax = fig.add_axes( [left, bottom, width, height] )    
thicc = 0.5
eq6_color = 'r'
eq15_color = 'b'
eq16_color = 'g'

def addData2Plot(axis, x, y, y_lineStyle, y_label, y_color):
	axis.plot(x, y, y_lineStyle, y_label, y_color)
	return axis
	

# ax = addData2Plot(ax, logRe, logEq6, '.','Fanning $\mathcal{f}$', 'r')

ax.plot(logRe, logEq6, '.',label='Fanning $\mathcal{f}$', color=eq6_color)
ax.plot(x, y_6, linestyle='-',color=eq6_color,linewidth=thicc)
ax.plot(logRe, logEq15, 'v',label='$\mathcal{Re}<2*10^3$', color=eq15_color)
ax.plot(x, y_15, linestyle='-', color=eq15_color, linewidth=thicc)
ax.plot(logRe, logEq16, '+', label='$2100<\mathcal{Re} < 10^5$', color=eq16_color)
ax.plot(x, y_16, linestyle='-', color=eq16_color, linewidth=thicc)
# ax.plot(logRe, y_eq15, linestyle='-', label='Linear reg eq15')
# ax.plot(logRe, y_eq16, linestyle='-', label='Linear reg eq16')

# Hide the top and right spines of the axis
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)

# Edit the major and minor ticks of the x and y axes
ax.xaxis.set_tick_params(which='major', size=4, width=1, direction='in', top='on')
ax.xaxis.set_tick_params(which='minor', size=4, width=1, direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=4, width=1, direction='in', right='on')
ax.yaxis.set_tick_params(which='minor', size=4, width=1, direction='in', right='on')

# Edit the major and minor tick locations
minTics_x = 2
x_tic = 0.1 
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(x_tic))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(x_tic/minTics_x))
minPerMajTic_y = 2
y_tic = 0.25 
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(y_tic))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(y_tic/minPerMajTic_y))

# Set the axis limit
min_y = np.min([logEq6, logEq15, logEq16])
max_y = np.max([logEq6, logEq15, logEq16])
min_x = np.min([logRe])
max_x = np.max([logRe])
axis_buffer = 0.20 
x_buffer = (max_x - min_x) * axis_buffer 
y_buffer = (max_y - min_y) * axis_buffer
ax.set_xlim(min_x - x_buffer, max_x + x_buffer)
ax.set_ylim(min_y - y_buffer, max_y + y_buffer)

# Add the x and y-axis labels
ax.set_xlabel(r'$Log_{10}(\mathcal{Re})$', labelpad=5)
ax.set_ylabel('$Log_{10}(\mathcal{f})$', labelpad=5)
# ax.set_title('Friction Factor models')

# Create new axes object by cloning the y-axis of the first plot
# ax2 = ax.twiny()
# # Edit the tick parameters of the new x-axis
# ax2.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax2.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')

# Collect all the font names available to matplotlib
font_names = [f.name for f in fm.fontManager.ttflist]
# print(font_names)
# Edit the font, font size, and axes width
mpl.rcParams['font.family'] = 'Avenir'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = .9

#Plotting Settings
# plt.title("Log(f) vs Log(Re)")
# plt.xlabel("Log(Re)")
# plt.ylabel("Log(f)")
plt.legend(bbox_to_anchor=(0.5,0.2), loc=1, frameon=True, fontsize=10) #lower/upper left/right OR center OR right

# Save figure
plt.savefig('loglog_frictionFactor.png', dpi=900, transparent=False, bbox_inches='tight')

#Show the Plot 
# plt.show()
print("PROGRAM COMPLETE") 