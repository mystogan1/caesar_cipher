alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

direction = input("Type 'encode' to encrypt, type 'decode' to dycript: \n").lower()
text = input("Type your messege:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabets.index(letter)
        if cipher_direction == "decode":
            shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabets[new_position]
    print(f"The {direction}d text is {end_text}:\n")

ceaser(text, shift, direction)



