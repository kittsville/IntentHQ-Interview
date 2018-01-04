def encryptLetter((letter, cipherLetter)):
    return chr(ord(letter) + ord(cipherLetter) - 65)

def encrypt(text, secret):
    ciphertext = secret

    encryptedText = ''.join(map(encryptLetter, zip(text, ciphertext)))

    return encryptedText
