import unittest
import keytocrypto

class TestKeyToCrypto(unittest.TestCase):
    def testNoChange(self):
        self.assertEqual(
            keytocrypto.encrypt("B", "A"),
            "B"
        )

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

    def testLongerCipherLength(self):
        self.assertEqual(
            keytocrypto.encrypt("D", "BC"),
            "E"
        )

    def testLetterWrapping(self):
        self.assertEqual(
            keytocrypto.encrypt("Y", "E"),
            "C"
        )
