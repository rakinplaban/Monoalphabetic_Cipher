# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:18:13 2023

@author: Rakin Shahriar
"""

def encrypt(plain_text, key):
    plain_text = plain_text.upper()
    cipher = ''
    
    for char in plain_text:
        # to check the string contains only alphabet -> true, anything else withou alphabet->false
        if char.isalpha():
            index = ord(char) - ord('A')
            cipher_ = key[index]
            cipher += cipher_
        else:
            cipher += char
            
    return cipher


def decrypt(cipher, key):
    cipher = cipher.upper()
    plain_text = ''
    
    for char in cipher:
        if char.isalpha():
            index_ = key.index(char)
            text = chr(index_ + ord('A'))
            plain_text += text
        else:
            plain_text += char
            
    return plain_text


key = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Example usage
plain_text = "HELLO WORLD"
encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Plain text:", plain_text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)