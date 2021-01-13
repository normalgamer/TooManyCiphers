import os

text        = "Hello World! Eooo"
outputText  = ""

characters          = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
morseChars          = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
specialCharacters   = [' ','.',',','?','\'','!','/','(',')','&',':',';','=','+','-','_','"','$','@']
specialMorse        = ['/','.-.-.-','--..--','..--..','.----.','-.-.--','-..-.','-.--.','-.--.-','.-...','---...','-.-.-.','-...-','.-.-.','-....-','..--.-','.-..-.','...-..-','.--.-.']

def toMorse(inputText):

    global outputText
    inputText = inputText.lower()
    
    for char in inputText:
        if char in specialCharacters:
            x = specialCharacters.index(char)
            outputText=outputText+specialMorse[x]+" "
            
        elif char in characters:
            x = characters.index(char)
            outputText=outputText+morseChars[x]+" "
        else:
            pass
        

def decode(inputText):
    global outputText
    
    words = inputText.split('   ')
    
    for word in words:
        l = word.split(' ')
        for char in l:
            if char in specialMorse:
                x = specialMorse.index(char)
                outputText=outputText+specialCharacters[x]
            
            elif char in morseChars:
                x = morseChars.index(char)
                outputText=outputText+characters[x]
            else:
                pass
        outputText = outputText+" "



print("*** MORSE ENCODER/DECODER ***")
toMorse(text)

print(outputText)

input()

morseText = outputText
outputText = ""

decode(morseText)
print(outputText)

input()