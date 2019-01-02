#!/usr/bin/env python3

import unittest
import bataille as b

class test_simple(unittest.TestCase):

    def test_simple(self):
        b.cards_p1 = ['10D']
        b.cards_p2 = ['9S']
        b.one_run()
        self.assertTrue(len(b.cards_p1) == 2)
        self.assertTrue(len(b.cards_p2) == 0)
        self.assertTrue(b.cards_p1[0] == '10D')
        self.assertTrue(b.cards_p1[1] == '9S')

    def test_bataille_simple(self):
        b.cards_p1 = ['10D','8D', '7S', 'AH', 'KD']
        b.cards_p2 = ['10S', 'AD', '2D', 'QH', '10H']
        b.display()
        b.one_run()
        b.display()
        self.assertTrue(len(b.cards_p1) == 10)
        self.assertTrue(len(b.cards_p2) == 0)
        self.assertTrue(b.cards_p1[0] == '10D')
        self.assertTrue(b.cards_p1[2] == '7S')
        self.assertTrue(b.cards_p1[4] == 'KD')
        self.assertTrue(b.cards_p1[5] == '10S')
        self.assertTrue(b.cards_p1[8] == 'QH')

    def test_nested_bataille(self):
        b.cards_p1 = ['10D', '8D', '7S', 'AH', 'KD','8D', '7S', 'AH', 'JH']
        b.cards_p2 = ['10S', 'AD', '2D', 'QH', 'KH', 'AD', '2D', 'QH', 'QD']
        b.display()
        b.one_run()
        b.display()
        self.assertTrue(len(b.cards_p1) == 0)
        self.assertTrue(len(b.cards_p2) == 18)
        self.assertTrue(b.cards_p2[0] == '10D')
        self.assertTrue(b.cards_p2[2] == '7S')
        self.assertTrue(b.cards_p2[4] == 'KD')
        self.assertTrue(b.cards_p2[5] == '8D')
        self.assertTrue(b.cards_p2[8] == 'JH')
        self.assertTrue(b.cards_p2[10] == 'AD')
        self.assertTrue(b.cards_p2[12] == 'QH')

if __name__ == '__main__':
    unittest.main()