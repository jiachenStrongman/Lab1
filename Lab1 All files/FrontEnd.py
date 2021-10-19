#FrontEnd.py File
#this will be the file that will run everything with it

import DataBase as DB
import Graph as GG
from tkinter import*
from tkinter.ttk import*

menu = Tk()
menu.title("Hey, lets look at some charts")
menu.geometry("440x350")

#label for user
prompt = Label(menu, text = "DATA VISUALIZATION PROGRAM", font = ("arial", 20))

prompt.grid()

style = Style()
style.configure('W.TButton', font = ('arial', 20, 'bold'), background = 'cyan')


def plotClick():
    XY = GG.XYPlot()
    XY.showPlot()

def thisClickWalksIntoABar():
    XY = GG.BAR()
    XY.showPlot()

def linRegPlot():
    XY = GG.linReg()
    XY.showPlot()
    
#buttons for each graph
plotBtn = Button(menu, text = "XY PLOT GRAPH", style = 'W.TButton', command = plotClick)
barBtn = Button(menu, text = "BAR CHART GRAPH", style = 'W.TButton', command = thisClickWalksIntoABar)
lineBtn = Button(menu, text = "LINEAR REGRESSION GRAPH", style = 'W.TButton', command = linRegPlot)
quitBtn = Button(menu, text = "QUIT", style = 'W.TButton', command = menu.destroy) #quit button

plotBtn.grid(column = 0, row = 1)
barBtn.grid(column = 0, row = 2)
lineBtn.grid(column = 0, row = 3)
quitBtn.grid(column = 0, row = 4)

menu.mainloop()

