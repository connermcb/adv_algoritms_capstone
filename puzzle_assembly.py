# -*- coding: utf-8 -*-
"""
Puzzle Assembly
"""
import itertools as It

class Puzzle(object):
    
    def __init__(self, dims):
        self.dims = dims
        self.results = [[None for i in range(dims)] for j in range(dims)]
        self.edge_test = ('black', 'black', 'black', 'black')
        self.corners = {(1, 1, 0, 0):(0, 0), (0, 1, 1, 0):(dims-1, 0), (0, 0, 1, 1):(dims-1, dims-1), (1, 0, 0, 1):(0, dims-1)}
        self.edges = {x:[] for x in range(4)}
        self.middle = []
        
    def read_data(self, line):
        test = [int(i==j) for i, j in zip(line, self.edge_test)]
        if tuple(test) in self.corners:
            _get_match = [t for t in self.corners if t == tuple(test)][0] 
            row, col = self.corners[_get_match]
            self.results[row][col] = line
            return 
        elif 1 in test:
            edge_key = test.index(1)
            self.edges[edge_key].append(line)
        else:
            self.middle.append(line)
        return
        
    def top_bottom(self):
        top_perms = It.permutations(self.edges[0])
        for each in top_perms:
            test = True
            for i in range(len(each)-1):
                if each[i][3] != each[i+1][1]:
                    test = False
            if test and each[0][1] == self.results[0][0][3] and each[-1][3]==self.results[0][self.dims-1][1]:
                self.results[0][1:-1] = each
                break
        bottom_perms = It.permutations(self.edges[2])
        for each in bottom_perms:
            test = True
            for i in range(len(each)-1):
                if each[i][3] != each[i+1][1]:
                    test = False
            if test and each[0][1] == self.results[self.dims-1][0][3] and each[-1][3]==self.results[self.dims-1][self.dims-1][1]:
                self.results[self.dims-1][1:-1] = each
        return
                
        
        
p = Puzzle(4)

l= [('black','black','green','red'),('black','red','blue','green'),('black','green','red','yellow'),('black','yellow','blue','black'),
    ('green','black','blue','purple'),('blue','purple','purple','green'),('red','green','blue','yellow'),('blue','yellow','green','black'),
    ('blue','black','yellow','green'),('purple','green','red','yellow'),('blue','yellow','green','purple'),('green','purple','yellow','black'),
    ('yellow','black','black','purple'),('red','purple','black','purple'),('green','purple','black','blue'),('yellow','blue','black','black'),]

#l = [('yellow','black','black','blue'), 
#     ('blue','blue','black','yellow'), 
#     ('orange','yellow','black','black'),
#     ('red','black','yellow','green'),
#     ('orange','green','blue','blue'),
#     ('green','blue','orange','black'),
#     ('black','black','red','red'),
#     ('black','red','orange','purple'),
#     ('black','purple','green','black')]

for line in l:
    p.read_data(line)
print(p.top_bottom())
print(p.results)
        
        