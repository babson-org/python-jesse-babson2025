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
        words += 1              # ADD A SPACE TO ACCOUNT FOR LAST WORD OF SENTENCE
    
    else:
        pass

    # TODO: Count sentences

sentences = 0                  # Set sentences to count first 

for char in text:                   
    if char in ".?!":
        sentences += 1
    # TODO: Print the results

print(f"Letters: {letters}")
print(f"Words: {words}")        
print(f"Sentences: {sentences}")    