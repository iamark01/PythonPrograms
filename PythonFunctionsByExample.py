print("Program to demonstrate usage of functions in Python")

# Write a function to find maximum of three numbers in Python

def find_maximum(num1, num2, num3):
    '''This function takes 3 variables as input and returns the maximum number from them'''
    return max(num1, num2, num3)

print("Maximum number from (10, 20, 2) is:",find_maximum(10, 20, 2))

# Write a Python Function to create  and print a list where the values are square of numbers between 1 and 30.

def create_list():
    mylist = []
    for i in range(1, 30):
        mylist.insert(i, i ** 2)
    return mylist

print("List generated with square of numbers between 1 and 30 is:",create_list())

# Write a Python function that takes a number as a parameter and check if the number is prime or not.

def is_prime_num(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if (num % i == 0):
                return False            
        return True

number = int(input("Enter a number to check if it is prime or not: ")) # 3

if is_prime_num(number):
    print(f"{number} is Prime Number")
else:
    print(f"{number} is not a Prime Number")

# Write a Python function to sum all the numbers in a list.

def list_sum(mylist):
    return sum(mylist)

list_a = [1, 3, 5, 7, 9, 11]
print("Sum of all numbers in list is: ",list_sum(list_a))

# Write a Python program to solve the Fibonacci Sequence using Recursion.

def fib(num):
    if num <= 1:
        return num
    else:
        return (fib(num-1) + fib(num-2))
    
number = int(input("Enter a number for Fibonacci sequence: "))# 10

if number <= 0:
    print("Enter a positive whole number")
else:
    print("Printing Fibonacci Sequence")
    for i in range(number):
        print(fib(i), end=" ")