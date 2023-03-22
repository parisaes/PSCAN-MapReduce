import pandas as pd
import sys

def listToString(list, delimeter=","):
    strList = [str(i) for i in list]
    return delimeter.join(strList)

def ExtractAdjacencyLists(fileName):
    with open(fileName, 'r') as f:
        first_line = f.readline().strip() # read the first line of the file
    if ',' in first_line:
        delimiter = ','
    else:
        delimiter = '\s+'

    df = pd.read_csv(fileName, delimiter=delimiter , header=None)
    numberOfNodes = max(df[0].max(), df[1].max()) + 1 #maxID + 1

    adjacencyLists = [[] for i in range(numberOfNodes)] 
    for _, row in df.iterrows():
        node1 = int(row[0]) #TO-DO: specify data type when building the dataFrame
        node2 = int(row[1])
        adjacencyLists[node1].append(node2)
        adjacencyLists[node2].append(node1)

    adjacencyListsTxt = ""
    for ID, list in enumerate(adjacencyLists):
        if (len(list) > 0):
            adjacencyListsTxt += str(ID) + ","
            adjacencyListsTxt += listToString(list)
            if (ID < len(adjacencyLists) - 1):
                adjacencyListsTxt += "\n"
    return adjacencyListsTxt

def WriteToFile(string, fileName):
    f = open(fileName, "w")
    f.write(string)
    f.close()

if __name__ == "__main__":
    output = ExtractAdjacencyLists(sys.argv[1])
    datasetName = sys.argv[1].split(".")[0]
    fileName = datasetName + "_adjacency-lists.csv"
    WriteToFile(output, fileName)

