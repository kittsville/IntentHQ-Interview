import unittest
import livingpeople

class TestLivingPeople(unittest.TestCase):
    def testSinglePerson(self):
        self.assertEqual(
            livingpeople.getMostAliveDate([(1994, 2054)]),
            1994
        )

    def testTwoPeople(self):
        self.assertEqual(
            livingpeople.getMostAliveDate([(1998, 2065), (1994, 1997)]),
            1994
        )

    def testOverlappingPeople(self):
        self.assertEqual(
            livingpeople.getMostAliveDate([(1994, 2054), (1965, 2034)]),
            1994
        )
