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