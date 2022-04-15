#Wesley Johanson
import ChE

dataNames = ["Log_10(Reynold's Number)", "Log_10(Friction Factor)[Eqn 6]", \
	"Log_10(Friction Factor)[Eqn15]", "Log_10(Friction Factor)[Eqn16]"]
fnLabels= ["Fanning $\mathcal{f}$", "$\mathcal{Re}<2\cdot10^3$", \
	"$2100<\mathcal{Re} < 10^5$" ]


plot = ChE.ChEplot()
#Data
plot.loadCSV('logRe_logf.csv', dataNames, indepVars=1)
#Plotting
plot.setFnLabels(fnLabels)
plot.setDataColors(['#89CFF0','#800020','#301934'])
plot.plotData(width=6,height=6)
#Regression
plot.plotLRegLines(width=0.1)
plot.printAllRSquared()
#Plot Parameters 
plot.setAxisLabels("$Log_{10}(\mathcal{Re})$", "$Log_{10}(\mathcal{f})$", xpadding=5, ypadding=5)
plot.setTicProps()
plot.setNumTics(0.1, 0.25, 3,3)
plot.showLegend()
plot.changeFont()
#Presentation
# plot.close()
plot.showPlot()
# plot.savePlot(filename="log(Re)_vs_log(f).png",_dpi=600)
	