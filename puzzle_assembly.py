# -*- coding: utf-8 -*-
"""
Puzzle Assembly
"""

class Puzzle(object):
    
    def __init__(self, dims):
        self.dims = dims
        self.results = [[] * dims]
        self.corners = {(1, 1, 0, 0):(0, 0), (0, 1, 1, 0):(0, 4), (0, 1, 1, 0):(4, 0), (1, 0, 0, 1):(4, 4)}
        self.top = []
        self.left = []
        self.right = []
        self.bottom = []
        
    def read_data(self, line):
        
        
        