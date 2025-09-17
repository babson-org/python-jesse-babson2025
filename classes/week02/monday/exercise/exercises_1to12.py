from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
steps=['step1','step2','step3']
def make_tea(myList):
    myList[2] = "step5"
    for item in myList:
        print(item)
    

make_tea(steps)
print(steps)

# enter your code here
# 1. Fill Kettle with Water
# 2. Boil Water
# 3. Place Tea Bag in Mug
# 4. Add Boiling Water
# 5. Let Steep for 1-2 Minutes
# 6. Enjoy

def make_tea():
    steps = [ "1. Fill Kettle with Water ", 
              "2. Boil the Water ", 
              "3. Place Tea Bag in Mug ",
              "4. Add Boiling Water", 
              "5. Let steep for 1-2 Minutes",
              "6. Enjoy Tea!!"]
    for step in steps:
        print(step)
make_tea()
pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
# enter your code here
nums = [2, 4, 6, 8, 10]
for i in range(3):
    next = nums[-1] + 2 + i * 2
    print(next)

list1 = [2,4,6,8,10]
for list1 in range(12,17,2):
    print(list1)

pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
# enter your code here
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e4c919093ed6a54f625d28f1658d2c0a2c09ac34
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello,", first_name, last_name)
first_name = first_name.capitalize()
last_name = last_name.capitalize()
<<<<<<< HEAD
=======
fname = input('please enter yur first name: ')
lname = input('please enter your last name: ')
fname = fname.capitalize()
lname = lname.capitalize()
print(f'Hello, {fname} {lname}')

>>>>>>> 779d4cea6716a08a7b94a798755b96eee5b9ceb1
=======
>>>>>>> e4c919093ed6a54f625d28f1658d2c0a2c09ac34

pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here
import sys
import platform
import pprint
import sys
import platform
import pprint

#pprint.pprint(dir(sys))
print(type(sys.version))
print(sys.version, sys.platform)
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 779d4cea6716a08a7b94a798755b96eee5b9ceb1
=======
>>>>>>> e4c919093ed6a54f625d28f1658d2c0a2c09ac34
pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e4c919093ed6a54f625d28f1658d2c0a2c09ac34
txt = "Enter a #: "
while True: 
    try:
        num_1 = int(input(txt))
        break
    except ValueError:
        txt = "follow instructions"

txt = "Enter another #: "
while True: 
    try:
        num_2 = int(input(txt))
        break 
    except ValueError:
        txt = "follow Instructions"        
sum_result = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2 
if num_2 != 0:
    division = num_1 / num_2 
    floor_division = num_1 // num_2 
else:
    division = "Cannot divide by zero"
    floor_division = "Cannot divide by zero"
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
print("Floor Division:", floor_division)
      
<<<<<<< HEAD
=======
txt = 'please enter an integer: '
while True:
    try:
        x = int(input(txt))
        break
    except ValueError:
        txt = 'follow directions, enter a number: '

txt = 'please enter an integer: '
while True:
    try:
        y = int(input(txt))
        break
    except ValueError:
        txt = 'follow directions, enter a number: '

total = x + y
diff = x - y
prod = x * y
div = x / y
flr = x // y

print(total, prod, diff, div, flr)
>>>>>>> 779d4cea6716a08a7b94a798755b96eee5b9ceb1
=======
>>>>>>> e4c919093ed6a54f625d28f1658d2c0a2c09ac34
pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''
txt = input('please entr some text:')
print(txt.upper())
print(txt.lower())
print(txt.capitalize())
print(txt.split())

# enter your code here
txt = input("Please type a sentence: ")
print(txt.upper())
print(txt.lower())
print(txt.capitalize())
print(txt.split())

pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# enter your code here
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e4c919093ed6a54f625d28f1658d2c0a2c09ac34
calculation1 = 10 + 2 * 5 / 2 - 3 ** 2
print(calculation1)
calculation2 = (10 + 2) * (5 / 2) - (3 ** 2)
print(calculation2)
<<<<<<< HEAD
=======
print(10 + 2 * 5 / 2 - 3 ** 2)

x = (10 + (2 * (5 / 2)) - (3 ** 2))
>>>>>>> 779d4cea6716a08a7b94a798755b96eee5b9ceb1

print(x)
=======
>>>>>>> e4c919093ed6a54f625d28f1658d2c0a2c09ac34

x = 2**3**2
print(x)
pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e4c919093ed6a54f625d28f1658d2c0a2c09ac34
food_list = ["Eggs ", " Bagels ", "Waffles "]
food_list[1] = "Pizza"
print(str(food_list))

<<<<<<< HEAD
=======
myList =['ice cream', 'blueberries', 'cake']
myList[1] = 'candy'
print(myList)
>>>>>>> 779d4cea6716a08a7b94a798755b96eee5b9ceb1
=======
>>>>>>> e4c919093ed6a54f625d28f1658d2c0a2c09ac34
pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here
tup1 = tuple("1", "2", "3", "4")

print(tup1)
pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here
student1 = {"Jesse":21}
student1["Jesse"] = 20
print(student1)
fav_nums = [24, 15, 8, 28, 15 ]
fav_nums.append(9)
print(fav_nums)

pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here
quote = input("Enter your favorite quote: ")
with open("quotes.txt", "w") as file:
    file.write(quote)
with open("quotes.txt", "r") as file:
    saved_quote = file.read()


pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here
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
clear_screen()