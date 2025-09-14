text = input("Enter text: ")

    # TODO: Get shift value
shift = int(input("Enter shift value (integer): "))

    # TODO: Ask user whether to encrypt or decrypt
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic
if choice == 'd':
        shift = -shift

result = ""

for char in text:
    if char.isalpha():
        
        if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        
        else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
    
    else:
            result += char

    # TODO: Print the final result
print("Result:", result)