# Write a Python program to calculate the commission based on sales amount
print("Welcome to Commission Calculator")

sales = int(input("Enter sales amount: "))
comm = 0
commPercent = ""

if sales >= 50000:
    comm = (sales * 10)/100
    commPercent = "10%"
elif sales >= 30000:
    comm = (sales * 7)/100
    commPercent = "7%"
elif sales >= 20000:
    comm = (sales * 5)/100
    commPercent = "5%"
else:
    comm = 0

if comm != 0:
    print("Commission percent is : ", commPercent, "\nActual Commission is: ", comm)
else:
    print("No Commission")