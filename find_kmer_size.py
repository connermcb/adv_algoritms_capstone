#python3
# -*- coding: utf-8 -*-
"""
Optimal k-mer Size
"""
import sys

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
        for k in range(25, 1, -1):
            self.divide_kmers(k)
            self.make_graph()
            self.calc_degrees()
            if g.is_balanced():
                print(k)
                return
        return None


if __name__ == "__main__":
    
    g = Graph()
    for i in range(400):
        g.add_node(str(input()))
    g.run()
#for i in range(1618):
#c = str(sys.stdin.readline()).strip().split()
#g.add_node([c][0])
#
#g.run()

#for each in l:
#    g.add_node(each)
#g.divide_kmers(4)
#g.make_graph()
#g.calc_degrees()
#print(g.is_balanced())
#g.divide_kmers(3)
#g.make_graph()
#g.calc_degrees()
#print(g.graph)
#print(g.degrees)
#print(g.is_balanced())