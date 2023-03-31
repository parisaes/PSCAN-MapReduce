import sys
import os
import subprocess

def toAdjacencyLists(file):
    command = ['python3', 'to-adjacency-list.py', file]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)

def runPCSS(inputFileName, outputFileName, numCores):
    command = ['python3', 'pcss.py', inputFileName, f"--num-cores={numCores}"]
    with open(outputFileName, 'w') as f:
        result = subprocess.run(command, text=True, stdout=f)
        if result.returncode != 0:
            print(result.stderr)

def runLPCC(inputFileName, outputFileName, numCores):
    command = ['python3', 'lpcc.py', inputFileName, f"--num-cores={numCores}"]
    with open(outputFileName, 'w') as f:
        result = subprocess.run(command, text=True, stdout=f)
        if result.returncode != 0:
            print(result.stderr)

if __name__ == "__main__":
    inputFilePath = sys.argv[1].split(".")[0] # without format
    toAdjacencyLists(sys.argv[1])

    numCores = 0; # number of cores to be used, value of 0 lets the programm decide
    if (len(sys.argv) > 2):
        numCores = sys.argv[2]

    SIFileName = inputFilePath + "_si.txt"
    runPCSS(inputFilePath + "_adjacency-lists.csv", SIFileName, numCores) # first MapReduce

    tmpFileName = inputFilePath + "_tmp.txt"
    while(True):
        bRun = False;
        with open(SIFileName, 'r') as file:
            for row in file:
                row = row.split("\t")
                status = row[1][1:-1].split(',')[0]
                if (status == '1'):
                    bRun = True
                    break
        if (bRun):
            runLPCC(SIFileName, tmpFileName, numCores) # second MapReduce
            os.remove(SIFileName)
            os.rename(tmpFileName, SIFileName)
        else:
            break