import os


characters          = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                       'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
                       '7', '8', '9']
morseChars          = ['.-', '-...', '-.-.',  '-..', '.', '..-.', '--.',
                       '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
                       '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
                       '-..-', '-.--', '--..', '-----', '.----', '..---',
                       '...--', '....-', '.....', '-....', '--...', '---..',
                       '----.']
specialCharacters   = [' ', '.', ',', '?', '\'', '!', '/', '(', ')', '&', ':',
                       ';', '=', '+', '-', '_', '"', '$', '@']
specialMorse        = ['/', '.-.-.-', '--..--', '..--..', '.----.', '-.-.--',
                       '-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.',
                       '-...-', '.-.-.', '-....-', '..--.-', '.-..-.',
                       '...-..-', '.--.-.']


def encodeMorse(inputText):
    outputText = ""
    inputText = inputText.lower()

    for char in inputText:
        if char in specialCharacters:
            x = specialCharacters.index(char)
            outputText = outputText + specialMorse[x] + " "

        elif char in characters:
            x = characters.index(char)
            outputText = outputText + morseChars[x] + " "
        else:
            pass

    return outputText


def decodeMorse(inputText):
    outputText = ""

    words = inputText.split('   ')

    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in specialMorse:
                x = specialMorse.index(char)
                outputText = outputText + specialCharacters[x]

            elif char in morseChars:
                x = morseChars.index(char)
                outputText = outputText + characters[x]
            else:
                pass
        outputText = outputText + " "

    return outputText


message = "The quick brown fox jumps over the lazy dog"

encrypted = encodeMorse(message)
print(encrypted)

decrypted = decodeMorse(encrypted)
print(decrypted)
