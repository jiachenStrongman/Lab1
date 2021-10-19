#graph.py file

import DataBase as DB
import matplotlib.pyplot as plt
import numpy as np


class XYPlot:

    def showPlot(self):
        plt.close() #just so the previous plot isnt still shown
        xpoints = []
        ypoints = []
        for i in DB.tempDB.search():
            xpoints.append(i[0])
            ypoints.append(i[1])
        plt.plot(xpoints, ypoints)
        plt.title("Average temperature anomaly, Gobal | XY Plot")
        plt.xlabel("YEAR")
        plt.ylabel("TEMPERATURE ANOMALY °C")
        plt.show()

class BAR:

    def showPlot(self):
        plt.close()
        xpoints = []
        ypoints = []
        for i in DB.tempDB.search():
            xpoints.append(i[0])
            ypoints.append(i[1])
        plt.bar(xpoints, ypoints)
        plt.title("Average temperature anomaly, Gobal | Bar Chart")
        plt.xlabel("YEAR")
        plt.ylabel("TEMPERATURE ANOMALY °C")
        plt.show()

class linReg:

    def showPlot(self):
        plt.close()
        xpoints = []
        ypoints = []
        for i in DB.tempDB.search():
            xpoints.append(i[0])
            ypoints.append(i[1])
        plt.scatter(xpoints, ypoints, color = 'b')

        #plots linear regression line
        coef = np.polyfit(xpoints, ypoints, 1)
        poly1d_fn = np.poly1d(coef)
        plt.plot(xpoints, ypoints, 'ro', xpoints, poly1d_fn(xpoints))
        plt.xlim(1850, 2018)

        #graph labels
        plt.title("Average temperature anomaly, Gobal | Linear Regression")
        plt.xlabel("YEAR")
        plt.ylabel("TEMPERATURE ANOMALY °C")
        plt.show()
