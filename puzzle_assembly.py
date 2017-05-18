#python3
# -*- coding: utf-8 -*-
"""
Puzzle Assembly
"""
import itertools as It
import sys

class Puzzle(object):
    
    def __init__(self, dims):
        self.dims = dims
        self.results = [[None for i in range(dims)] for j in range(dims)]
        self.edge_test = ('black', 'black', 'black', 'black')
        self.corners = {(1, 1, 0, 0):(0, 0), (0, 1, 1, 0):(dims-1, 0), (0, 0, 1, 1):(dims-1, dims-1), (1, 0, 0, 1):(0, dims-1)}
        self.edges = {x:[] for x in range(4)}
        self.middle = []
        self.mid_idx = 1
        
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
    
    def sides(self):
        left_perms = It.permutations(self.edges[1])
        for each in left_perms:
            test = True
            for i in range(len(each)-1):
                if each[i][2] != each[i+1][0]:
                    test = False
            if test and each[0][0] == self.results[0][0][2] and each[-1][2]==self.results[self.dims-1][0][0]:
                for i in range(len(each)):
                    self.results[i+1][0] = each[i]
                break
        right_perms = It.permutations(self.edges[3])
        for each in right_perms:
            test = True
            for i in range(len(each)-1):
                if each[i][2] != each[i+1][0]:
                    test = False
            if test and each[0][0] == self.results[0][self.dims-1][2] and each[-1][2]==self.results[self.dims-1][self.dims-1][0]:
                for i in range(len(each)):
                    self.results[i+1][self.dims-1] = each[i]
                break        
    
    def center(self):
        if not self.middle:
            return
        center_perms = It.permutations(self.middle, self.dims - 2)
        for each in center_perms:
            test = True
            for i in range(len(each)-1):
                if each[i][3] != each[i+1][1]:
                    test = False
#            print(test, all([e1==e2 for e1, e2 in zip([item[0] for item in each],[item2 for item2 in self.results[self.mid_idx-1][1:-1]])]))
            if test and each[0][1] == self.results[self.mid_idx][0][3] and \
                        each[-1][3] == self.results[self.mid_idx][self.dims-1][1] and \
                        all([e1==e2 for e1, e2 in zip([item[0] for item in each],[item2[2] for item2 in self.results[self.mid_idx-1][1:-1]])]):

                self.results[self.mid_idx][1:-1] = each
                for sqr in each:
                    self.middle.remove(sqr)
                self.mid_idx += 1
                break
        self.center()

    def run(self):
        self.top_bottom()
        self.sides()
        self.center()
        for row in self.results:
            print(";".join([str(t) for t in row]).replace(' ', '').replace("'", ""))
                    
            
#p = Puzzle(4)
#
#l= [('black','black','green','red'),('black','red','blue','green'),('black','green','red','yellow'),('black','yellow','blue','black'),
#    ('green','black','blue','purple'),('blue','purple','purple','green'),('red','green','blue','yellow'),('blue','yellow','green','black'),
#    ('blue','black','yellow','green'),('purple','green','red','yellow'),('blue','yellow','green','purple'),('green','purple','yellow','black'),
#    ('yellow','black','black','purple'),('red','purple','black','purple'),('green','purple','black','blue'),('yellow','blue','black','black'),]
#
##l = [('yellow','black','black','blue'), 
##     ('blue','blue','black','yellow'), 
##     ('orange','yellow','black','black'),
##     ('red','black','yellow','green'),
##     ('orange','green','blue','blue'),
##     ('green','blue','orange','black'),
##     ('black','black','red','red'),
##     ('black','red','orange','purple'),
##     ('black','purple','green','black')]

p = Puzzle(5)
#l = ['(black,black,blue,cyan)',
# '(black,brown,maroon,red)',
# '(black,cyan,yellow,brown)',
# '(black,red,green,black)',
# '(black,red,white,red)',
# '(blue,black,orange,yellow)',
# '(blue,cyan,white,black)',
# '(brown,maroon,orange,yellow)',
# '(green,blue,blue,black)',
# '(maroon,black,yellow,purple)',
# '(maroon,blue,black,orange)',
# '(maroon,orange,brown,orange)',
# '(maroon,yellow,white,cyan)',
# '(orange,black,maroon,cyan)',
# '(orange,orange,black,black)',
# '(orange,purple,maroon,cyan)',
# '(orange,purple,purple,purple)',
# '(purple,brown,black,blue)',
# '(red,orange,black,orange)',
# '(white,cyan,red,orange)',
# '(white,orange,maroon,blue)',
# '(white,orange,orange,black)',
# '(yellow,black,black,brown)',
# '(yellow,cyan,orange,maroon)',
# '(yellow,yellow,yellow,orange)']
#print(len(l))
for i in range(25):
    line = sys.stdin.readline().strip()
    line = tuple(line[1:-1].split(','))
    p.read_data(line)
p.run()
        
   