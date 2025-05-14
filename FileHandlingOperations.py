print("File handling program")

file = open("practice.txt","w")
file.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
file.close()

with open("practice.txt", 'r') as file:
    content = file.read()
updated_content = content.replace("Java", "Python")

with open("practice.txt", 'w') as file:
    file.write(updated_content)

with open("practice.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        if "learning" in line:
            print(True)
            print("Line Number: ",lines.index(line))
            print("Line: ",line)

def count_even(filepath):
    even_count = 0
    with open(filepath, "r") as file:
        for line in file:
            values = line.strip().split(",")
            for value in values:
                number = int(value)
                if number % 2 == 0:
                    even_count += 1
    return even_count

with open("newFile.txt", 'w') as file:
    file.write("1,2,3,4,5,6\n7,8,9,10,11,12\n13,14,15,16,17,18")
count =  count_even("newFile.txt")
print(f"The number of even numbers in newFile.txt is: {count}")