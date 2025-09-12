text = input("Enter some text: ")

    # TODO: Count letters
letters = 0
for char in text:
    if char.isalpha():
        letters += 1
#print(f"Letters: {letters}") check

    # TODO: Count words
words = 1
for space in text:
    if space == " ":
        words += 1
    else:
        pass
print(words)
    # TODO: Count sentences
sentences = 1
for sent in text:
        if char in ".?!":
            sentences += 1
    # TODO: Print the results
print(f"Letters: {letters}")
print(f"Words: {words}")        # replace 0
print(f"Sentences: {sentences}")    # replace 0