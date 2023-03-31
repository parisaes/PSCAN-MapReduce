from mrjob.job import MRJob
from mrjob.step import MRStep

class LPCC(MRJob):
    
    def steps(self):
        return[
            MRStep(mapper = self.LPCCMapper,
            reducer = self.LPCCReducer)
        ]

    #Mapper function
    def LPCCMapper(self, _, file):
        reader = file.split("\n")
        for row in reader:
            row = row.split("\t")
            nodeID = int(row[0])
            structureInformation = [int(item) for item in row[1][1:-1].split(',')]
            status = structureInformation[0]
            label = structureInformation[1]
            adjacencyList = structureInformation[2:]
            if status == 1:
                for neighbour in adjacencyList:
                    yield neighbour, label
            yield nodeID, structureInformation

    #Reducer function
    def LPCCReducer(self, key, values):
        nodeID = key
        structureInformation = []
        smallestLabel = float('inf')
        for value in values:
            if isinstance(value, int): # value is a label from the neighbours
                if value < smallestLabel:
                    smallestLabel = value
            else: # value is the structureInformation
                structureInformation = value
        if smallestLabel < structureInformation[1]:
            structureInformation[0] = 1 # setting the status as activated
            structureInformation[1] = smallestLabel
        else:
            structureInformation[0] = 0 # setting the status as inactivated
        yield nodeID, structureInformation 

if __name__ == "__main__":
    LPCC.run()