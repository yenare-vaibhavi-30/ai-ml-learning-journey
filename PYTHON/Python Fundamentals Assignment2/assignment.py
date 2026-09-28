# Write a program that takes as input. Using conditional statements,
# calculate the based on these rules:
# Q1 salary
# final tax rate
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

# salary = int(input("Enter a salary : "))
# if salary < 3000:
#      tax_rate = 5
# elif salary <= 70000:
#      tax_rate = 15
# else:
#      tax_rate = 25

# tax = tax_rate * salary / 100
# print("Salary : ", salary)
# print("Tax Rate : ", tax_rate)
# print("Tax : ", tax)


# Write a function that takes two integers and and prints all even
# numbers between them (inclusive).

# def even_odd(a , b):
#      for i in range(a, b):
#           if i % 2 == 0:
#                print(i)
# print(even_odd(1,20))

# def even_odd(a, b):
#      for i in range(a , b):
#           if i % 2 == 0:
#                print(i)
# print(even_odd(1, 30))

# Write a function that prints the of a number, .Q3 digits n
# For eg: , there are 3 digits in it 3, 1 and 2 & we need to print them.


# def print_digit(n):
#      for digit in str(n):
#           print(digit)
# print_digit(123)


# Write a function to return the count the number of digits in a number n

def count_num(n):
     count = 0
     while n > 0:
          n = n // 10
          count += 1
     return count
result = count_num(987654)
print(result)