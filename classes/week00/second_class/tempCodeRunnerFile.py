names_list = ["Rocky", "Newell", "Burke" , "Jones" , "Rowley" ]
Length = len(names_list)
shifted_list = [None] * 5

for i, value in enumerate(names_list):
    new_index = (i - 3) % Length
    print(new_index)