# from tkinter import font
# from cmath import log
# from turtle import width
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from pylab import cm
import matplotlib.font_manager as fm

logRe, logEq6, logEq15, logEq16 = np.loadtxt('logRe_logf.csv', unpack=True, delimiter=',',skiprows=1)

fig = plt.figure()
# plt.title("Poop")
# plt.xlabel("Log(Re)")
# plt.ylabel("Log(f)")
# plt.xlim(-5)

x = fig.add_axes([left,bottom, width, height])
ax.plot(logRe, logEq15,'.', logEq6, '.', logEq16, '.', color='blue')
# ax.plot(logRe, logEq16, '.', color='green')
# ax.plot(logRe, logEq6,'.', color='red')

# font_names = [f.name for f in fm.fontManager.ttflist]
# print(font_names)
# mpl.rcParams['font.family'] = 'Avenir'
# plt.rcParams['font.size'] = 18
plt.show()

print("PROGRAM COMPLETE") 