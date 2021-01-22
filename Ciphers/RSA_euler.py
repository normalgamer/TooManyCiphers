# # # # # # # # # # # # # #
#                         #
#   Python RSA            #
#   From TooManyCiphers   #
#                         #
# # # # # # # # # # # # # #


## Libraries ##
import random
import hashlib


## Variables ##

#p = 61
#q = 53

p = 641203022169498012877450874795813077188312545981142618236319125709021145105944511081258287131770189310159040744223794886282682379478466551979481182942828264875265064486263690320831155037245820439115099378085146158014374486383392637373507793374077101979301740228578147019603175764743813643652695941759

q = 667785423503543738655154802573083008068638310792316733102764079217595714771911625209167046918670804689903058920550838394088169479748105073220495631704102086885035567036601549831724325505386657554115810765055124013163635316980396011292150231539683581926366794061403371212875482954810518931330978477517

public_key = (0, 0)
private_key = (0, 0)

c = ""
m = ""

e = 0
d = 0
n = 0
euler = 0


## Functions ##

# from https://stackoverflow.com/questions/47761383/proper-carmichael-function
def gcd(a, b):
    while (a > 0):
        b = b % a
        (a, b) = (b, a)
    return b


def generateKeys():
    global e, d, n, euler
    n = p * q
    euler = (p - 1) * (q - 1)

    e = random.randint(1, euler)
    while gcd(e, euler) != 1:
        e = random.randint(1, euler)

    d = pow(e, -1, euler)

    public_key = (n, e)
    private_key = (n, d)


def encodeRSA(message, e, n):
    global c
    message = [ord(char) for char in message]
    c = [pow(char, e, n) for char in message]

    return [hex(chr) for chr in c]


def decodeRSA(message, d, n):
    global m
    m = "".join([chr(pow(char, d, n)) for char in message])
    return m


def signRSA(message, d, n):
    md5 = hashlib.md5()
    md5.update(message.encode("utf-8"))
    md5 = md5.hexdigest()

    signature = pow(int(md5, 16), d, n)
    return signature


def verifyRSA(message, signature, e, n):
    md5 = hashlib.md5()
    md5.update(message.encode("utf-8"))
    md5 = md5.hexdigest()

    verification_signature = pow(signature, e, n)
    return verification_signature == int(md5, 16)


## Main ##

# Keys are saved to a text file
try:
    with open("key.txt", "r") as f:
        keys = f.readlines()
        n = int(keys[0])
        e = int(keys[1])
        d = int(keys[2])

except IOError:     # File with keys doesn't exist
    generateKeys()
    with open("key.txt", "w") as f:
        f.write(str(n))
        f.write("\n")
        f.write(str(e))
        f.write("\n")
        f.write(str(d))
        f.write("\n")


text = "The quick brown fox jumps over the lazy dog"
encrypted = encodeRSA(text, e, n)
print("Input: " + text + "\n")
print("Encrypted: ")
print(encrypted)


#  Convert from int to hex to int
#
#  print(encrypted[0])
#  print(hex(encrypted[0]))
#  print(int(hex(encrypted[0]), 16))


decrypted = decodeRSA([int(chr, 16) for chr in encrypted], d, n)
print("\nDecrypted: " + decrypted)
print("N length: " + str(n.bit_length()) + " bits")


encrypted = str(encrypted).replace("0x", "").replace("[", "").replace("]", "")\
    .replace("'", "")
signature = signRSA(str(encrypted), d, n)
print("\nVerified: " + str(verifyRSA(str(encrypted), signature, e, n)))
