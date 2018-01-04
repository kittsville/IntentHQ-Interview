def encryptLetter((letter, cipherLetter)):
    return chr(ord(letter) + ord(cipherLetter) - 65)

def encrypt(text, secret):
    ciphertext = (secret + text)[:len(text)]

    encryptedText = ''.join(map(encryptLetter, zip(text, ciphertext)))

    return encryptedText
