print("Welcome to Percentage Calculator")

eng = int(input("Enter marks for English: "))
maths = int(input("Enter marks for Mathematics: "))
hindi = int(input("Enter marks for Hindi: "))
marathi = int(input("Enter marks for Marathi: "))
sci = int(input("Enter marks for Science: "))

result = eng + maths + hindi + marathi + sci

percentage = result / 5

print("Percentage obtained is: ", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >=60:
    print("Grade D")
else:
    print("Grade F")