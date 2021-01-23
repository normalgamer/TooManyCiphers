# Kid RSA encryption

Kid RSA is an encryption algorithm published in 1997, designed for educational
purposes. It's a simplified version which uses modular multiplication to
simplify the calculation progress; the trade-off is that the algorithm becomes
susceptible to a well-known mathematical attack.

## Key generation

The user chooses four positive integers _a, b, a', b'_

```
  M = ab - 1
  e = a'M + a
  d = b'M + b
  n = (ed - 1)/M = a'b'M + ab' + a'b + 1
```

The public key is _(n, e)_, the private one is _(n, d)_.

## Encryption

As with RSA, encryption and decryption is very simple. If m is an integer
representing a character of a plaintext message, then the encrypted integer is
```
  c = (me) mod n
```

## Decryption

As with RSA, decryption is very similar to encryption
```
  m = (cd) mod n
```

## Example

Let `a = 9`, `b = 11`, `a' = 5`, `b' = 8`, thus
```
  M = (9 x 11) - 1 = 98
  e = (5 x 98) + 9 = 499
  d = (8 x 98) + 11 = 795
  n = ((499 x 795) - 1) / 98 = 4048
```

If we want to encrypt character "A" (unicode 65)
```
  c = (65 x 499) mod 4048 = 51
```
To decrypt it
```
  m = (51 x 795) mod 4048 = 65
```

## Breaking Kid RSA

For more info about Kid RSA and how to break it, visit
[this page](http://math.uttyler.edu/sjgraves/aam/sec-PublicKey-KidRSA.html)
