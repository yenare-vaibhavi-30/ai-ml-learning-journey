# Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string which is same when we read it forward & backward. Eg -
# “madam”, “raceca" 

# world = (input("Enter a string : "))

# if world == world[::-1]:
#      print(" is palidrom")
# else:
#      print(" is not palidrom")



# Given a list of integers compute the average of all numbers in the list.

# nums = [10,20,30,40]
# total = sum(nums)
# count = len(nums)
# avg = total / count
# print(avg)

#  Input two lists of integers from the user. Merge them into one list and sort the
# result.
# Eg - ,list1 = [1, 2, 7] list2 = [2, 4, 5]
# result = [1, 2, 3, 54, 5, 7]

# num1 = list(map(int,input(" Enter a number : ").split()))
# num2 = list(map(int,input("Enter a number : ").split()))
# result = num1+num2
# print(result)


#  Given a tuple of integers, create
# • A tuple of all even numbers
# • A tuple of all odd numbers

# numbers = (1, 2, 3, 4, 5, 6, 7, 8)

# even = ()
# odd = ()

# for num in numbers:
#      if num % 2 == 0:
#           even += (num,)
#      else:
#           odd += (num,)
# print(even, " is even")
# print(odd, " is odd")


#  Create a dictionary where
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ)
# depending on the operation they want to perform on the dictionary:
# 1. - Add a studentA
# 2. - Update marksB
# 3. - Search for a studentC
# 4. - Display all students and marks

# students = {}

# while True:
#      print("\n Student marks menu : ")
#      print(" A. Add a student A")
#      print(" B. Update a marks")
#      print(" C. Search a student")
#      print(" D Display all students marks")

#      choice = input("Enter your choice : ").upper()

#      if choice == "A":
#           name = input("Enter a name : ")
#           marks = input("Enter a marks : ")
#           students[name] = marks 
#           print("student added successfully")

#      elif choice == "B":
#           name = input("Enter a student name : ")

#           if name in students:
#                marks = input("Enter a new marks")
#                students[name] = marks
#                print("marks update successfully")
#           else:
#                print("student is not found")

#      elif choice == "C":
#           name = input("Enter a student name : ")

#           if name in students:
#                print("Student : ", name)
#                print("Marks : ", students[name])
#           else:
#                print("Student is not found")

#      elif choice == "D":
#           if len(students) == 0:
#                print(" No student found")
#           else :
#                print("\n Student Name - Marks")
#                for name,marks in students.items():
#                     print(name, " = ", marks)
     
#      elif choice == "E":
#           print("Program is end")
#           break

#      else:
#           print("Invalid choice! Please enter A, B, C, D or E")
               
          
#  Given a list of words:Q6
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...}

# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# result = {}
# for word in words:
#      result[word] = len(word)
# print(result)

# Write a program that takes a string from the user and prints the number of
# spaces in the string.

text = input("Enter a any sentence : ")
result = (text.count(" "))
print(result)