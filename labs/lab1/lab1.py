"""
Lab 1 – Python Basics
Author: Jesse Buchanan
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    # TODO: Prompt user for an odd number
    try:
        height = int(input("Enter an odd number for the height: "))

        # I ADDED PROTECTION TO NOT BREAK INPUT (WE ONLY WANT + ODD #)
    except ValueError:
        print("Please enter an odd number")
        return
    if height <= 0 or height % 2 == 0:
        print("Error: Please enter a positive odd number.")
        return
    
    middle = height // 2 

# TODO: Draw the top half of the diamond

    for i in range(middle, -1, -1):          # USED A FOR LOOP TO DETERMINE NUMBER OF SPACES AND IF THERE IS NO SPACE TO PUT A *
        before = " " * i                     # ADDS SPACE BEFORE THE STAR
        between_num = ((middle - i)) * 2-1   # MIDDLE - i GROWS AS >i, THEN 2 - 1 GIVES UP CORRECT PATTERN
        between = " " * between_num          # (ACTUAL SPACES)
    
        if between_num == -1:                    # SAME LOGIC TRICK AS LINE 3
            print(before + "*")
    
        else:
            print(before + "*" + between + "*")

# TODO: Draw the bottom half of the diamond
    for i in range(1, middle +1):                   # SAME LOGIC AS ABOVE (DIFFERENT RANGE FOR BOTTOM)
        before = " " * i
        between_num = ((middle - i)) * 2-1
        between = " " * between_num
    
        if between_num == -1:
            print(before + "*")
    
        else:
            print(before + "*" + between + "*")
# Uncomment to test Part 1
#draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """
    # TODO: Get user input
    text = input("Enter some text: ")

    # TODO: Count letters
    letters = 0

    for char in text:               # USE CHAR TO GO THROUGH INPUT 1 LETTER AT A TIME
        if char.isalpha():          # .isalpha() TO DETERMINE IF THE CHARACTER IS A LETTER
            letters += 1            

    # TODO: Count words
    words = 1                       # COUNTS WORDS BY ADDING SPACES, STARTS AT SPACE "1"

    for space in text:
    
        if space == " ":
            words += 1              # ADDs A SPACE TO ACCOUNT FOR LAST WORD OF SENTENCE
    
        else:
            pass

    # TODO: Count sentences

    sentences = 0                  # Set sentences to count (start at zero)

    for char in text:              # Counts sentences by looking for the characters ". ? !"
        if char in ".?!":
            sentences += 1
    # TODO: Print the results

    print(f"Letters: {letters}")
    print(f"Words: {words}")        
    print(f"Sentences: {sentences}")    

# Uncomment to test Part 2
# text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
#def caesar_cipher(): 
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """
    # TODO: Get user input text
    # ***Below
    # text = input("Enter text: ")
    # TODO: Get shift value
    # shift = int(input("Enter shift value (integer between (1-25)): ")) % 26
'''


'''
#I had to add caesar_cipher() and text in order to not get "indent error"
def caesar_cipher(): 
    text = input("Enter text: ")
    shift = int(input("Enter shift value (integer between (1-25)): ")) % 26
              # MODULUS THE # OF LETTERS IN ALPHABET

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

# Uncomment to test Part 3
#caesar_cipher()


# ==============================
# Main Program
# ==============================
def main():
    print("Lab 1 - Python Basics")
    print("1. Draw Diamond")
    print("2. Text Analysis")
    print("3. Caesar Cipher")
    choice = input("Select part to run (1-3): ")
    
    if choice == "1":
        draw_diamond()
    elif choice == "2":
        text_analysis()
    elif choice == "3":
        caesar_cipher()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
