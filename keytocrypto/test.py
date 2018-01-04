import unittest
import keytocrypto

class TestKeyToCrypto(unittest.TestCase):
    def testSingleLetter(self):
        ciphertext = keytocrypto.encrypt("B", "C")

        self.assertEqual(
            ciphertext,
            "D"
        )

    def testMultipleLetters(self):
        ciphertext = keytocrypto.encrypt("AB", "EE")

        self.assertEqual(
            ciphertext,
            "EF"
        )
