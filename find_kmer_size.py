#python3
# -*- coding: utf-8 -*-
"""
Optimal k-mer Size
"""


class Graph(object):
    
    def __init__(self):
        self.node_set = []
        self.graph = {}
        self.degrees = {}
        self.components = {}
        
    def add_node(self, node):
        self.node_set.append(node)
        
    def divide_kmers(self, k):
        orgnl = len(self.node_set[0])
        if k == orgnl:
            return
        temp = []
        for node in self.node_set:
            for i in range(orgnl - k + 1):
                temp.append(node[i:i+k])
        self.node_set = list(temp)
        
    def make_graph(self):
        for node in self.node_set:
            self.components[node] = -1
            self.components[self.node_set[0]] = 1
        for kmer in self.node_set:
            if kmer in self.graph:
                self.graph[kmer[:-1]].append(kmer[1:])
                self.degrees[kmer[:-1]][0] += 1
                self.degrees[kmer[1:]][1] += 1
            else:
                self.graph[kmer[:-1]] = kmer[1:]
                self.degrees[kmer[:-1]] = [1,0]
                self.degrees[kmer[1:]] = [0,1]

                
                
    def has_euler(self):
        return True
    
    def run(self):
        pass
    
g = Graph()

l = ['ATCCGA']
g.add_node(l[0])
g.divide_kmers(2)
print(g.node_set)