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

    def testProjectWithMultipleDependencies(self):
        projects     = ["a", "b", "c"]
        dependencies = [("a", "c"), ("b", "c")]

        self.assertEqual(
            buildorder.getBuildOrder(projects, dependencies),
            ["a", "b", "c"]
        )

    def testProjectWithUnresolvableDependencies(self):
        projects     = ["a", "b", "c", "d"]
        dependencies = [("a", "b"), ("b", "c"), ("c", "a")]

        with self.assertRaises(buildorder.DependencyError):
            buildorder.getBuildOrder(projects, dependencies)
