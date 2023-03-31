from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy as np
import csv

threshold = 0.5

class PCSS(MRJob):
    
    def steps(self):
        return[
            MRStep(mapper = self.PCSSMapper,
            reducer = self.PCSSReducer),
            MRStep(mapper = self.SIMapper,
            reducer = self.SIReducer)
        ]
    
    # PCSS
    def PCSSMapper(self, _, file):
        reader = csv.reader([file])
        for row in reader:
            nodeID = int(row[0])
            neighbours = [int(r) for r in row[1:]]
            for u in neighbours:
                yield (min(nodeID, u), max(u, nodeID)), neighbours
            
    def PCSSReducer(self, key, values):
        edgeLists = list(values)
        structural_similarity = StructuralSimilarity(edgeLists[0], edgeLists[1])
        if structural_similarity >= threshold:
            yield key[0], key[1] # output the edge

    # Building Structural Info 
    def SIMapper(self, key, value):
        yield key, value
        yield value, key
            
    def SIReducer(self, key, values):
        edgeList = list(values)
        structureInfo = [1, key] + edgeList
        yield key, structureInfo  


def Intersect(list1, list2):
    return [value for value in list1 if value in list2]

def StructuralSimilarity(edgeList1, edgeList2): # assuming no self loops
    numerator = len(Intersect(edgeList1, edgeList2)) + 1 # u and v are connected: adding u and v to u.neighbours and v.neighbours
    len1 = len(edgeList1) + 1 # adding u to u.neighbours
    len2 = len(edgeList2) + 1 # adding v to v.neighbours
    denominator = np.sqrt(len1 * len2)
    return numerator / denominator

if __name__ == "__main__":
    PCSS.run()