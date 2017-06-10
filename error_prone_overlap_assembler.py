#python3
# -*- coding: utf-8 -*-
"""
Overlap Assembler with Error-Prone Reads
"""
import itertools as it
import string
import sys


class OverlapEP(object):
    
    def __init__(self, read_length):
        self.read_length = read_length
        self.reads = []
        self.graph = {}
        self.result = ""

    def hamming_dist(self, r1, r2):
        dist = 0
        for i in range(len(r1)):
            if r1[i] != r2[i]:
                dist += 1
            if dist > 2:
                break
        return dist
                
    def build_graph_ep(self):
        self.perms = it.permutations(reads, 2)
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
                
    def assemble_genome(self):
        pass
    
    def trim(self):
        pos = 1
        while True:
            if self.result[:pos] == self.result[-pos:]:
                self.result = self.result[:-pos]
                return
            pos += 1
            
    