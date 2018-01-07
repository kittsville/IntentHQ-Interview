import unittest
import pondsizes

class TestPondSizes(unittest.TestCase):
    def testNoPonds(self):
        self.assertItemsEqual(
            pondsizes.getPondSizes([]),
            []
        )
