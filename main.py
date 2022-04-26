#dictionary with alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
#logo
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

#variable to store the input to use the program
directions = input("type 'encode' or 'decode' to start: ")


#function to encode
def encrypt():
    shift = int(input("type a number to shift: "))
    message = input("type a message to encode: ")
    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                print(alphabet[(j + shift) % 26], end="")

#function to decode
def decrypt():
    shift = int(input("type a number to shift: "))
    message = input("type a message to decode: ")
    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                print(alphabet[(j - shift) % 26], end="")
#loop if error
while True:
    if directions == "encode":
        encrypt()
        break
    elif directions == "decode":
        decrypt()
        break
    else:
        print(logo)
        directions = input("type 'encode' or 'decode' to start: ")

