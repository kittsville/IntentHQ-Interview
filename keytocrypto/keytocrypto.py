def encryptLetter((letter, cipherLetter)):
    encryptedLetter = ord(letter) + ord(cipherLetter) - 65

    if encryptedLetter > 90:
        encryptedLetter -= 26

    return chr(encryptedLetter)

def encrypt(text, secret):
    ciphertext = (secret + text)[:len(text)]

    encryptedText = ''.join(map(encryptLetter, zip(text, ciphertext)))

    return encryptedText
