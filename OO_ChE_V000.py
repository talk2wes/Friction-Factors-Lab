# from tkinter import font
# from cmath import log
# from turtle import width
# from cProfile import label
# from statistics import LinearRegression
from ctypes import sizeof
from re import I
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import matplotlib.font_manager as fm
from pylab import cm
from sklearn.linear_model import LinearRegression


#Get Data
logRe, logEq6, logEq15, logEq16 = np.loadtxt('logRe_logf.csv', unpack=True, delimiter=',',skiprows=0)
# print(type(logRe))
print("\n\n PROGRAM INITIATED")
print(logEq6)
print("size of logEq6 array", logEq6.size)
bend0 = logEq6[:6]
bend90 = logEq6[6:10]
bend180 = logEq6[10:15]
bend0_logRe = logRe[:6]
bend90_logRe = logRe[6:10]
bend180_logRe = logRe[10:15]
print("Size of bend 0 = ",bend0.size,"\tbend90 size = ",bend90.size)
print("Size of bend 180 = ", bend180.size)
print("BEND 0 = ", bend0, "\nBend 90 = ", bend90, "\nbend 180 = ", bend180)

class plotter:
	def __init__(self, size):
		print("instance made")
		self.fig = plt.figure(size)
		left, bottom, width, height = [0.15,0.1,0.80,.85] 
		ax = fig.add_axes( [left, bottom, width, height] )   

	def linRegLine(x, y):
		m, b = np.polyfit(x, y)
		y_linReg = m * x + b
		return y_linReg

def addData2Plot(axis, x, y, y_lineStyle, y_label, y_color):
	axis.plot(x, y, y_lineStyle, y_label, y_color)


def rSquared_linReg(domain, range):
	#Change row-vector to col-vector so the next function doesn't bitch at me
	domain = domain.reshape((-1,1))
	y_linReg = LinearRegression().fit(domain, range)
	rSquared = y_linReg.score(domain, range)
	return rSquared

print("0°\tR^2 = ", rSquared_linReg(bend0_logRe, bend0))
print("90°\tR^2 = ", rSquared_linReg(bend90_logRe, bend90))
print("180°\tR^2 = ", rSquared_linReg(bend180_logRe, bend180))

# ax.plot(logRe, logEq6, '.',label='Fanning $\mathcal{f}$', color=eq6_color)

#Make Figure and plot it
fig = plt.figure(figsize=(6,6))
left, bottom, width, height = [0.15,0.1,0.80,.85] 
ax = fig.add_axes( [left, bottom, width, height] )    
thicc = 0.5
eq6_color = 'r'
eq15_color = 'b'
eq16_color = 'g'

bend0_color = 'r'
bend0_linestyle = '.'
bend0_label = '$test label 2$'

bend90_color = 'b'
bend90_linestyle = '.'
bend90_label = '$90° bend$'
# ax.plot(bend0_logRe, bend0, '.',label='$0° Bend: Eqn6$', color=eq6_color)
addData2Plot(ax, bend0_logRe, bend0, bend0_linestyle, bend0_label, bend0_color)
addData2Plot(ax, bend90_logRe, bend90, bend90_linestyle, bend90_label, bend90_color)

# ax.plot(x, y_6, linestyle='-',color=eq6_color,linewidth=thicc)
# ax.plot(bend90_logRe, bend90, 'v',label='$90° Bend: Eqn6$', color=eq15_color)
# ax.plot(x, y_15, linestyle='-', color=eq15_color, linewidth=thicc)
# ax.plot(bend180_logRe, bend180, '+', label='$180° Bend: Eqn6$', color=eq16_color)
# ax.plot(x, y_16, linestyle='-', color=eq16_color, linewidth=thicc)
# # ax.plot(logRe, y_eq15, linestyle='-', label='Linear reg eq15')
# ax.plot(logRe, y_eq16, linestyle='-', label='Linear reg eq16')

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

#LEGEND!!!!!!!!!!!!!!!!!!!!!
# plt.legend(bbox_to_anchor=(0.3,0.2), loc=1, frameon=True, fontsize=10) #lower/upper left/right OR center OR right

# Save figure
plt.savefig('3plot_diagram_logflogRe.png', dpi=900, transparent=False, bbox_inches='tight')

#Show the Plot 
plt.show()
print("PROGRAM COMPLETE") 



#Make linear regression lines from data
# lin_Re = logRe.reshape((-1,1))
# eq6_LR= LinearRegression().fit(lin_Re, logEq6)
# eq6_r_sq = eq6_LR.score(lin_Re, logEq6)

# eq15_LR= LinearRegression().fit(lin_Re, logEq15)
# eq15_r_sq = eq15_LR.score(lin_Re, logEq15)

# eq16_LR= LinearRegression().fit(lin_Re, logEq16)
# eq16_r_sq = eq16_LR.score(lin_Re, logEq16)
# print('rsq6 = ', eq6_r_sq, '\trsq15=',eq15_r_sq, '\trsq16=',eq16_r_sq)

# x = np.linspace(logRe.min(), logRe.max(), logRe.size)

# m_6, b_6  = np.polyfit(logRe, logEq6, 1)
# y_6 = m_6 * x + b_6
# m_15, b_15  = np.polyfit(logRe, logEq15, 1)
# y_15 = m_15 * x + b_15  
# m_16, b_16  = np.polyfit(logRe, logEq16, 1)
# y_16 = m_16 * x + b_16 

# print("m_eq6\t",m_6,"m_eq15",m_15,"m_eq16",m_16)
# print("b_eq6\t",b_6 ,"b_eq15\t",b_15 ,"b_eq16\t",b_16)






#  Create new axes object by cloning the y-axis of the first plot
# ax2 = ax.twiny()
# # Edit the tick parameters of the new x-axis
# ax2.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax2.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')

