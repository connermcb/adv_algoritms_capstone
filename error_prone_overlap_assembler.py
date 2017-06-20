#python3
# -*- coding: utf-8 -*-
"""
Overlap Assembler with Error-Prone Reads
"""
import phi_X174_formatter as fmtr
import itertools as it
import numpy as np
np.set_printoptions(threshold=np.inf)
import random
import read_maker2
from statistics import mode
import string
import sys


class OverlapEP(object):
    
    def __init__(self, read_length, num_reads, reads):
        self.read_length = read_length
        self.num_reads = num_reads
        self.reads = np.array(reads)
        self.walk = [(0,0)]
        self.searched = np.zeros(21, dtype=bool)
        self.graph = {}
        self.result = []
        self.nxt = 0

    def reads_compare(self, nxt):
        print(nxt, self.nxt)
        for i in range(1, self.read_length):
            test = self.reads[nxt, i:] == self.reads[:, :-i]
            counts = np.count_nonzero(test==0, axis=1)
            matches = np.nonzero(counts<3)
            if len(matches[0])>0:
                nxt = matches[0][0,]
                self.walk.append((nxt, i))
                self.searched[nxt] = True
                self.nxt = int(nxt)
                return
            
    def build_graph_ep(self):
        counter = 0
        while not np.all(self.searched):
            if counter > 16:
                print('reached end')
                return
            counter += 1
            self.reads_compare(self.nxt)

    def get_cumulative_indices(self):
        self.cumulative_indices = {read:0 for read in range(self.num_reads)}
        self.cum_idx = 0
        for read, idx in self.walk:
            self.cum_idx += idx
            self.cumulative_indices[read] = self.cum_idx
               
    def build_overlaps(self):
        self.result = np.zeros((len(self.walk), self.cum_idx + self.read_length))
        print(self.result)
        for each in self.walk:
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




#test_reads = [['A', 'C', 'G', 'A', 'C', 'A', 'T', 'G', 'T', 'T'],
#              ['C', 'T', 'T', 'G', 'T', 'T', 'T', 'G', 'C', 'C'],
#              ['T', 'G', 'T', 'T', 'C', 'C', 'C', 'C', 'C', 'C'],
#              ['T', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'G', 'T'],
#              ['C', 'C', 'C', 'C', 'G', 'C', 'C', 'G', 'A', 'C'],
#              ['C', 'A', 'G', 'A', 'C', 'G', 'T', 'C', 'C', 'C'],
#              ['C', 'G', 'T', 'C', 'C', 'T', 'G', 'A', 'G', 'G'],
#              ['C', 'C', 'G', 'A', 'G', 'T', 'T', 'C', 'T', 'C'],
#              ['G', 'T', 'C', 'G', 'C', 'G', 'T', 'A', 'G', 'C'],
#              ['C', 'T', 'C', 'G', 'T', 'A', 'C', 'C', 'G', 'T'],
#              ['G', 'C', 'A', 'T', 'G', 'A', 'G', 'A', 'C', 'G'],
#              ['G', 'T', 'C', 'A', 'G', 'A', 'C', 'G', 'A', 'G'],
#              ['T', 'G', 'A', 'G', 'A', 'T', 'G', 'A', 'G', 'C'],
#              ['A', 'C', 'G', 'A', 'G', 'C', 'A', 'C', 'G', 'A'],
#              ['A', 'G', 'C', 'A', 'C', 'G', 'A', 'C', 'T', 'T'],
#              ['A', 'C', 'G', 'A', 'C', 'T', 'T', 'G', 'T', 'T']]
test_reads = read_maker2.make_reads(errors=True)
O=OverlapEP(8, 21, test_reads)
print(O.reads)
print(O.reads.shape)
O.build_graph_ep()
print(O.walk)
O.get_cumulative_indices()
print(O.cumulative_indices)
    
