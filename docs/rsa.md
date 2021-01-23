# RSA Explanation

## What is RSA?

RSA (Rivest-Shamir-Adleman) is a public-key cryptosystem. Public-key means that
two different keys are used: one for encryption (the public key) and one for
decryption (the private key). The security of RSA relies on the difficulty of
factoring the product of two large prime numbers. RSA is a relatively slow
algorithm, thus it's usually used to encrypt symmetric keys, which are used on
faster symmetric encryption algorithms.

## Functioning

The RSA algorithm involves four steps: key generation, distribution, encryption
and decryption.

## Key Generation

The keys are generated in the following way:

- Choose two distinct prime numbers, _p_ and _q_.
  - For security reasons, _p_ and _q_ should be chosen at random and should be
    similar in magnitude but differ in length by a few digits to make factoring
    harder.
  - _p_ and _q_ are kept secret.

- Compute _n = pq_
  - _n_ is used as the modulus for both the public and private keys. It's
    length, usually expressed in bits, is the key length.
  - _n_ is released as part of the public key.

- Compute _λ(n)_, which is Carmichael's totient function. Alternatively, the
  Euler totient function _φ(n) = (p − 1)(q − 1)_ can be used.
  - _λ(n)_ or _φ(n)_ are kept secret.
  - _φ(n)_ is used in the script because of it's speed.

- Choose an integer _e_ such that _1 < e < φ(n)_ and _gcd(e, φ(n)) = 1_, that
  is, _e and φ(n)_ are coprime.
  - _e_ having a short bit-length and small Hamming weigth results in more
    efficient encryption - the most commonly chosen value is
    _e = 2^16 + 1 = 65,537_.
  - _e_ is released as part of the public key.

- Determine _d_ as _d ≡ e−1 (mod φ(n))_, that is, _d_ is the modular
  multiplicative inverse of _e mod(φ(n))_.
  - _d_ is kept secret as the private key exponent.

The public key consists of the modulus _n_ and the public (or encryption)
exponent _e_. The private key consists of the private (or decryption) exponent
_d_. _p, q_ and _φ(n)_ should be discarded after generating the key since they
can be used to calculate _d_.

## Key distribution
If Bob wants to send a message to Alice, Bob needs to know Alice's public key.
Alice sends his public key _(n, e)_ to Bob via a reliable, but not necessarily
secret, route.

## Encryption
After Bob receives Alice's public key, he can send a message _M_ to Alice. To
do it, he first turns _M_ into an integer _m_, such that 0 ≤ m < n by using an
agreed-upon reversible protocol known as a padding scheme (not implemented in
the script). He then computes the ciphertext _c_, using Alice's public key _e_,
corresponding to

`m^e ≡ c (mod n)`

## Decryption
Alice can recover _m_ from _c_ by using her private key exponent _d_ by
computing

`c^d ≡ m (mod n)`

## Example

This is an example of RSA encryption and decryption. The prime numbers used are
very small, usually the length of _p_ and _q_ are of 1024 bits, with _n_ having
a length of 2048 bits. In this example, _p_ and _q_ have a length of 6 bits,
and _n_ has a length of 12 bits.

- Choose two prime numbers, such as

  _p = 61_ and _q = 53_

- Compute _n = pq_ giving

  _n = 61 x 53 = 3233_

- Compute the Euler's totient function (or Carmichael's)

  _φ(3233) = (p - 1) x (q - 1) = 3120_

- Choose any number _1 < e < 3120_ that is coprime to 3120. Choosing a prime
  number for e leaves us only to check that _e_ is not a divisor of 3120
  (gcd(e, 3120) = 1)

  Let _e = 1127_

- Compute _d_, the modular multiplicative inverse of _e (mod φ(n))_

  In python, you can use `pow(e, -1, φ(n))`, which yields 263

The public key is _(n = 3233, e = 1127)_. To encrypt _M = A_
_(m = unicode("A") = 65)_, the encryption function is
```
  c(m) = m^e mod n
  c(65) = 65^1127 mod 3233 = 2424
```
The private key is _(n = 3233, d = 263)_. To decrypt the encrypted letter A
(2790), the procedure is
```
  m\(c\) = c^d mod n
  m(2790) = 2424^263 mod 3233 = 65
```
## Signing messages
Suppose Alice uses Bob's public key to send him an encrypted message. In the
message she claims to be Alice, but Bob has no way of verifying that the message
was from Alice, since anyone can use Bob's key to send him encrypted messages.
In order to verify the origin of a message, RSA can be used to sign a message.

Suppose Alice wants to send a signed message to Bob. She can use her private key
to do so. She produces a hash value of the message, converts it to an integer
and rises it to the power of _d (modulo n)_, as she does when decrypting a
message, and attaches the signature to the encrypted message. When Bob receives
the message, he raises the signature to the power of _e (modulo n)_ as he does
when encrypting a message, _e_ being Alice's public key. He then decrypts
Alice's message using his private key, uses the same hashing algorithm on the
decrypted message and compares it to the signature's hash.
