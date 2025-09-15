text = input("Enter text: ")

    # TODO: Get shift value
shift = int(input("Enter shift value (integer): ")) % 26          # MODULUS THE # OF LETTERS IN ALPHABET

    # TODO: Ask user whether to encrypt or decrypt
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic
if choice == 'd':                                               # DETERMINES FORWARD OR REVERSE SHIFT
        shift = -shift

result = ""                 
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for char in text:
    if char.islower():
        result += alphabet[(alphabet.index(char) + shift) % 26]           # USE MODULUS 26 FOR THE NUMBER OF LETTERS IN ALPHABET
    elif char.isupper():                                                   # USING .upper and .lower TO ACCOUNT CAPITALIZATION
        result += alphabet[(alphabet.index(char.lower()) + shift) % 26].upper()
    else:
        result += char 
    # TODO: Print the final result
print("Result:", result)