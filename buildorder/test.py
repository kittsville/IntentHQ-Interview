import unittest
import buildorder

class TestBuildOrder(unittest.TestCase):
    def testSingleProject(self):
        self.assertEqual(
            buildorder.getBuildOrder(["a"]),
            ["a"]
        )
