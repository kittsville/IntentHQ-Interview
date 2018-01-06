import unittest
import keytocrypto

class TestKeyToCryptoEncryption(unittest.TestCase):
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

    def testLongText(self):
        self.assertEqual(
            keytocrypto.encrypt("SENDMOREMONKEYS", "ACM"),
            "SGZVQBUQAFRWSLC"
        )

class TestKeyToCryptoDecryption(unittest.TestCase):
    def testNoChange(self):
        self.assertEqual(
            keytocrypto.decrypt("B", "A"),
            "B"
        )

    def testSingleLetter(self):
        self.assertEqual(
            keytocrypto.decrypt("D", "B"),
            "C"
        )

    def testMultipleLetters(self):
        self.assertEqual(
            keytocrypto.decrypt("DE", "BC"),
            "CC"
        )

    def testShorterCipherLength(self):
        self.assertEqual(
            keytocrypto.decrypt("ED", "D"),
            "BC"
        )

    def testLongerCipherLength(self):
        self.assertEqual(
            keytocrypto.decrypt("E", "BC"),
            "D"
        )

    def testTestWrapping(self):
        self.assertEqual(
            keytocrypto.decrypt("C", "E"),
            "Y"
        )

    def testLongText(self):
        self.assertEqual(
            keytocrypto.decrypt("SGZVQBUQAFRWSLC", "ACM"),
            "SENDMOREMONKEYS"
        )

class TestKeyToCryptoIntegration(unittest.TestCase):
    def testEncryptionThenDecryption(self):
        originalText = "SENDMOREMONKEYS"
        key          = "ACM"

        encryptedText = keytocrypto.encrypt(originalText, key)
        decryptedText = keytocrypto.decrypt(encryptedText, key)

        self.assertEqual(
            decryptedText,
            originalText
        )

    def testDecryptionThenEncryption(self):
        originalEncryptedText = "SGZVQBUQAFRWSLC"
        key                   = "ACM"

        decryptedText = keytocrypto.decrypt(originalEncryptedText, key)
        encryptedText = keytocrypto.encrypt(decryptedText, key)

        self.assertEqual(
            encryptedText,
            originalEncryptedText
        )
