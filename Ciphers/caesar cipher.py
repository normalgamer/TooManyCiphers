import os
encodedText = ""
decodedText = ""

characters  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']


def encode(s, i):
    
    s = s.lower()
    global encodedText
    encodedText = ""
    
    for char in s:
        if char in characters:
            x = characters.index(char)
            encodedText = encodedText+characters[x+i]
        
        else:
            encodedText = encodedText+char
        
    return encodedText
    

def decode(s, i):
    
    s = s.lower()
    global decodedText
    decodedText = ""
    
    for char in s:
        if char in characters:
            x = characters.index(char)
            decodedText = decodedText+characters[x-i]
        else:
            decodedText = decodedText+char
    
    return decodedText


print("Text: hi, world")
print("Encoded: " + encode("hi, world", 2))

input()

print("Decoded: " + decode(encodedText, 2))




