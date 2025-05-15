print("Program to display the usage of Set data types")

# Write a program to find max and min in a set.
number_set = {1, 3, 5, 7, 9, 11}

print("Maximum number in set is :", max(number_set))
print("Minimum number in set is :", min(number_set))

# Write a program to find common elements in three lists using sets.
list_a = [1, 2, 3, 4]
list_b = [4, 5, 6, 7]
list_c = [1, 3, 5, 7]

result1 = set(list_a).intersection(list_b)
result2 = set(list_b).intersection(list_c)
result3 = set(list_a).intersection(list_c)

print("Common elements between three lists:",result1, result2, result3)

# Write a program to find different between two sets.
set_a =  {"Ironman","Hulk","Thor","Captain America"}
set_b = {"Superman","Hawkeye", "Hulk", "Thor"}

print(set_a.difference(set_b))

# Write a Python program to remove an item from a set if it is present in the set.
set_a =  {"Ironman","Hulk","Thor","Captain America"}
print("Before removing: ",set_a)
if "Thor" in set_a:
    set_a.remove("Thor")
print("After removing: ",set_a)

# Write a Python program to check if a set is a subset of another set.
set_a =  {"Ironman","Hulk","Thor","Captain America"}
set_b = {"Hulk", "Thor"}

print("Checking if set_a is a subset of set_b:",set_a.issubset(set_b))
print("Checking if set_b is a subset of set_a:",set_b.issubset(set_a))
