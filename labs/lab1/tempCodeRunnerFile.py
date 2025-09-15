def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """
    # TODO: Get user input text
text = input("Enter text: ")

    # TODO: Get shift value
shift = int(input("Enter shift value (integer): ")) % 26

    # TODO: Ask user whether to encrypt or decrypt
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic
if choice == 'd':
        shift = -shift

result = ""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for char in text:
    if char.islower():
        result += alphabet[(alphabet.index(char) + shift) % 26]
    elif char.isupper():
        result += alphabet[(alphabet.index(char.lower()) + shift) % 26].upper()
    else:
        result += char 
    # TODO: Print the final result
print("Result:", result)