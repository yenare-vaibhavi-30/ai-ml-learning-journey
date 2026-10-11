# try: 
#      x = int(input("Enter x : "))
#      ans = 10 / x

# except ZeroDivisionError:
#      print("Divide by 0 is not allowed")
# else:
#      print(f"ans = {ans}")




# try: 
#      x = int(input("Enter x : "))
#      ans = 10 / x
# except ValueError:
#      print(f"Invalid input")
# else:
#      print(f"ans = {ans}")



# try:
#      a = 10
#      b = 0
#      print(a / b)
# except ZeroDivisionError:
#      print("Cannot divide by zero")



# ValueError
# number = int("hello")


# # TypeError
# result = "10" + 5

# # IndexError
# numbers = [10, 20, 30]
# print(numbers[5])

# # KeyError
# student = {"name": "Vaibhavi"}
# print(student["age"])








# ValueError
# try:
#      age = int(input("Enter your age: "))
#      print("your age is ", age)
# except ValueError:
#      print("Please enter a valid number")




# try:
#      number = int(input("Enter a number: "))
#      result = 100 / number
# except ValueError:
#      print("Enter a number")

# except ZeroDivisionError:
#      print("Number cannot be zero")

# else:
#      print("Result : ", result)
# finally:
#      print("program execution completed") 





# ZeroDivisionError	Number ला zero ने divide केल्यावर
# ValueError	योग्य type असलेल्या function ला चुकीची value दिल्यावर
# TypeError	दोन incompatible types वर operation केल्यावर
# IndexError	List मधील नसलेला index वापरल्यावर
# KeyError	Dictionary मध्ये नसलेली key access केल्यावर
# NameError	Define न केलेले variable वापरल्यावर
# FileNotFoundError	अस्तित्वात नसलेली file उघडण्याचा प्रयत्न केल्यावर
# AttributeError	Object कडे नसलेली attribute किंवा method वापरल्यावर