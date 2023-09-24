plainText = input("What is your plaintext? ")
shift = int(input("What is your shift? "))

def caesar(plainText, shift): 
    cipherText = ""  # Initialize the ciphertext

    for char in plainText:
        if char.isalpha():
            stayInAlphabet = ord(char) + shift 
            if char.islower():
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
                elif stayInAlphabet < ord('a'):
                    stayInAlphabet += 26
            elif char.isupper():
                if stayInAlphabet > ord('Z'):
                    stayInAlphabet -= 26
                elif stayInAlphabet < ord('A'):
                    stayInAlphabet += 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter  # Append each letter to the ciphertext
        else:
            cipherText += char  # Preserve non-alphabetic characters

    print("Your ciphertext is:", cipherText)

    return cipherText

caesar(plainText, shift)
