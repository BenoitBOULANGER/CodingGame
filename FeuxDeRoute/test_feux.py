import unittest
import feux as f

class test_simple(unittest.TestCase):

    def test_time(self):
        time=f.get_time(36, 100)
        self.assertTrue(int(time) == 10)

    def test_light(self):
        speed = 50
        light=[200,15]
        self.assertTrue(f.verify_light(speed, light))

        speed = 50
        light=[200,10]
        self.assertFalse(f.verify_light(speed, light))

        speed = 40
        light=[200,10]
        self.assertFalse(f.verify_light(speed, light))

        speed = 36
        light=[200,10]
        self.assertTrue(f.verify_light(speed, light))


if __name__ == '__main__':
    unittest.main()