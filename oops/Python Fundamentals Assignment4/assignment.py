# # Create a class with , ,
# # and .
# # Add to , , and .
# # BankAccount attributes account_number owner_name
# # balance
# # methods deposit withdraw check balance

# class BankAccount:
#      def __init__(self, account_num, owner_name, balance):
#           self.account_num = account_num
#           self.owner_name = owner_name
#           self.balance = balance

#      def diposit(self, amount):
#           self.balance = self.balance - amount
#           print(f"Rs {amount} deposited successfully")

#      def withdrow(self,amount):
#           if amount <= self.balance:
#                self.balance = self.balance - amount
#                print(f"Rs {amount} withdrow successfully")
#           else:
#                print("Insufficient balance")

#      def check_balance(self):
#           print(f"Current balance {self.balance}")

# account = BankAccount(234567, "Vaibhavi", 10000)
# print("Acount Number : ", account.account_num)
# print("Owner Name : ",account.owner_name)
# account.check_balance()
# account.diposit(5000)
# account.withdrow(3000)
# account.check_balance()




# Q2 Create a class Book with the following attributes:
# • title
# • author
# • list of reviews
# And add methods to:
# • add a new review
# • count reviews
# • display all reviews

# class Book:
#      def __init__(self, title, author, ):
#           self.title = title
#           self.author = author
#           self.review = []

#      def add_review(self, review):
#           self.review.append(review)
#           print("Review add successfully")

#      def count_review(self):
#           print("Total review ", len(self.review))

#      def dis_review(self):
#           print("All review")

#           for review in self.review:
#            print("-", review)

# book = Book("Python programing","John Smith")
# book.add_review("Very easy to understand.")
# book.add_review("Good book for beginners.")
# book.add_review("The examples are very useful.")

# book.count_review()
# book.dis_review()





# • display all reviews
# EncapsulationConcept:
# Create a class Student with private attributes _name, _roll_no, and _marks.
# Provide and methods with validation (e.g., marks cannot be
# negative, roll number has to be between 1 & 100 & name cannot be empty).

# class Student:
#      def __init__(self, name, roll_no, marks):
#           self._name = name
#           self.roll_no = roll_no
#           self.marks = marks

#      def set_name(self, new_name):
#           if new_name != " ":
#               self._name = new_name
#           else:
#               print("Name cannot be empty")
#           return self._name

#      def set_roll_no(self, new_roll_no):
#           if 1 <= new_roll_no <= 100:
#              self.roll_no = new_roll_no
#           else:
#               print("Roll number must be between 1 and 100")
#           return self.roll_no

#      def set_marks(self, new_marks):
#           if new_marks >= 0:
#              self.marks = new_marks
#           else:
#              print("Marks cannot be negative")
#           return self.marks



# student = Student("Vaibhavi", 32, 98)

# student.set_name("iururhu")
# print("Name:", student._name)

# student.set_roll_no(34)
# print("Roll No:", student.roll_no)

# student.set_marks(99)
# print("Marks:", student.marks)


     


# Function Overriding
# Create a class Shape with a method area().
# Create subclasses circle , rectangle , and triangle that override the area()
# method.
# Q4 Shape
# Circle Rectangle Triangle override


# import math

# class Shape:
#     def area(self):
#         print("Area of shape")


# class Circle(Shape):
#      def __init__(self, radius):
#         self.radius = radius

#      def area(self):
#         return math.pi * self.radius * self.radius

# class Rectangle(Shape):
#      def __init__(self, length, width):
#         self.length = length
#         self.width = width

#      def area(self):
#          return self.length * self.width


# class Triangle(Shape):
#      def __init__(self, base, height):
#          self.base = base
#          self.height = height

#      def area(self):
#          return 0.5 * self.base * self.height 

# c = Circle(5)
# r = Rectangle(5, 10)
# t = Triangle(4,6)

# print("Circle Area : ", round(c.area(), 2))
# print("Rectangle Area : ",r.area())
# print("Triangle Area : ", t.area())



# Inheritance Concept:
# Create a class Vehicle with attributes like brand and model.
# Create two subclasses car and bike that add extra attributes - seats (in Car) &
# engine_cc (in Bike).
# Q5 base Vehicle

# class Vehicle:
#      def __init__(self, brand, model):
#           self.brand = brand
#           self.model = model

#      def display(self):
#           print("Brand : ", self.brand)
#           print("Model : ", self.model)


# class Car(Vehicle):
#      def __init__(self, seats, brand, model):
#           super().__init__(brand, model)
#           self.seats = seats

#      def display(self):
#           super().display()
#           print("Seats : ", self.seats)

# class Bike(Vehicle):
#      def __init__(self, brand, model, engine_cc):
#           super().__init__(brand, model)
#           self.engine_cc = engine_cc

#      def display(self):
#           super().display()
#           print("Engine_cc : ", self.engine_cc)

# car1 = Car("Tata", "Nexon", 4)
# bike1 = Bike("Royal Enfield", "Classic 350", 350)

# print("Car Details: ")
# car1.display()

# print("\nBike Details: ")
# bike1.display()






# Concept:Abstraction
# Create an abstract class Employee with an abstract method
# calculate_salary().
# Create subclasses Intern FullTimeEmployee and ContractEmployee that
# implement the method differently.


# from abc import ABC, abstractmethod

# class Employee:
#      @abstractmethod
#      def calculate_salary(self):
#           pass

# class Intern(Employee):
#      def calculate_salary(self):
#           print("Intern Salary: 10000")

# class FullTime_Emp(Employee):
#      def calculate_salary(self):
#           print("Full Time Salary: 40000")

# class ContractEmployee(Employee):
#      def calculate_salary(self):
#           print("Contract Salary: 20000")

# e1 = Intern()
# e2 = FullTime_Emp()
# e3 = ContractEmployee()

# e1.calculate_salary()
# e2.calculate_salary()
# e3.calculate_salary()




# Concept: Constructor Overloading (with Default Parameters
# . Create a class that allows the constructor to work with:Q7 Person
# • name only
# • name + age
# • name + age + address
# As direct constructor overloading (multiple constructors) are not allowed but
# we have to use default parameters to simulate constructor overloading.

class Person:
     def __init__(self,name, age = None, address = None):
          self.name = name
          self.age = age
          self.address = address

     def display(self):
          print("Name : ", self.name)
          print("Age : ", self.age)
          print("Address : ", self.address)

p1 = Person("Vaibhavi")
p2 = Person("Vaibhavi", 22)
p3 = Person("Vaibhavi", 22, "Ahilyanager")

print("Person 1:")
p1.display()

print("\nPerson 2:")
p2.display()

print("\nPerson 3:")
p3.display()