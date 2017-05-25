#python3
# -*- coding: utf-8 -*-
"""
Optimal k-mer Size
"""


class Graph(object):
    
    def __init__(self):
        self.reads = []
        self.node_set = []
        self.start = None
        self.graph = {}
        self.degrees = {}
        self.components = {}
        
    def add_node(self, node):
        self.reads.append(node)
        
    def divide_kmers(self, k):
        self.node_set = []
        orgnl = len(self.reads[0])
        if k == orgnl:
            self.node_set = list(self.reads)
            return
        for node in self.reads:
            for i in range(orgnl - k + 1):
                self.node_set.append(node[i:i+k])
        
    def make_graph(self):
        self.graph = {}
        self.start = self.node_set[0][:-1]
        for node in self.node_set:
            self.components[node[:-1]] = -1
            self.components[node[1:]] = -1
            self.components[self.node_set[0][:-1]] = 1
        for kmer in self.node_set:
            if kmer[:-1] in self.graph:
                self.graph[kmer[:-1]].append(kmer[1:])
            else:
                self.graph[kmer[:-1]] = [kmer[1:]]


    def calc_degrees(self):     
        self.degrees = {}
        nodes = self.graph.keys()
        for n in nodes:
            self.degrees[n] = [0,0]
        for n1 in nodes:
            for n2 in nodes:
                if n1[1:] == n2[:-1]:
                    self.degrees[n1][0] += 1
                    self.degrees[n2][1] += 1
        
        
    def is_connected(self):
        queue = [self.start]
        while queue:
            current = queue.pop(0)
            for each in self.graph[current]:
                self.components[each] = current
                queue.append(each)
        return True
    
    def is_balanced(self):
        if not self.degrees:
            return False
        for each in self.degrees.items():
            if each[1][0] != each[1][1]:
                return False
        return True
    
    def run(self):
        for k in range(100, 1, -1):
            self.divide_kmers(i)
            self.make_graph()
            self.calc_degrees()
            if g.is_balanced():
                print(k)
                return
    
g = Graph()

l = ['AACG','ACGT','CAAC','GTTG','TGCA']
for each in l:
    g.add_node(each)
g.divide_kmers(4)
g.make_graph()
g.calc_degrees()
print(g.is_balanced())
g.divide_kmers(3)
g.make_graph()
g.calc_degrees()
print(g.graph)
print(g.degrees)
print(g.is_balanced())