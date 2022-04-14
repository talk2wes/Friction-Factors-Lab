
import ChE
import numpy as np

plt = ChE.ChEplot()
plt.loadCSV("che118_hw.csv", skip=11)

#FIXING THE DATA_____________________________________
print("what the original data looked like")
plt.printData()
#Gotta fix the data, it's scrambled from the copy/paste
#	->Each Row vector of the orig. matrix is listed in order, in the first col
#	of the CSV file
x = []
y = []
x_err = []
y_err = []
orig = plt.data

i = 0
while(i < len(plt.data)):
	x.append(orig[i]); i += 1	
	y.append(orig[i]); i += 1
	x_err.append(orig[i]); i += 1
	y_err.append(orig[i]); i += 1
print("what the corrected data looks like")
plt.printData()
#FIXING THE DATA_____________________________________



labels = ["Pressure [Bar]", "Signal [Volts]", "Pressure_xError [bar]",\
		"Signal_yError [Volts]" ]
# plotFxns = []
newData = np.array([x, y, x_err, y_err])
plt.setData(newData, vars = 1)
plt.setDataLabel(labels)
m , b = np.polyfit(x,y,1)
plt.printMeans()

# x_mean = np.mean()




	



print("Program Complete")