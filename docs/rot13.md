# ROT13 cipher

ROT13 (ROTate by 13 places) is a simple letter substitution cipher that
replaces a letter with the 13th letter after it in the alphabet. It's basically
a Caesar cipher with a fixed key.

## How does it work

Ciphering can be done using a lookup table, such as the following:
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
NOPQRSTUVWXYZABCDEFGHIJKLM
```
Since there are 26 letters in the english alphabet (2 x 13), the ROT13 function
is its own reverse. For example,
```
The quick brown fox
Gur dhpvx oebja sbk
```
