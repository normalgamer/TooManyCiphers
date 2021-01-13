## Variables
import random


p = 61
q = 53


public_key = (0,0)
private_key = (0,0)

c = ""
m = ""

e = 0
d = 0
n = 0

## Functions ##
# from https://stackoverflow.com/questions/47761383/proper-carmichael-function
def gcd(a,b):
    while (a>0):
        b=b%a
        (a,b)=(b,a)
    return b    

def carmichael(n):
    n=int(n)
    k=2
    a=1
    alist=[]

    while not ((gcd(a,n))==1):
        a=a+1

    while ((gcd(a,n))==1) & (a<=n) :
        alist.append(a)
        a=a+1
        while not ((gcd(a,n))==1):
            a=a+1

    timer=len(alist)
    while timer>=0:
        for a in alist:
            if (a**k)%n==1:
                timer=timer-1
                if timer <0:
                    break
                pass
            else:
                timer=len(alist)
                k=k+1
    return k

def generateKey():
    global e, d, n
    n = p*q
    carm = carmichael(n)
    
    e = random.randint(1, carm)
    while gcd(e, carm) != 1:
        e = random.randint(1, carm)
    #e = 17  # 1 < e < carmichael that is coprime to 780, or simpler, choose a prime for e and check that it's not a divisor of carmichael
    e=17
    d = pow(e, -1, carm)
    
    public_key = (n, e)
    private_key = (n, d)
    
def encryption(message):
    global c
    message = [ord(char) for char in message]
    c = [pow(char, e) % n for char in message]
    return c

def decryption(message):
    global m
    m = "".join([chr(pow(int(char), d) % n) for char in message])
    return m


text = "A"
generateKey()
encrypted = encryption(text)
print("Input: " + text +"\n")
print("Encrypted: ")
print(encrypted)
#print("".join([hex(char) + " " for char in encrypted]))
with open("rsa.txt", "wb") as f:
    for char in c:
        f.write(chr(char).encode("utf-8"))
#    f.write(str([chr(char) for char in c]).encode("utf-8"))

decrypted = decryption(encrypted)
print("\nDecrypted: " + decrypted)
print("N length: " + str(n.bit_length()) + " bits")