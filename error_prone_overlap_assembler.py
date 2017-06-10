#python3
# -*- coding: utf-8 -*-
"""
Overlap Assembler with Error-Prone Reads
"""
import itertools as it
from statistics import mode
import string
import sys


class OverlapEP(object):
    
    def __init__(self, read_length):
        self.read_length = read_length
        self.reads = []
        self.graph = {}
        self.result = []

    def add_line(self, line):
        self.reads.append(line)
        self.graph[line] = []

    def hamming_dist(self, r1, r2):
#        print(r1, r2)
        dist = 0
        for i in range(len(r1)):
            if r1[i] != r2[i]:
                dist += 1
            if dist > 2:
                return False
        return True
                
    def build_graph_ep(self):
        self.perms = it.permutations(self.reads, 2)
        for pair in self.perms:
            r1, r2 = pair
            range_end = self.read_length
            pos = 0
            for i in range(0, range_end-3):
                if len(self.graph[r1]) == 4:
                    break
                if self.hamming_dist(r1[i:], r2[:self.read_length-i]):
                    pos = int(i)
                    break
            if pos > 0:
                self.graph[r1].append((r2, pos))

    def get_cumulative_indices(self):
        self.cumulative_indices = {read:0 for read in self.reads}
#        nxt = self.reads[0]
        stack = [self.reads[0]]
        while stack:
            nxt = stack.pop(0)
            for each in self.graph[nxt]:
                self.cumulative_indices[each[0]] = self.cumulative_indices[nxt] + each[1]
                stack.append(each[0])
            if self.reads[0] in stack:
                break

            
               
    def build_overlaps(self):
        cumulative_idx = {read:0 for read in self.reads}
        nxt = None
        c_idx = 0
        stack = [each for each in self.graph[self.reads[0]]]
        self.result = [[ltr] for ltr in self.reads[0]]
        while stack:
            if nxt == self.reads[0]:
                break
            prv, nxt = nxt, stack.pop(0)
            cummulative_idx[nxt] = c_idx
            
            
        
    
    def trim(self):
        pos = 1
        while True:
            if self.result[:pos] == self.result[-pos:]:
                self.result = self.result[:-pos]
                return
            pos += 1

reads = ['ABCDEFGHIJ','CDEFGHIJKL','GHIJKLMNOP','MNOPQRSTUV','NOPQRSTUVW','QRSTUVWXYZ','UVWXYZABCD']
        
#genome = string.ascii_uppercase
#genome += genome[:10]
#reads = [genome[i:i+5] for i in range(len(genome)-5)]
o = OverlapEP(10)
for each in reads:
    o.add_line(each)
o.build_graph_ep()
print(o.graph)
o.get_cumulative_indices()
print(o.cumulative_indices)
#o.find_path()
#o.trim()
#print(o.result)   
    