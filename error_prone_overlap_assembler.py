#python3
# -*- coding: utf-8 -*-
"""
Overlap Assembler with Error-Prone Reads
"""
import phi_X174_formatter as fmtr
import itertools as it
import numpy as np
import random
import read_maker
from statistics import mode
import string
import sys


class OverlapEP(object):
    
    def __init__(self, read_length, reads):
        self.read_length = read_length
        self.reads = np.array(reads)
        self.pair_overlap_list = np.zeros((1618, 2))
        self.searched = np.zeros(1618, dtype=bool)
        self.graph = {}
        self.result = []
        self.nxt = 0

    def compare(self, nxt):
        for i in range(99, 10, -1):
            test = self.reads[nxt, 100-i:] == self.reads[:, :i]
            counts = np.count_nonzero(test==0, axis=1)
            matches = np.nonzero(counts < 3)
            if matches[0]:
                self.pair_overlap_list[nxt, :] = [matches[0], i]
                self.searched[nxt] = True
                self.nxt = matches[0]
                return
            
    def build_graph_ep(self):
        counter = 0
        while not np.all(self.searched):
            if counter > 1618:
                return
            counter += 1
            self.compare(nxt)

    def get_cumulative_indices(self):
        self.cumulative_indices = {read:0 for read in self.reads}
        stack = [self.reads[0]]
        while stack:
            nxt = stack.pop(0)
            new = self.graph[nxt]
            self.cumulative_indices[new[0]] = self.cumulative_indices[nxt] + new[1]
            stack.append(new[0])
            if self.reads[0] in stack:
                break
               
    def build_overlaps(self):
        self.result = [[ltr] for ltr in self.reads[0]]
        reads_by_index =  sorted(self.cumulative_indices.items(), key=lambda x:x[1])
        for each in reads_by_index:
            result_length = len(self.result)
            read, start = each
            overlap = result_length - start
            for i in range(overlap):
                self.result[start+i].append(read[i])
            for j in range(overlap,len(read)):
                self.result.append([read[j]])
            
    def flatten_overlaps(self):
        for pos in range(len(self.result)):
            try:
                self.result[pos] = mode(self.result[pos])
            except:
                self.result = ['A' for x in range(6000)]
                return
    
    def trim(self):
        pos = 1
        while True:
            if self.result[:pos] == self.result[-pos:]:
                self.result = self.result[:-pos]
                return
            pos += 1


test_reads = ["".join([random.choice('ACGT') for i in range(10)])\
              for j in range(1618)]

test_reads = [list(each) for each in test_reads]

O = OverlapEP(10, test_reads)
print(O.reads)
#print(test_reads)
#print(len(test_reads))
#print(len(test_reads[0]))
#
#reads = np.array(test_reads)#[:, np.newaxis]
#print(reads)
#print(reads.shape)
#print(reads[0])
#print(reads[1])
#print(reads[0,0])
#import time
#start = time.time()
#check = reads[0,:]==reads[1:,:]
#print(time.time()-start)
#print(check)
#print(reads[9,0])
#print(reads[0,0]==reads[1:,0])
#if __name__ == "__main__":
#    reads = []
#    for i in range(1618):
#        read = sys.stdin.readline().strip()
#        reads.append(list(read))
#    O = OverlapEP(100, reads)



    
