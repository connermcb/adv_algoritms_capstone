#python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:37:27 2017

@author: User
"""
import sys

class Euler(object):
    
    def __init__(self, start, n):
        self.start = start
        self.d = {num:[] for num in range(1,n+1)}
        self.degrees = {num:[0, 0] for num in range(1,n+1)}
        self.circuit =[]
        self.current = -1
    
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
        for each in self.degrees:
            if self.degrees[each][0] != self.degrees[each][1]:
                print(0)
                return
        self.circuit.append(self.start)
        self.eulerian_cycles()
        print(1)
        print(" ".join([str(x) for x in self.circuit][:-1]))

#n, m = (3, 4)
#l = [(1, 3), (2, 3), (1, 2), (3, 1)]      
#n, m = (4, 7)
#l = [(2, 3), (3, 4), (1, 4), (3, 1), (4, 2), (2, 3), (4, 2)]
#e = Euler(1, n)
#n, m = (4, 7)
#l = [(1, 2), (2, 1), (1, 4), (4, 1), (2, 4), (3, 2), (4, 3)]                
#n,m = (7, 11)
#
#l = [(1, 2), (1, 6), (2, 3), (3, 1), (3, 4), (4, 1), (6, 5), (6, 7), (5, 7), (7, 3), (7, 6)]
#e = Euler(1)
#n, m = (3,4)
#e = Euler(1, n)
#l =[(2, 2), (2, 3), (3, 1), (1, 2)]
#for each in l:
#    v, w = each
#    e.d[v].append(w)
#    e.degrees[v][0] += 1
#    e.degrees[w][1] += 1    
#e.run()


n, m = (int(x) for x in sys.stdin.readline().split(" "))
e = Euler(1, n)
for i in range(m):
    v, w = (int(x) for x in sys.stdin.readline().split(" "))
    e.d[v].append(w)
    e.degrees[v][0] += 1
    e.degrees[w][1] += 1

e.run()      
