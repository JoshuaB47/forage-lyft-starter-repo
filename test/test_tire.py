import unittest
import sys
sys.path.insert(0, sys.path[0] + '/../')

from New_Design.tire import OctoprimeTire, CarriganTire

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        # sum is 3
        tire_array = [1, 1, 0.5, 0.5]
        tire = OctoprimeTire(tire_array)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        # sum is 2.9
        tire_array = [0.9, 1, 0.5, 0.5]
        tire = OctoprimeTire(tire_array)

        self.assertFalse(tire.needs_service())

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        # an element is 0.9
        tire_array = [0.9, 0.5, 0.5, 0.5]
        tire = CarriganTire(tire_array)

        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        # no element is >= 0.9
        tire_array = [0.8, 0.7, 0.5, 0.5]
        tire = OctoprimeTire(tire_array)

        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()