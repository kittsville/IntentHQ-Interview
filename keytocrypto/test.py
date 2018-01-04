import unittest
import keytocrypto

class TestKeyToCrypto(unittest.TestCase):
    def testSingleLetter(self):
        self.assertEqual(
            keytocrypto.encrypt("B", "C"),
            "D"
        )

    def testMultipleLetters(self):
        self.assertEqual(
            keytocrypto.encrypt("AB", "EE"),
            "EF"
        )

    def testShorterCipherLength(self):
        self.assertEqual(
            keytocrypto.encrypt("AB", "C"),
            "CB"
        )
