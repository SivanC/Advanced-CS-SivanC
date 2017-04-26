import matplotlib.pyplot as plt
from sortfunctions import randListGen

aList = randListGen(10,10)
bList = randListGen(10,10)

def scatterGraph(xList, y):
    plt.scatter(xList,y)
    plt.show(block=True)
    
def plotGraph(xList,y):
    plt.plot(xList,y)
    plt.show(block=True)
    
def barGraph(xList, yList):
    plt.bar(xList,yList)
    plt.show(block=True)

barGraph(aList, bList)