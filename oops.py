class Student:
    def __init__(self, name, grade, gender):
        self.name = name
        self.grade = grade
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Gender: {self.gender}")
        print("-" * 30)

# Create an object
Student1 = Student("Arjun", "E", "M")
Student2 = Student("Anjana", "A", "F")
Student3 = Student("Albin", "A", "M")
Student4 = Student("Alphons", "S", "M")
Student5 = Student("Athulya", "B", "F")

# Storing in a list for easy handling
Students = [Student1, Student2, Student3, Student4, Student5]

# Displaying all consumer data
for Student in Students:
    Student.display()

class Consumer:
    def __init__(self, name, gender, income):
        self.name = name
        self.gender = gender
        self.income = income

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Gender : {self.gender}")
        print(f"Income : ₹{self.income:,.2f}")
        print("-" * 30)


# Creating 5 consumer objects
consumer1 = Consumer("Arjun Ajith", "Male", 750000)
consumer2 = Consumer("Meera Nair", "Female", 560000)
consumer3 = Consumer("Rahul Menon", "Male", 920000)
consumer4 = Consumer("Anjali Das", "Female", 430000)
consumer5 = Consumer("Vikram Pillai", "Male", 1000000)

# Storing in a list for easy handling
consumers = [consumer1, consumer2, consumer3, consumer4, consumer5]

# Displaying all consumer data
for consumer in consumers:
    consumer.display()