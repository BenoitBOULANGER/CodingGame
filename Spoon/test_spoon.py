#!/usr/bin/env python3

import unittest
import spoon as sp

class test_simple(unittest.TestCase):

    def test_simple(self):
        sp.neighbours=[]
        data=[['0','0'], ['0','.']]
        sp.solve(data)
        sp.display_neighbours()

        self.assertTrue(sp.neighbours[0] == [0,0,1,0,0,1])
        self.assertTrue(sp.neighbours[1] == [1,0,-1,-1,-1,-1])
        self.assertTrue(sp.neighbours[2] == [0,1,-1,-1,-1,-1])

    def test_line(self):
        sp.neighbours=[]
        data = ['0', '0', '0']
        sp.solve(data)
        sp.display_neighbours()
        self.assertTrue(sp.neighbours[0]) == [0,0,1,0,-1,-1]
        self.assertTrue(sp.neighbours[0]) == [1,0,2,0,-1,-1]
        self.assertTrue(sp.neighbours[0]) == [2,0,-1,-1,-1,-1]

if __name__ == '__main__':
    unittest.main()