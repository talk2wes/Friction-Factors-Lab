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
	def __init__(self, width, height):
		print("instance made")
		self.figure = plt.figure(figsize=(width, height))
		left, bottom, width, height = [0.15,0.1,0.80,.85] 
		self.axis = self.figure.add_axes( [left, bottom, width, height] )   

	def linRegLine(self, x, y):
		m, b = np.polyfit(x, y)
		y_linReg = m * x + b
		return (x, y_linReg)

	def addData2Plot(self, x, y, y_lineStyle, y_label, y_color):
		self.axis.plot(x, y, y_lineStyle, y_label, y_color)

	def showPlot(self):
		plt.show()


def rSquared_linReg(domain, range):
	#Change row-vector to col-vector so the next function doesn't bitch at me
	domain = domain.reshape((-1,1))
	y_linReg = LinearRegression().fit(domain, range)
	rSquared = y_linReg.score(domain, range)
	return rSquared


myplot = plotter(6,6)

bend0_color = 'r'		
bend0_linestyle = '.'
bend0_label = '$test label 2$'

myplot.addData2Plot(bend0_logRe, bend0, bend0_linestyle, bend0_label, bend0_color)
myplot.showPlot()
myplot.fn1()



print("PROGRAM COMPLETE") 

