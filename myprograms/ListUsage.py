print("Day 5 - List and usage")
# Write a program to separate the following string into coma (,)  separated values.
a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
b = a.split(".")
print(b)

# Write a program to sort strings alphabetically in python.
a = input("Enter any thing here to verify sorting: ")
b = sorted(a)
print(b)

# Write a program to remove a given character from string.
a = "hello"
b = a.replace("e","")
print(b)

# Write a program to remove dot (.) from the following string.
z = "F.R.I.E.N.D.S."
b=z.replace(".","")
print(b)

# Write a program to check the number of occurrence of sea.
a = "she sells seashells on the sea shore"
b=a.count("sea")
print("The number of times substring sea is occurring is",b)

# Take an input from a user as a string then, reverse it.
a= input("Enter anything here to get it reversed: ")
print(a[::-1])

# Write a program to check if a string contains only digits.
a= input("Enter anything here to check contains only digits: ")
b=(a.isdigit())
if b==True:
    print("It contains only digits")
else:
    print("It does not contain only digits")

# Write a program to check if a string is palindrome.
a= input("Enter anything here to check Palindrome: ")
rev = a[::-1]
if a == rev:
    print("It is palindrome")
else:
    print("It is not palindrome")

# Write a program to find the number of vowels in a string.
a = input("Enter anything here to count vowels: ")
vowels = 0
for i in a:
    if i=="a" or i=="A" or i=="e" or i =="E" or i== "i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U" :
        vowels += 1
print("Number of vowels used is: ",vowels)