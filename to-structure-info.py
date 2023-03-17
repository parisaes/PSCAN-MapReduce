import pandas as pd
import sys


def listToString(list, delimeter=","):
    strList = [str(i) for i in list]
    return delimeter.join(strList)

def extractNodeAndStructure(fileName):
    df = pd.read_csv(fileName, delimiter=",", header=None)
    numberOfNodes = max(df[0].max(), df[1].max()) + 1 #maxID + 1

    adjacencyLists = [[] for i in range(numberOfNodes)] 
    for _, row in df.iterrows():
        node1 = int(row[0]) #TO-DO: specify data type when building the dataFrame
        node2 = int(row[1])
        adjacencyLists[node1].append(node2)
        adjacencyLists[node2].append(node1)

    nodeAndStructure= ""
    for ID, list in enumerate(adjacencyLists):
        if (len(list) > 0):
            #insert node
            nodeAndStructure += str(ID) + ","
            #insert activation satus
            nodeAndStructure += str(1) + ","
            #insert activation Label
            nodeAndStructure+= str(ID) + ","
            #insert adjacencyList
            nodeAndStructure += listToString(list)
            if (ID < len(adjacencyLists) - 1):
                nodeAndStructure += "\n"
    return nodeAndStructure

def WriteToFile(string, fileName):
    f = open(fileName, "w")
    f.write(string)
    f.close()

if __name__ == "__main__":
    output = extractNodeAndStructure(sys.argv[1])
    fileName =sys.argv[1].split(".")[0] + "_structure-info.csv"
    WriteToFile(output, fileName)

