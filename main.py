import sys
import subprocess

def toAdjacencyLists(file):
    command = ['python3', 'to-adjacency-list.py', file]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)

def runPCSS(inputFileName, outputFileName):
    command = ['python3', 'pcss.py', inputFileName]
    with open(outputFileName, 'w') as f:
        result = subprocess.run(command, text=True, stdout=f)
        if result.returncode != 0:
            print(result.stderr)

def runLPCC(inputFileName):
    command = ['python3', 'lpcc.py', inputFileName]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)

if __name__ == "__main__":
    inputFilePath = sys.argv[1].split(".")[0] # without format
    inputFileFormat = ".csv" # TO-DO: command line argument
    toAdjacencyLists(inputFilePath + inputFileFormat)

    runPCSS(inputFilePath + "_adjacency-lists.csv", inputFilePath + "_si.txt") # first MapReduce

    # while(True):
    #     runLPCC(inputFilePath + "_filtered_structure-info.csv") # second MapReduce
    #     break;

