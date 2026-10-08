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


     