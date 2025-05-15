class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print(f"Hi {self.name}, your average score is {(sum/3)}")

s1 = Student("Ataur Khan", [89, 94, 70])
s1.get_average()

s1.name = "John Wick"
s1.marks = [90, 70, 80]
s1.get_average()

s1.name = input("Enter name: ")
s1.marks = [int(x) for x in input("Enter marks: ").split(",")]
s1.get_average()