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
        self.graph[line] = (None, self.read_length)
        
    def build_graph(self):
        self.perms = it.permutations(reads, 2)
        for pair in self.perms:
            r1, r2 = pair
            range_end = self.graph[r1][1]
            pos = 0
            for i in range(0, range_end):
                if r1[i:] == r2[:self.read_length-i]:
                    pos = int(i)
                    break
            if pos > 0:
                self.graph[r1] = (r2, pos)

    def find_path(self):
        nxt = self.reads[0]
        self.result += nxt
        for i in range(len(self.graph)):
            nxt, pos = self.graph[nxt]
            self.result += nxt[self.read_length-pos:]
            
    
    
        
    
#genome = string.ascii_uppercase
#genome += genome[:10]
#reads = [genome[i:i+5] for i in range(len(genome)-5)]
#o = Overlap(5)
#for each in reads:
#    o.add_line(each)
#o.build_graph()
#o.find_path()
reads = []
for i in range(1618):
    reads += [sys.stdin.readline().strip()]
o=Overlap(100)
for read in reads:
    o.add_line(read)
o.build_graph()
o.find_path()
print(o.result)

