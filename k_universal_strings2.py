#python3
# -*- coding: utf-8 -*-
"""
k-Universal String
"""
import itertools as it
import sys


class Universal(object):
    
    def __init__(self, k):
        self.k = k
        self.start = 0
        self.k_mers = [''.join(each) for each in list(it.product(['0','1'], repeat=k))]  
        self.node_set = set([])
        for kmer in self.k_mers:
            self.node_set.add(kmer[1:])
            self.node_set.add(kmer[:-1])
        self.node_set = list(self.node_set)
        self.d = {}
        self.circuit =[]
        self.current = -1
        
    def make_graph(self):
        for kmer in self.node_set:
            dec = 0
            kmer_temp = kmer[::-1]
            for i in range(len(kmer)):
                dec += 2**i * int(kmer_temp[i])
            self.d[dec] = [dec*2%(2**len(kmer)), dec*2%(2**len(kmer))+1]
                
    def walk(self):
        if self.start in self.d[self.start]:
            self.current = self.start
            self.d[self.start].remove(self.start)
        else:
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

    def deci_to_binary(self, num):
        if num == 0:
            return '0'*(self.k-1)
        if num == 1:
            return '0'*(self.k-2)+'1'
        binary = ''
        while num > 0:
            x = num%2
            binary+=str(x)
            num = num//2
        return binary[::-1]
        
    def run(self):
        self.make_graph()
        self.circuit.append(self.start)
        self.eulerian_cycles()
        self.circuit = self.circuit[:-1]
        self.circuit = [self.deci_to_binary(num) for num in self.circuit]
        result = "".join([each[-1] for each in self.circuit])
        print(result)

    
k = int(sys.stdin.readline().split()[0])
u = Universal(k)
u.run()