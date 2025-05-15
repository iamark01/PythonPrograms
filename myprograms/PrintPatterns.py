n = int(input("Enter the value of n: "))

print("Number Patterns") 
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("Star Patterns")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

print("Number Pattern - 2")
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
    num += 1
    print()

print("Number Pattern - 3")
b = 0
for i in range(n, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=" ")
    print()

print("Number Pattern - 4")
rows = 7
for i in range(rows, 1, -1):
    for j in range(1, i-1, 1):
        print(rows - j, end=" ")
    print()

print("Number Pattern - 5")
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    
print("Number Pattern - 6")
rows = 10
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()
    
print("Star Pattern - 2")
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print()