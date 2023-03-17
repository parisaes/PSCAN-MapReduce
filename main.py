import sys
import subprocess

def transformDatasetToAdjacencyLists(file):
    command = ['python3', 'to-adjacency-list.py', file]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)

def runPCSS(fileName):
    command = ['python3', 'pcss.py', fileName]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)

def runLPCC(fileName):
    command = ['python3', 'lpcc.py', fileName]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)

if __name__ == "__main__":
    inputFilePath = sys.argv[1].split(".")[0] # without format
    inputFileFormat = ".csv" # TO-DO: command line argument
    transformDatasetToAdjacencyLists(inputFilePath + inputFileFormat)

    runPCSS(inputFilePath + "_adjacency-lists.csv") # first MapReduce

    while(False):
        runLPCC(inputFilePath + "_filtered.csv") # second MapReduce

