myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']

length = len(myList)
shifted_list = [] 
shift = 3
for idx in range(length - shift, length - shift + length):
    old_idx = idx % length    
    shifted_list.append(myList[old_idx])
print(shifted_list)
