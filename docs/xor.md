# XOR Encryption

XOR encryption uses XOR gates to encrypt data.

## What is a XOR gate

XOR or eXclusive OR is a logical operation that outputs true only when inputs
differ (one is true, the other is false).
```
  0 xor 0 = 0
  0 xor 1 = 1
  1 xor 0 = 1
  1 xor 1 = 0
```

## Functioning
Let's encrypt the word "fox". If we convert fox into each characters'
unicode number and then to binary, we get
```
01100110 01101111 01111000
```

If we use the key 00101100 to encrypt the message, we get
```
01100110 01101111 01111000
00101100 00101100 00101100
--------------------------
01001010 01000011 01010100
```

We can use the same key to decrypt the message
```
01001010 01000011 01010100
00101100 00101100 00101100
--------------------------
01100111 01101111 01111000
```

At last, if we xor the plaintext with the ciphertext, we get the key
```
01100110 01101111 01111000
01001010 01000011 01010100
--------------------------
00101100 00101100 00111100
```

## One-Time Pad (OTP)
If we want a XOR key to be teorically uncrackable unless brute-forced, we can
use a one-time pad. In this technique, the key (otp) is a unique key as long as
or longer than the plaintext.

In order to be unbreakable four conditions should be met:

- The key must be truly random

- The key must be at least as long as the plaintext

- The key must never be reused in whole or in part

- The key must be completely secret

If you want to use an OTP, use `os.urandom(len(plaintext))` to generate a key as
long as the plaintext of random bytes suitable for cryptographic use. The main
problem of the One-Time Pad is key distribution
