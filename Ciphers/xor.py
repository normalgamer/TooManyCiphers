import os


def xor(a, b):

    if type(a) == bytearray or type(a) == bytes:
        message = a
    else:
        message = bytes(bytes(a.encode()))

    if type(b) == bytes:
        key = b
    else:
        key = bytearray(b.encode())

    while (len(key) < len(message)):
        key.extend(key)

    result = bytearray()
    for a, b in zip(message, key):
        result.append(a ^ b)

    return result  # Returns a bytearray


# Input message
message = "Confidential, don't show anyone"

# Key to be used, type = string
# key = "This is the key"

# Alternatively, use os.urandom(len(message)), for a randomized OTP
key = os.urandom(len(message))


encrypted = xor(message, key)

# The encrypted result is returned as a bytearray, it can't be decoded
print(encrypted)


decrypted = xor(encrypted, key)

# Decrypted result can be decoded
print(decrypted.decode())


# The encryption/decryption key and the encrypted output can be written to a
# file in binary mode, and later read and decrypted

# Write encrypted output and key
with open("xor_encrypted.txt", "wb") as f:
    f.write(encrypted)
with open("xor_key.txt", "wb") as f:
    f.write(key)

# Read key and encrypted text and decryption
with open("xor_key.txt", "rb") as f:
    read_key = f.read()
with open("xor_encrypted.txt", "rb") as f:
    input = f.read()
    decrypted = xor(input, read_key)
