
import ChE
import numpy as np

print ("\n\n")

plt = ChE.ChEplot()
plt.loadCSV("che118_hw.csv", skip=11)
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

print("what the new data looks like")
newData = np.array([x, y, x_err, y_err])
plt.setData(newData, vars = 1)
plt.printData()
m , b = np.polyfit(x,y,1)

x_mean = np.mean()




	



print("Program Complete")