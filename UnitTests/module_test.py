from module import cube
import unittest


# call py -m unittest .\module_test.py

class TestCubes(unittest.TestCase):
    def test_volume_cube(self):
        self.assertAlmostEqual(cube(1), 1 ,"should be 1")
        self.assertAlmostEqual(cube(3), 27,"should be 27")
        
    def test_input_value(self):
        self.assertRaises(TypeError, cube, True)