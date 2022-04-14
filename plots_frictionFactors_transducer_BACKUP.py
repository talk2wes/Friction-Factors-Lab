import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import matplotlib.font_manager as fm
from pylab import cm
from sklearn.linear_model import LinearRegression

#Get Data
I, P = np.loadtxt('transducer_mA_psi.csv', unpack=True, delimiter=',',skiprows=0) 
# print(type(logRe))

#Make linear regression lines from data
# lin_Re = logRe.reshape((-1,1))
# eq6_LR= LinearRegression().fit(lin_Re, logEq6)
# eq6_r_sq = eq6_LR.score(lin_Re, logEq6)

# eq15_LR= LinearRegression().fit(lin_Re, logEq15)
# eq15_r_sq = eq15_LR.score(lin_Re, logEq15)

# eq16_LR= LinearRegression().fit(lin_Re, logEq16)
# eq16_r_sq = eq16_LR.score(lin_Re, logEq16)
# print('rsq = ', eq6_r_sq, '\trsq15=',eq15_r_sq, '\trsq16=',eq16_r_sq)

# x = np.linspace(logRe.min(), logRe.max(), logRe.size)

# m_6, b_6  = np.polyfit(logRe, logEq6, 1)
# y_6 = m_6 * x + b_6
# m_15, b_15  = np.polyfit(logRe, logEq15, 1)
# y_15 = m_15 * x + b_15  
# m_16, b_16  = np.polyfit(logRe, logEq16, 1)
# y_16 = m_16 * x + b_16 

I_linSpace = np.linspace(I.min(), I.max(), I.size)
degreeOfPoly = 1
m, b = np.polyfit(I, P, degreeOfPoly) #np.poltfit(I, P, degreeOfPoly)
P_linReg = (m * I_linSpace) + b

I_colVec = I.reshape((-1,1))
P_LR = LinearRegression().fit(I_colVec, P)
P_linReg_rSquared = P_LR.score(I_colVec, P)
print("m = ", m, "\tb = ", b, "\tr^2 = ", P)
#Make Figure and plot it
fig = plt.figure(figsize=(6,6))
left, bottom, width, height = [0.15,0.1,0.80,.85] 
ax = fig.add_axes( [left, bottom, width, height] )
thicc = 0.5
P_color = 'r'
# eq15_color = 'b'
# eq16_color = 'g'
ax.plot(I, P, '.',label='$PressureDrop[psi]$', color=P_color)
ax.plot(I_linSpace, P_linReg, linestyle='-',color=P_color,linewidth=thicc)

# ax.plot(logRe, logEq15, '.',label='$\mathcal{Re} < 10^5$', color=eq15_color)
# ax.plot(x, y_15, linestyle='-', color=eq15_color, linewidth=thicc)
# ax.plot(logRe, logEq16, '.', label='$\mathcal{Re} > 10^5$', color=eq16_color)
# ax.plot(x, y_16, linestyle='-', color=eq16_color, linewidth=thicc)
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
numberOfTicsPerAxis = 5

minTics_x = 2 #small tics per big tic
x_tic = 2#abs(I.max() - I.min()) / numberOfTicsPerAxis
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(x_tic))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(x_tic/minTics_x))
minPerMajTic_y = 2
y_tic = 2.5 #abs(P.max() - P.min()) / numberOfTicsPerAxis
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(y_tic))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(y_tic/minPerMajTic_y))

# Set the axis limit
min_y = np.min(P)
max_y = np.max(P)
min_x = np.min(I)
max_x = np.max(I)
axis_buffer = 0.20 #making the domain & range a % wider than the dataset
x_buffer = (max_x - min_x) * axis_buffer 
y_buffer = (max_y - min_y) * axis_buffer
ax.set_xlim(min_x - x_buffer, max_x + x_buffer)
ax.set_ylim(min_y - y_buffer, max_y + y_buffer)

# Add the x and y-axis labels
ax.set_xlabel(r'$I[mA]$', labelpad=5)
ax.set_ylabel('Pressure Drop [psi]', labelpad=5)
# ax.set_title('Pressure / Current Relation')

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
# plt.legend(bbox_to_anchor=(0.3,0.2), frameon=True, fontsize=10) #lower/upper left/right OR center OR right

# Save figure
plt.savefig('transducer_psi_mA.png', dpi=900, transparent=False, bbox_inches='tight')

#Show the Plot 
plt.show()
print("PROGRAM COMPLETE") 