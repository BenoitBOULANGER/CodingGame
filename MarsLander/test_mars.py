import unittest
import mars as m

class test_simple(unittest.TestCase):

    def test_landing_zone(self):
        surface=[[0, 100], [1000, 500], [1500, 1500], [3000, 1000], [4000, 150], [5500, 150], [6999, 800]]
        assert(m.get_landing_zone(surface) == (4000, 5500, 150))

    def test_y(self):
        assert(m.get_y(0,2, 2,0, 1) == 1)
        assert(m.get_y(200, 0,200, 300, 100) == 133)
        assert(m.get_y(0,-100,-100, 100, 100) == 0)

    def test_get_current_ground_high(self):
        m.surface = [[0, 100], [1000, 500], [1500, 1500], [3000, 1000], [4000, 150], [5500, 150], [6999, 800]]

        assert(m.get_current_ground_high(500) == 300)
        assert(m.get_current_ground_high(5000) == 150)

    def test_max_ground_high(self):
        m.surface = [[0, 100], [1000, 500], [1500, 1500], [3000, 1000], [4000, 150], [5500, 150], [6999, 800]]

        assert(m.get_max_ground_high(0, 4000) == 1500)
        assert(m.get_max_ground_high(500, 4000) == 1500)
        assert(m.get_max_ground_high(2000, 4000) == 1000)
        assert(m.get_max_ground_high(3500, 4500) == 150)

if __name__ == '__main__':
    unittest.main()