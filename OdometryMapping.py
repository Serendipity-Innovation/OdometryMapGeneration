#change path directory per computer
import matplotlib.pyplot as plt
import csv
import string

def getDataX(graphDataPath):
    x = []
    with open(graphDataPath, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
    return x


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
    versionStringFile = readFile("version.txt")
    for line in versionStringFile:
      if line.isspace():
        pass
      else:
        version = line #will repeat all the way to the end, the last line is the version number
    return version
    
def makeGraph(graphDataPath):
# get the data
    xList = getDataX(graphDataPath)
    yList = getDataY(graphDataPath)
    isDetectGermsList = getDataIsDetectGerms(graphDataPath)
    print("xList is " + str(xList))
    print("yList is " + str(yList))
# plot the data first
    noGermsDetected, = plt.plot(xList, yList, label = "No Germs Detected", color = "green")
# add dots to where germs are found
    detectGermsListX = []
    detectGermsListY = []
    for i in range(len(xList)):
        xCoordinate = xList[i]
        yCoordinate = yList[i]
        isDetectGerms = isDetectGermsList[i]
        if isDetectGerms == "true":
          detectGermsListX.append(xCoordinate)
          detectGermsListY.append(yCoordinate)
    germDetectedLabel, = plt.plot(detectGermsListX, detectGermsListY, marker="o", linewidth = 5, label = "Germs Detected", color="red")

# Add titles, legends, etc
    plt.title("Germ Detection Location in Robot Path")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend(handles = [germDetectedLabel, noGermsDetected])
    #plt.legend(handles = noGermsDetected)
    plt.show()

def main():
    version = getVersion()
    makeGraph("odometryGraphData" + version + ".txt")
    
main()
    

        
