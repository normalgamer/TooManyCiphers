# Caesar cipher

The caesar cipher is probably one of the best known and simplest encryption
algorithms. It's a type of substitution cipher in which each letter in the
plaintext is substituted by a letter some fixed number of positions down the
alphabet. The cipher is named after Julius Caesar, who used it in his private
correspondence.

## Example

Let's encrypt the phrase "The quick brown fox jumps over the lazy dog" using a
shift parameter of +2
```
The quick brown fox jumps over the lazy dog
Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi
```

Deciphering is done in reverse, with a right shift of 2
```
Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi
The quick brown fox jumps over the lazy dog
```

## Modern applications
The caesar cipher is sometimes used as part of more complex schemes, such as
the [Vigenère cipher](vigenére.md), but nowadays it's easily broken, either by
bruteforcing or by using [frequency analysis]
(https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher).
