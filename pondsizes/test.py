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

    def testVerticallyAdjacentWaterPond(self):
        self.assertItemsEqual(
            pondsizes.getPondSizes([(0, 0), (0, 1)]),
            [2]
        )

    def testMultipleVerticallyAdjacentWaterPonds(self):
        self.assertItemsEqual(
            pondsizes.getPondSizes([(0, 0), (0, 1), (3, 2), (3, 3), (3, 1)]),
            [3, 2]
        )

    def testDiagonallyAdjacentWaterPond(self):
        self.assertItemsEqual(
            pondsizes.getPondSizes([(0, 0), (1, 1), (0, 2), (2, 2), (2, 0)]),
            [5]
        )

    def testMultipleDiagonallyAdjacentWaterPonds(self):
        waterSquares = [
            (0, 0),
            (1, 1),
            (2, 0),
            (4, 1),
            (3, 2),
            (1, 3),
            (2, 4)
        ]

        self.assertItemsEqual(
            pondsizes.getPondSizes(waterSquares),
            [3, 2, 2]
        )

    def testAllAdjacencyTypes(self):
        waterSquares = [
            (0, 0),
            (3, 0),
            (0, 1),
            (2, 1),
            (2, 2),
            (0, 3),
            (2, 3)
        ]

        self.assertItemsEqual(
            pondsizes.getPondSizes(waterSquares),
            [2, 4, 1]
        )
