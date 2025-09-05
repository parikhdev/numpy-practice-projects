class Employee:
    def __init__(self, Role, Department, Salary):
        self.Role = Role
        self.Department = Department
        self.Salary = Salary

    def show_details(self):
        print("Role is:", self.Role)
        print("Department is:", self.Department)
        print("Salary is:", self.Salary)

class Engineer(Employee):
        def __init__(self, name, age):
            self.name = name
            self.age = age
            super().__init__("Engineer", "IT", "90,000")
        
        def show_details(self):
            print(f"The name is {self.name}")
            print(f"The age is {self.age}")
            super().show_details()


# Employee1 = Employee("Accountant", "Finance", "75,000")
# Employee1.show_details()

Eng1 = Engineer("Yash", 22)
Eng1.show_details()
    




