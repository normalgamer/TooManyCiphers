import os


characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encodeCaesar(s, i):

    s = s.lower()
    encodedText = ""

    for char in s:
        if char in characters:
            x = characters.index(char)
            encodedText = encodedText + characters[x + i]

        else:
            encodedText = encodedText + char

    return encodedText


def decodeCaesar(s, i):

    s = s.lower()
    decodedText = ""

    for char in s:
        if char in characters:
            x = characters.index(char)
            decodedText = decodedText + characters[x - i]
        else:
            decodedText = decodedText + char

    return decodedText


# Message must be a string, the key an integer
message = "The quick brown fox jumps over the lazy dog"
key = 2

encrypted = encodeCaesar(message, key)
print(encrypted)

decrypted = decodeCaesar(encrypted, key)
print(decrypted)
