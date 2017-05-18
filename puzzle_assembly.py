# -*- coding: utf-8 -*-
"""
Puzzle Assembly
"""

class Puzzle(object):
    
    def __init__(self, dims):
        self.dims = dims
        self.results = [[] * dims]
        

        