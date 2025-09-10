quote = input("Enter your favorite quote: ")
with open("quotes.txt", "w") as file:
    file.write(quote)
with open("quotes.txt", "r") as file:
    saved_quote = file.read()

