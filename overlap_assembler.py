#python3
# -*- coding: utf-8 -*-
"""
Overlap Assembler
"""
import itertools as it
import string

import sys

class Overlap(object):
    
    def __init__(self, read_length):
        self.read_length = read_length
        self.reads = []
        self.graph = {}
        self.result = ""
    
    def add_line(self, line):
        self.reads.append(line)
        self.graph[line] = []
        
    def build_graph(self):
        self.perms = it.permutations(reads, 2)
        for pair in self.perms:
            r1, r2 = pair
            pos = 0
            for i in range(0, self.read_length):
                if r1[-i:] == r2[:i]:
                    pos = int(i)
            if pos > 0:
                self.graph[r1].append((r2, pos))

    def find_path(self):
        nxt = self.reads[0]
        self.result += nxt
        for i in range(len(self.reads)):
            nxt, pos = max(self.graph[nxt], key=lambda x:x[1])
            self.result += nxt[pos:]
            
    
    
        
    
#genome = string.ascii_uppercase
#genome += genome[:10]
#reads = [genome[i:i+5] for i in range(len(genome)-5)]
#print(reads)
#o = Overlap(5)
#for each in reads:
#    o.add_line(each)
#o.build_graph()
#o.find_path()
#print(o.result)
reads = []
for i in range(1618):
    reads += [sys.stdin.readline().strip()]
o=Overlap(100)
for read in reads:
    o.add_line(read)
o.build_graph()
o.find_path()
print(o.result)

