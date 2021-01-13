## Key Generation ##

a = 5
b = 25
a_prime = 12
b_prime = 45

M = a*b-1
e = a_prime*M+a
d = b_prime*M+b
n = int((e*d-1)/M)

#public_key = (n, e)
#private_key = (n, d)

text = "The quick brown fox jumps over the lazy dog"

text_input = [ord(char) for char in text]

encrypted = [(char*e)%n for char in text_input]
x = bytes("".join([chr(int(char)) for char in encrypted]).encode("utf-8"))

print(x)

decrypted = "".join([chr((char*d)%n) for char in encrypted])
print(decrypted)



with open("Kid_RSA.txt", "w") as f:
    f.writelines("Encrypted: ")
with open("Kid_RSA.txt", "ab") as f:
    f.write(x)
with open("Kid_RSA.txt", "a") as f:
    f.writelines("\n")
    f.writelines("Decrypted: " + decrypted)

input()