
'''
# Python Basics II Exercises


## EX 1 - Data Structures

**Strings**:
   1. Write a function to count the number of vowels in a given string.
   2. Write a function that takes a string and returns the same string but with every second letter capitalized.

**List**:
   3. Write a function that takes a list of numbers and returns a new list containing only the even numbers.
   4. Write a function that takes a list and returns a new list with duplicate values removed.

**Set**:
   5. Write a function that takes two sets and returns their intersection as a new set.
   6. Write a function that takes two sets and returns their union as a new set.

**Tuple**:
   7. Write a function that takes a list of tuples and sorts them based on the second element of each tuple.
   8. Write a function that takes a tuple and returns a reversed version of that tuple.

**Dictionary**:
   9. Write a function that takes a dictionary and returns the keys and values as separate lists.
   10. Write a function that takes a dictionary and a key, and if the key exists in the dictionary, return its value. If the key does not exist, return a default value.

## EX 2 - Conditional Statements, Loops, and Functions

**Task 1:** Write a program that takes two numbers as inputs from the user and prints their sum.

**Task 2:** Write a program that takes an integer input from the user. Use a `for` loop to print all numbers from that integer down to 0.

**Task 3:** Write a program that takes an integer input from the user. Use a `while` loop to keep doubling the number until it is greater than 1000, then print the result.

**Task 4:** Write a function that takes a number as input and returns the square of the number. Use it in a program that takes an input from the user and prints the square.

**Task 5:** Write a program that takes a number as input from the user. If the number is greater than 10, print "Big number". If the number is less than or equal to 10, print "Small number".

**Task 6:** Write a function that takes two numbers as inputs and returns their product. Use this function in a program that takes two inputs from the user and prints the product.

**Task 7:** Write a program that uses a `while` loop to take a number as input from the user, subtract 5, and print the result. Continue this until the result is less than 0.

**Task 8:** Write a program that uses a `for` loop to take an integer input from the user and print the factorial of that number.

**Task 9:** Write a program that takes a number as input from the user. If the number is positive, print "Positive". If the number is negative, print "Negative". If the number is zero, print "Zero".

**Task 10:** Write a lambda function that takes two numbers as inputs and returns their division as a floating-point number. Use this function in a program that takes two inputs from the user and prints the division.

***

**P.S. ALL CODE MUST BE CLEAN, READABLE, WELL EXPLAINED, AND FOLLOWS THE PEP 8 STYLE GUIDE.**

Happy coding!!
'''


#                                                    EX 1- string - 1
def num_of_vowels(input_string:str) :

    vowels = 'aeiou'
    input_string = input_string.lower()

    return sum([1 for i in input_string if i in vowels])

# print(num_of_vowels('abdulla iiiI '))      # test string 
 
#                                                   EX 1- string -2

def capitalize_second_letter (input_string : str):
   result =''
   i =1
   for i in range(len(input_string)):
      if (i+1)%2 == 0:
            result += (input_string[i].upper())
      else:
            result += (input_string[i])
   return result
#print(capitalize_second_letter('abdulla alkhwalda'))  # test string

#                                                       EX 1 - list - 3
def even_numbers(lst):
    new_lst = [i for i in lst if i%2==0]
    return new_lst

#print(even_numbers([1,2,3,4,56,8,7]))

#                                                       EX 1 - list - 4
def remove_duplicate(data)->list: 
    '''remove any duplicate in data'''
    return list(set(data))

#print(remove_duplicate([2124,2,3,2,1,22,3,22]))
#                                                       EX 1 - sets - 5

def intersection(first:set,second:set):
    first = set(first)
    second =set(second)
    return first.intersection(second)
#                                                       EX 1 - sets - 6

def union(first:set , second:set):
    first = set(first)
    second =set(second)
    return first.union(second)
a = [1,2,3,4]
b = [3,4,5,6]
#print(intersection(a,b),'\n',union(a,b))

#                                                       EX 1 - tuple - 7
def sort_tuples_by_second_element(list_of_tuples):

  return sorted(list_of_tuples, key=lambda item: item[1])

#print(sort_tuples_by_second_element([(12,22),(1,2),(9,99)]))
#                                                       EX 1 - tuple - 8
def reverse_tuple(input_tuple):
  return tuple(reversed(input_tuple))
#print(reverse_tuple((12,22,34,34,88,110)))

#                                                       EX 1 - dict - 9

def split_keys_values(dec : dict)->list:
    
    keys = list(dec.keys()) ; values = list(dec.values())
    return keys, values

#                                                       EX 1 - dict - 10
def detect(dic : dict, key)->any:
    
    return dic[key] if key in dic.keys() else None

#####################################    EX 2    ###########################################3

#                                               Task 1
num1 =float(input('enter first Number : '))
num2 = float(input('Enter secont NYmber : '))
print('the sum of tow number : ', (num1+num2))

#                                                task 2

num1 = int(input('enter any integer  Number : '))
for i in range(num1,-1,-1):
   print(i)

#                                                 Task 3
user_input = int(input("Enter an integer Number : "))

while True:
    
   if 1000 <= user_input:
      break
   user_input *= 2
print(user_input)

#                                               task 4
def squer(num):
    return num**2
number = int(input('enter an integer number : '))
print('the squer number of ',number,' = ',squer(number))

#                                                       task 5
num = int(input("Enter a number: "))

if num > 10:
  print("Big number")
else:
  print("Small number")
 
#                                                        TAsk 6
num1 =float(input('enter first Number : '))
num2 = float(input('Enter secont NYmber : '))
def product(num1,num2):
    return (num1*num2)

print(f'the product of {num1} * {num2} = {product(num1,num2)}')

#                                                                          task 7

num = int(input("Enter a number: "))
while num > 0:
    num -= 5
    print(f'{num+5} - 5  = {num}')

#                                                           Task 8
def factorial(n):
  if n < 0:
    return "Factorial is not defined for negative numbers."
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

n = int(input('Enter the inger number : '))
print(f'the factorial {n} is {factorial(n)}')

#                                                                  tsak 9

num_task9 = float(input("Enter a number is positive, negative or zero??? : "))
if num_task9 > 0:
  print("Positive")
elif num_task9 < 0:
  print("Negative")
else:
  print("Zero")


#                                                                 tsak 10

divide_numbers = lambda x, y: (x/y)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number : "))

print(f'the divide {num1} and {num2}  =  {divide_numbers(num1,num2)}') if num2 != 0 else print('Error')

