import pandas as pd
import matplotlib.pyplot as plt
import time

class Graph:
    
    startIndex = 0
    endIndex = 0
    start = -1
    end = -1
    name = ""
    logDict = {}
    df = pd.DataFrame()

    def __init__(self, inputDict, inputName="", inputStart=-1, inputEnd=-1):
        global name, logDict, start, end
        name = inputName
        logDict = inputDict
        start = inputStart
        end = inputEnd
        self.update()

    def changeGraphRange(self, newStarting, newEnding):
        global start, end
        
        start = newStarting
        end = newEnding
        self.update()
        

    def update(self):
        global start, end, startIndex, endIndex, name, logDict, df
        timeStamps = list(logDict.keys())
        values = list(logDict.values())

        if(len(timeStamps) < 1):
            print("NO REAL DATA VALUES")
            timeStamps = [0]
            values = [0]

        if(start > -1 and end > -1):
            if(self.end > self.start):
                print("INPUT ERROR: ending index is smaller than starting index: ")

            startIndex = timeStamps.index(start)
            endIndex = timeStamps.index(end) + 1

            df = pd.DataFrame(values[startIndex:endIndex], timeStamps[startIndex:endIndex], columns=['Time (seconds)'])
        else:
            df = pd.DataFrame(values, timeStamps, columns=['Time (seconds)'])
        df.plot(color = 'red', title = self.name + ' Over Time')

        plt.show(block=True)

    def addNewRow(self):
        pass

    def delete(self):
        global df, startIndex, endIndex
        df = pd.DataFrame()
        startIndex = 0
        endIndex = 0
        plt.close()

if __name__ == "__main__": #testing
     global df
     testDict = {1: 90, 2: 87, 3: 83, 4: 45, 5: 92, 6: 86, 7: 69, 8: 88, 9: 96, 10: 90, 11: 77}
     print(testDict)

     testGraph = Graph(testDict, "value1")
     testDict[12] = 200
     print(testDict)

     testGraph.update()
     print("updated once, about to delete")
     print("test grpah before delete", df)
     testGraph.changeGraphRange(5, 8)
     time.sleep(5)
     testGraph.delete()
     print("deleted", df)
   