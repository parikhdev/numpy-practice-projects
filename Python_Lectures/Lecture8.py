"""
Create student class that takes names and marks of 3 subjects as Arguments in Constructor.
Then Create a method to print the Average.  
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def Average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "Your Average is", sum / len(self.marks))

s1 = Student("Alice", [93, 99, 97, 91])
s1.Average()

s2 = Student("Bob", [85, 87, 90, 92])
s2.Average()

s3 = Student("Charlie", [78, 82, 80, 76])
s3.Average()
