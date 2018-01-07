import unittest
import pondsizes

class TestPondSizes(unittest.TestCase):
    def testNoPonds(self):
        self.assertItemsEqual(
            pondsizes.getPondSizes([]),
            []
        )

    def testSingleWaterPond(self):
        self.assertItemsEqual(
            pondsizes.getPondSizes([(0, 0)]),
            [1]
        )

    def testMultipleSingleWaterPonds(self):
        self.assertItemsEqual(
            pondsizes.getPondSizes([(0, 0), (1, 2)]),
            [1, 1]
        )

    def testHorizontallyAdjacentWaterPond(self):
        self.assertItemsEqual(
            pondsizes.getPondSizes([(0, 0), (1, 0)]),
            [2]
        )

    def testMultipleHorizontallyAdjacentWaterPonds(self):
        self.assertItemsEqual(
            pondsizes.getPondSizes([(0, 0), (1, 0), (1, 2), (2, 2), (3, 2)]),
            [2, 3]
        )
