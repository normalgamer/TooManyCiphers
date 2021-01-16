import os


# Alphabet split between lines to keep 80 characters per line
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encodeVigenère(message, key):

    encrypted = list()
    temp = list()

    message.lower()
    key.lower()

    key = [char for char in key]

    while len(key) < len(message):
        key.extend(key)

    for m, k in zip(message, key):
        temp = list()
        i = alphabet.index(k)
        while i <= 25:
            temp.append(alphabet[i])
            i += 1
        i = 0
        while i < alphabet.index(k):
            temp.append(alphabet[i])
            i += 1

        if m in alphabet:
            encrypted.append(temp[alphabet.index(m)])
        else:
            # If the message contains numbers or punctuation marks,
            # these will be ignored
            encrypted.append(m)

    return "".join([char for char in encrypted])  # Returns a string


def decodeVigenère(message, key):

    decrypted = list()
    temp = list()

    message.lower()
    key.lower()

    key = [char for char in key]

    while len(key) < len(message):
        key.extend(key)

    for m, k in zip(message, key):
        temp = list()
        i = alphabet.index(k)
        while i <= 25:
            temp.append(alphabet[i])
            i += 1
        i = 0
        while i < alphabet.index(k):
            temp.append(alphabet[i])
            i += 1

        if m in alphabet:
            decrypted.append(alphabet[temp.index(m)])
        else:
            # If the message contains numbers or punctuation marks,
            # these will be ignored
            decrypted.append(m)

    return "".join([char for char in decrypted])  # Returns a string


# Input message and key must be strings
# Uppercase letters will be converted into lowercase
message = "The quick brown fox jumps over the lazy dog"
key     = "password"

encrypted = encodeVigenère(message, key)
print(encrypted)

decrypted = decodeVigenère(encrypted, key)
print(decrypted)
