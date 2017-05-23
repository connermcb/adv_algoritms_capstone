# -*- coding: utf-8 -*-
"""
De Bruijn - Genome Assembler
"""
import random
import sys

class Assemble(object):
    
    def __init__(self, n=5396):
        self.start = None
        self.d = {}
        self.circuit =[]
        self.current = -1
    
    def add_kmer(self, kmer):
        self.d[kmer] = []
        
    def make_graph(self):
        for kmer in self.d.keys():
            for kmer2 in self.d.keys():
                if kmer[1:] == kmer2[:-1]:
                   self.d[kmer].append(kmer2)
        self.start = list(self.d.keys())[1]
    
    def walk(self):
        self.current = self.d[self.start].pop()
        while self.current != self.start:
            self.circuit.append(self.current)
            if self.current in self.d[self.current]:
                self.d[self.current].remove(self.current)
            else:
                self.current = self.d[self.current].pop()
        self.circuit.append(self.current)
    
    def eulerian_cycles(self):
        self.walk()
        for i in list(set(self.circuit)):
            if len(self.d[i]) > 0:
                self.start = i
                cut = self.circuit.index(i)
                self.circuit = self.circuit[cut:-1] + self.circuit[:cut] + [self.start]
                self.eulerian_cycles()
        return self.circuit


    def run(self):
        self.circuit.append(self.start)
        self.eulerian_cycles()
        print(self.circuit[0] + "".join([str(x)[-1] for x in self.circuit][1:-10]))
        
#l =['AAC',  'ACG', 'CGT', 'GTA', 'TAA']
l= ['ACGTTAGGCT', 'CGTTAGGCTA', 'GTTAGGCTAC', 'TTAGGCTACG', 'TAGGCTACGT', 'AGGCTACGTA',
    'GGCTACGTAT', 'GCTACGTATT', 'CTACGTATTA', 'TACGTATTAA', 'ACGTATTAAC', 'CGTATTAACG',
    'GTATTAACGT', 'TATTAACGTT', 'ATTAACGTTA', 'TTAACGTTAG', 'TAACGTTAGG', 'AACGTTAGGC']
a =Assemble()
for each in l:
    a.add_kmer(each)
a.make_graph()
print(a.d.items())
a.run()