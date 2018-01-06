import unittest
import buildorder

class TestBuildOrder(unittest.TestCase):
    def testNoDependencies(self):
        self.assertEqual(
            buildorder.getBuildOrder(["a"]),
            ["a"]
        )

    def testSameDependency(self):
        projects     = ["a", "b", "c"]
        dependencies = [("a", "b"), ("a", "c")]

        self.assertEqual(
            buildorder.getBuildOrder(projects, dependencies),
            ["a", "b", "c"]
        )

    def testMultipleDependencies(self):
        projects     = ["a", "b", "c"]
        dependencies = [("a", "c"), ("b", "c")]

        self.assertEqual(
            buildorder.getBuildOrder(projects, dependencies),
            ["a", "b", "c"]
        )

    def testUnresolvableDependencies(self):
        projects     = ["a", "b", "c", "d"]
        dependencies = [("a", "b"), ("b", "c"), ("c", "a")]

        with self.assertRaises(buildorder.DependencyError):
            buildorder.getBuildOrder(projects, dependencies)

    def testChainedDependencies(self):
        projects     = ["a", "b", "c"]
        dependencies = [("a", "b"), ("b", "c")]

        self.assertEqual(
            buildorder.getBuildOrder(projects, dependencies),
            ["a", "b", "c"]
        )

    def testOverlappingChainedDependencies(self):
        projects     = ["a", "b", "c"]
        dependencies = [("b", "a"), ("c", "b"), ("c", "a")]

        self.assertEqual(
            buildorder.getBuildOrder(projects, dependencies),
            ["c", "b", "a"]
        )
