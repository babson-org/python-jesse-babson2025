num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
num_list = [num1, num2, num3, num4, num5]
sum_numlist = sum(num_list)
average = sum(num_list) / len(num_list)
print("Sum ", sum_numlist)
print("Average ", average)

pause=input('pause')