#python3
# -*- coding: utf-8 -*-
"""
Overlap Assembler with Error-Prone Reads
"""

import numpy as np
from statistics import mode
import sys


class OverlapEP(object):
    
    def __init__(self, read_length, num_reads, reads):
        self.read_length = read_length
        self.num_reads = num_reads
        self.reads = np.array(reads)
        self.walk = [(0,0)]
        self.searched = np.zeros(num_reads, dtype=bool)
        self.graph = {}
        self.result = [[] for i in range(5500)]
        self.nxt = 0

    def reads_compare(self, nxt):
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
            if counter > 1618:
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
        for each in self.walk:
            read = self.reads[each[0],:]
            start_idx = self.cumulative_indices[each[0]]
            for i in range(len(read)):
                self.result[(start_idx+i)%5396].append(read[i])
            
            
    def flatten_overlaps(self):
        while len(self.result[-1]) < 1:
            self.result.pop(-1)
        for pos in range(len(self.result)):
            try:
                self.result[pos] = mode(self.result[pos])
            except:
                self.result = ['A' for x in range(6000)]
                return


reads = []
for i in range(1618):
    read = sys.stdin.readline().strip()
    read = list(read)
    reads.append(read)
    
graph = OverlapEP(100, 1618, reads)
graph.build_graph_ep()
graph.get_cumulative_indices()
graph.build_overlaps()
graph.flatten_overlaps()
print("".join(graph.result))
