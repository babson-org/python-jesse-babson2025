from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
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
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello,", first_name, last_name)


pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here
num_1 = input("Enter a #: ")
num_2 = input('Enter another #: ')
print(int(num_1 + num_2, num_1 - num_2, num_1 * num_2, num_1 / num_2, num_1 % num_2))
      
pauce=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''

# enter your code here


pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here


pause=input('pause')
clear_screen()