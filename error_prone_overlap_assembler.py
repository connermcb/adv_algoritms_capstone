#python3
# -*- coding: utf-8 -*-
"""
Overlap Assembler with Error-Prone Reads
"""
import phi_X174_formatter as fmtr
import itertools as it
import numpy as np
import read_maker
from statistics import mode
import sys


class OverlapEP(object):
    
    def __init__(self, read_length):
        self.read_length = read_length
        self.reads = []
        self.graph = {}
        self.result = []

    def build_graph_ep(self):
        self.perms = it.permutations(self.reads, 2)
        for pair in self.perms:
            r1, r2 = pair
            range_end = self.graph[r1][1]
            pos = 0
            for i in range(0, range_end):
                if self.hamming_dist(r1[i:], r2[:self.read_length-i]):
                    pos = int(i)
                    break
            if pos > 0:
                self.graph[r1] = (r2, pos)

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




#if __name__ == "__main__":
#    o = OverlapEP(100)
#    genome = fmtr.reader()
#    reads = read_maker.make_reads(genome, 1618)
#    for r in reads:
#        o.add_line(r)
#    o.build_graph_ep()



    
