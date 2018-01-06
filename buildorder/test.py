import unittest
import buildorder

class TestBuildOrder(unittest.TestCase):
    def testSingleProject(self):
        self.assertEqual(
            buildorder.getBuildOrder(["a"]),
            ["a"]
        )

    def testProjectsWithSameDependency(self):
        projects     = ["a", "b", "c"]
        dependencies = [("a", "b"), ("a", "c")]

        self.assertEqual(
            buildorder.getBuildOrder(projects, dependencies),
            ["a", "b", "c"]
        )
