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
        
        
    def make_graph(self, k):
        for node1 in self.node_set:
            for node2 in self.node_set:
                
                
    def has_euler(self):
        return True
    
    def run(self):
        pass