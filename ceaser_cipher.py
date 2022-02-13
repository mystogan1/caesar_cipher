from posixpath import split


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

directions = input("Type 'encode' to encrypt, type 'decode' to dycript: \n").lower()
text = input("Type your messege:\n").lower()
shift = int(input("Type the shift number:\n"))
# TODO-1: create a function called "encrypt".

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position+shift_amount
        if new_position >= 26:
            new_position = 26 - new_position
        encrypted_letter = alphabets[new_position]
        cipher_text += encrypted_letter
    print(f"The encoded text is {cipher_text}.")

# TODO-2: create a function called "dycript".

def dycrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabets.index(letter)
        new_position = position-shift_amount
        if new_position >= 26:
            new_position = 26 - new_position
        dycrypted_letter = alphabets[new_position]
        plain_text += dycrypted_letter
    print(f"The decoded text is {plain_text}.")

if directions == "encode":
    encrypt(text, shift)

elif directions == "decode":
    dycrypt(text, shift)
