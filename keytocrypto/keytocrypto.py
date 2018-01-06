def encryptLetter((letter, cipherLetter)):
    encryptedLetter = ord(letter) + ord(cipherLetter) - 65

    if encryptedLetter > 90:
        encryptedLetter -= 26

    return chr(encryptedLetter)

def encrypt(text, secret):
    ciphertext = (secret + text)[:len(text)]

    encryptedText = ''.join(map(encryptLetter, zip(text, ciphertext)))

    return encryptedText

def decryptLetter((encryptedLetter, cipherLetter)):
    letter = ord(encryptedLetter) - ord(cipherLetter) + 65

    if letter < 65:
        letter += 26

    return chr(letter)

def decrypt(encryptedText, secret):
    text = ''.join(map(decryptLetter, zip(encryptedText, secret)))

    if len(text) == len(encryptedText):
        return text

    offset = len(encryptedText) - len(text)

    for i in xrange(offset, len(encryptedText)):
        cipherPosition  = i - offset
        cipherLetter    = text[cipherPosition]
        encryptedLetter = encryptedText[i]
        text           += decryptLetter((encryptedLetter, cipherLetter))

    return text
