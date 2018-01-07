import unittest
import livingpeople

class TestLivingPeople(unittest.TestCase):
    def testSinglePerson(self):
        self.assertEqual(
            livingpeople.getMostAliveDate([(1994, 2054)]),
            1994
        )
