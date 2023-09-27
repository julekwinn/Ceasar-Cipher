# Szyfr Cezara 27.09.2023r.

from colorama import Fore, Back, Style, init

# Inicjalizacja colorama
init()

# Obrazek ASCII
ascii_art = r'''
  ____                                  ____  _         _                 
 / ___| __ _   ___  ___   __ _  _ __   / ___|(_) _ __  | |__    ___  _ __ 
| |    / _` | / _ \/ __| / _` || '__| | |    | || '_ \ | '_ \  / _ \| '__|
| |___| (_| ||  __/\__ \| (_| || |    | |___ | || |_) || | | ||  __/| |   
 \____|\__,_| \___||___/ \__,_||_|     \____||_|| .__/ |_| |_| \___||_|   
                                                |_|                        
'''

# Funkcja do wyświetlania kolorowego obrazka ASCII
def display_colored_ascii(ascii_art):
    colored_ascii = ""
    for line in ascii_art.split('\n'):
        for char in line:
            if char.isalnum():
                colored_ascii += Fore.RED + char + Fore.RESET
            else:
                colored_ascii += char
        colored_ascii += '\n'
    print(colored_ascii)

# Wyświetlanie kolorowego obrazka ASCII
display_colored_ascii(ascii_art)

alphabet = ['clea','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encrypted text is: {cipher_text}")

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encrypted text is: {cipher_text}")



def Caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text = end_text + alphabet[new_position]
    print(end_text)

Caesar(text,shift,direction)