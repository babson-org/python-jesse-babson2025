
from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
# enter code here
num = int(input("please enter a number: "))
if num == 0: 
    print('zero')
elif num > 0:
    print('positive')
else:
    print('negative')


pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
# enter code here
num = int(input("please enter a number: "))
if num % 2 == 0 :
    print("Even")
elif num == 0:
    print("Neutral")
else:
    print("Odd")


pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
# enter code here
num1 = int(input("please enter a number: "))
num2 = int(input("please enter another number: "))
if num1 > 0 and num2 > 0: 
    print("both positive")
elif num1 < 0 and num2 > 0:
    print("second number positive")
elif num1 > 0 and num2 < 0:
    print("First number positive")
elif num1 == 0 or num2 == 0:
    print("Neutral")



pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
# enter code here
for i in range(1,20):
    if i % 3 == 0:
        print(i)


pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
# enter code here



pause=input('pause')
clear_screen()

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
# enter code here
n = 0 
while n < 10:
    n = n + 1 
    if n == 3:
        continue
    if n == 8:
        break
    print(n)


pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
# enter code here
def square():
    print(int(x^2))
x = int(input("Please enter a number: "))    
square(x)


pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
# enter code here
def add_item(1st,item):
    

    


pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
# enter code here



pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
# enter code here
name1 = str(input("please enter a name: "))
name2 = str(input("please enter another name: "))
name3 = str(input("please enter another name: "))
name4 = str(input("please enter another name: "))
name5 = str(input("please enter another name: "))
names = [name1, name2, name3, name4, name5]
names = [(name.title()), for name in names]
names = sorted(names)
print(names)

##Chatgpt ansmwer
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
clear_screen()

