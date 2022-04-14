# from tkinter import font
# from cmath import log
# from turtle import width
from cProfile import label
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import matplotlib.font_manager as fm
from pylab import cm

#Get Data
logRe, logEq6, logEq15, logEq16 = np.loadtxt('logRe_logf.csv', unpack=True, delimiter=',',skiprows=1)
print(type(logRe))
#Make Figure and plot it
fig = plt.figure(figsize=(6,6))
left, bottom, width, height = [0.15,0.1,0.80,.85] 
ax = fig.add_axes( [left, bottom, width, height] )
ax.plot(logRe, logEq6, '.',label='$\mathcal{Re} < 2100$', color='r')
ax.plot(logRe, logEq15, '.',label='$\mathcal{Re} < 10^5$', color='b')
ax.plot(logRe, logEq16, '.', label='$\mathcal{Re} > 10^5$', color='b')

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
ax.set_title('Friction Factor models')

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
plt.legend(bbox_to_anchor=(0.3,0.2), loc=1, frameon=True, fontsize=10) #lower/upper left/right OR center OR right

# Save figure
plt.savefig('Final_Plot.png', dpi=900, transparent=False, bbox_inches='tight')

#Show the Plot 
plt.show()
print("PROGRAM COMPLETE") 