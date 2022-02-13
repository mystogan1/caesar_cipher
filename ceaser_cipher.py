from def_functions import encrypt
from def_functions import dycrypt

directions = input("Type 'encode' to encrypt, type 'decode' to dycript: \n").lower()
text = input("Type your messege:\n").lower()
shift = int(input("Type the shift number:\n"))




if directions == "encode":
    encrypt(text, shift)

elif directions == "decode":
    dycrypt(text, shift)