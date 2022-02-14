from variables import *

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to dycript: \n").lower()
text = input("Type your messege:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
            shift_amount *= -1
    
    for letter in start_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        if new_position > 26:
            new_position = new_position%26
        end_text += alphabets[new_position]
    print(f"The {direction}d text is {end_text}:\n")

ceaser(text, shift, direction)



