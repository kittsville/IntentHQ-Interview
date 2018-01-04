def encryptLetter((letter, cipherLetter)):
    encryptedLetter = ord(letter) + ord(cipherLetter) - 65

    if encryptedLetter > 90:
        encryptedLetter -= 26

    return chr(encryptedLetter)

def encrypt(text, secret):
    ciphertext = (secret + text)[:len(text)]

    encryptedText = ''.join(map(encryptLetter, zip(text, ciphertext)))

    return encryptedText

def decryptLetter((letter, ciphertext)):
    return chr(ord(letter) - ord(ciphertext) + 65)

def decrypt(encryptedText, secret):
    text = ''.join(map(decryptLetter, zip(encryptedText, secret)))

    return text
