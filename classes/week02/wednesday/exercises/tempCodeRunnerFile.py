# Ask the user to enter 5 names and store them in a list
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

# Capitalize each name
names = [name.title() for name in names]

# Sort the list alphabetically
names.sort()

# Print the sorted, capitalized list
print("Sorted names:", names)



pause=input('pause')