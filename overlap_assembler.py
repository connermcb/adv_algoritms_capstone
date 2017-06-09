#python3
# -*- coding: utf-8 -*-
"""
Overlap Assembler
"""

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
        
    



reads = []
for i in range(1618):
    reads += [sys.stdin.readline().strip()]
o=Overlap(100)
for read in reads:
    o.add_line(read)
o.assemble()
print(o.result)
