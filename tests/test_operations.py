import unittest
import math
from coordinate_lib.cartesian import Cartesian2D, Cartesian3D
from coordinate_lib.operations import translate, rotate, scale

class TestOperations(unittest.TestCase):
    def test_translate_2d(self):
        point = Cartesian2D(1, 2)
        translated_point = translate(point, 3, 4)
        self.assertEqual(translated_point.x, 4)
        self.assertEqual(translated_point.y, 6)

    def test_translate_3d(self):
        point = Cartesian3D(1, 2, 3)
        translated_point = translate(point, 3, 4, 5)
        self.assertEqual(translated_point.x, 4)
        self.assertEqual(translated_point.y, 6)
        self.assertEqual(translated_point.z, 8)

    def test_rotate_2d(self):
        point = Cartesian2D(1, 0)
        rotated_point = rotate(point, math.pi / 2)
        self.assertAlmostEqual(rotated_point.x, 0)
        self.assertAlmostEqual(rotated_point.y, 1)

    def test_scale_2d(self):
        point = Cartesian2D(1, 2)
        scaled_point = scale(point, 2, 3)
        self.assertEqual(scaled_point.x, 2)
        self.assertEqual(scaled_point.y, 6)

if __name__ == '__main__':
    unittest.main()
