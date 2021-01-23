# Vigenère cipher

The Vigenère cipher is a method of encrypting text by using a series of
intervowen [Caesar ciphers](caesar.md), based on the letters of a keyword. It
employs a form of polyalphabetic substitution.

## How does it work

In a Caesar cipher, each letter of the alphabet is shifted along some number of
places. The Vigenère cipher has several Caesar ciphers in sequence with
different shift values.

For example, let the plaintext be
```
quickbrownfox
```

The person sending the message chooses a keyword and repeats it until it
matches the length of the plaintext. If the keyword is "lazy"
```
lazylazylazyl
```
For encryption and decryption, a table of alphabets can be used, also known as
[_tabula recta_](https://en.wikipedia.org/wiki/Tabula_recta), _Vigenère square_
or _Vigenère table_. It has the alphabet written out 26 times in different
rows, each alphabet shifted to the left compared to the previous one,
corresponding to the 26 possible Caesar ciphers.

![Vigenère table](https://upload.wikimedia.org/wikipedia/commons/9/9a/Vigen%C3%A8re_square_shading.svg)

Each row starts with a key letter. The rest of the row holds the letters A to Z
in shifted order.

For example, the first letter of the plaintext, `Q`, is paired with `L`, the
first letter of the key. Therefore, row `Q` and column `L` of the Vigenère
square are used, which corresponds to `B`. The process is repeated for all the
letters in the plaintext: row `U` and column `A` yields `U`, row `I` and column
`Z` yields `J`...
```
quickbrownfox
buhavbqmhnemi
```
Decryption is performed by going to the row in the table corresponding to the
key, finding the position of the ciphertext letter in that row and then using
the column's label as the plaintext. For example, in row `L` (from lazy), the
ciphertext b appears in column `Q`, which is the first plaintext letter.
