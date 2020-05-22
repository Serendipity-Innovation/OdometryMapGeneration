#change path directory per computer
def getDataX(graphDataPath):
    x = []
    with open(graphDataPath, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
    return x
import matplotlib.pyplot as plt
import csv

def getDataY(graphDataPath):
    y = []
    with open(graphDataPath, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            y.append(int(row[1]))
    return y
        
def getDataIsDetectGerms(graphDataPath):
    isDetectGerms = []
    with open(graphDataPath, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            isDetectGerms.append(row[2])
    return isDetectGerms
    
def readFile(path):
    #this function reads a txt file
    with open(path, "rt") as file:
        return file.read()

def getVersion():
    versionStringFile = readFile("/Users/JustKyle-ngaround/StudioProjects/OdometryMapGeneration/version.txt")
    for line in versionStringFile:
        version = line #will repeat all the way to the end, the last line is the version number
    return version
    
def makeGraph(graphDataPath):
# get the data
    xList = getDataX(graphDataPath)
    yList = getDataY(graphDataPath)
    isDetectGermsList = getDataIsDetectGerms(graphDataPath)
# plot the data
    for i in range(len(xList)):
        xCoordinate = xList[i]
        yCoordinate = yList[i]
        isDetectGermsList = isDetectGermsList[i]
        if isDetectGermsList = "true":
            plt.plot(xCoordinate,yCoordinate,marker="o")
        else:
            plt.plot(xCoordiante,yCoordinate,maker="-")
        
    plt.title("Germ Detection Location in Robot Path")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.show()

def main():
    version = getVersion()
    makeGraph("/Users/JustKyle-ngaround/Desktop/odometryGraphData/odometryMapData"
                + version + ".txt")
    
    
    
    

        
