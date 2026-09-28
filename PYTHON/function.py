# def hello():
#      print("Hello python")
# hello()

# def welcome():
#      print("Welcome to python")
# welcome()
# welcome()
# welcome()


# def greet(name):
#     print("hello ", name)
# greet("vaibhavi")

# def add(a, b):
#      print(a + b)
# add(12, 43)

# def sub(a, b):
#      print(a - b)
# sub(12, 43)

# def mul(a, b):
#      print(a * b)
# mul(12, 43)


# def div(a, b):
#      print(a / b)
# div(12, 4)


# def square(num):
#      print(num * num)
# square(10)


# def cube(n):
#      return n ** 3
# num = int(input("Enter a number : "))
# result = cube(num)
# print("Result = ", result)


# def check_even_odd(n):
#      if n % 2 == 0:
#         print(n , " is even number ")
#      else:
#         print(n , " is odd number ")
# num = int(input("Enter a number "))
# check_even_odd(num)

# def check_pos_neg(n):
#      if n > 0:
#           print(n, " is positive number")
#      elif n < 0:
#           print(n , " is negative number")
#      else:
#           print(n , " is zero")
# num = int(input("Enter a number: "))
# check_pos_neg(num)


# def check_large(a , b):
#      if a >= b:
#           print(a , " is largest number")
#      else:
#           print(b , ' is largest number')
# num1 = int(input("Enter a number "))
# num2 = int(input("Enter a number "))
# check_large(num1, num2)


# def check_large(a , b, c):
#      if a >= b:
#           print(a , " is largest number")
#      elif b >= c:
#           print(b , ' is largest number')
#      else:
#           print(c, " is largest number ")
# num1 = int(input("Enter a number "))
# num2 = int(input("Enter a number "))
# num3 = int(input("Enter a number "))
# check_large(num1, num2, num3)


# def total_sum(*args):
#      return sum(args)
# result = total_sum(10, 20, 30, 40)
# print(result)

# def sutdent_info(**kwargs):
#      for key, value in kwargs.items():
#           print(key, " = ", value)
# sutdent_info(
#      name = "Vaibhavi",
#      age = 21,
#      course = "MCA"
# )

# def car_info(**kwargs):
#      for key, value in kwargs.items():
#           print(key , " : ", value)
# car_info(
#      car_name = "Thar",
#      car_number = 3453,
#      car_color = "Black"
# )


# add = lambda a, b : a + b
# result = add(10,20)
# print(result)

# square = lambda num : num * num
# print(square(3))

# check = lambda n : "even" if n % 2 == 0 else "odd"
# print(check(5))


# def square(n):
#      return n * n
# def calculate(func, number):
#      return func(number)
# result = calculate(square, 5)
# print(result)


def outer():
     def inner():
          print("Hello form inner function")
     inner()
outer()