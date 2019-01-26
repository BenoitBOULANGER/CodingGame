#!/usr/bin/env python3.4

import unittest
import batman as bat

class test_simple(unittest.TestCase):

    def test_simple(self):
        bat.high=40
        bat.get_next_vertical_position(20, "D")

if __name__ == '__main__':
    unittest.main()