import unittest
from coordinate_lib.cartesian import Cartesian2D, Cartesian3D

class TestCartesian(unittest.TestCase):
    def test_cartesian2d(self):
        point = Cartesian2D(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

    def test_cartesian3d(self):
        point = Cartesian3D(3, 4, 5)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)
        self.assertEqual(point.z, 5)

if __name__ == '__main__':
    unittest.main()
