characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def rot13(s):

    s = s.lower()
    encodedText = ""

    for char in s:
        if char in characters:
            x = characters.index(char)
            encodedText = encodedText + characters[x + 13]

        else:
            encodedText = encodedText + char

    return encodedText


message = "The quick brown fox jumps over the lazy dog"

encrypted = rot13(message)
print(encrypted)

decrypted = rot13(encrypted)
print(decrypted)
