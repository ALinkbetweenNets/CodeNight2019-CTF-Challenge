first = ord("A")

def encrypt(plainText, key):
    plainText = plainText.upper()
    key = key%26
    encrypted = ""
    for c in list(plainText):
        encrypted += chr((((ord(c)-first) + key)%26)+first)
        key = (key+1)%26
    return encrypted