import math
import unittest


def transform_time_to_cyclic(time):
    radians = 2 * math.pi * time / 24
    return math.sin(radians), math.cos(radians)


def time_difference(time1, time2):
    sin1, cos1 = transform_time_to_cyclic(time1)
    sin2, cos2 = transform_time_to_cyclic(time2)

    return math.acos(sin1 * sin2 + cos1 * cos2) * (24 / (2 * math.pi))


# Unit tests
class TestCyclicTimeFeatures(unittest.TestCase):

    def test_transform_time_to_cyclic(self):
        self.assertAlmostEqual(transform_time_to_cyclic(0), (0, 1), places=5)
        self.assertAlmostEqual(transform_time_to_cyclic(6), (1, 0), places=5)
        self.assertAlmostEqual(transform_time_to_cyclic(12), (0, -1), places=5)
        self.assertAlmostEqual(transform_time_to_cyclic(18), (-1, 0), places=5)

    def test_time_difference_same_day(self):
        self.assertAlmostEqual(time_difference(10, 12), 2, places=5)
        self.assertAlmostEqual(time_difference(23, 1), 2, places=5)

    def test_time_difference_across_midnight(self):
        self.assertAlmostEqual(time_difference(23, 0), 1, places=5)
        self.assertAlmostEqual(time_difference(23, 2), 3, places=5)

    def test_time_difference_no_difference(self):
        self.assertAlmostEqual(time_difference(5, 5), 0, places=5)
        self.assertAlmostEqual(time_difference(0, 0), 0, places=5)


if __name__ == "__main__":
    unittest.main()
