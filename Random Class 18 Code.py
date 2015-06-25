#These functions encrypt and decrypt text messages.

import random

shift = random.randint(0, 69)

def encrypt(word):
    codedword = ""
    for letter in word:
        codedword += chr(ord(letter) + shift)
    return codedword

result1 = encrypt("my name is jeremy")



def decrypt(word):
    decodedword = ""
    for letter in word:
        decodedword += chr(ord(letter) - shift)
    return decodedword

result2 = decrypt(result1)
