# print even or odd

# num = int(input("Enter a number : "))
# if num % 2 == 0:
#      print(num , " is even")
# else:
#      print(num, " is odd")


# 2. Positive, Negative or Zero

# num = int(input("Enter a number : "))
# if num > 0:
#      print(num , " is positive")
# elif num < 0:
#      print(num, " is negative")
# else:
#      print(num, " is zero")


#3. Swap Two Numbers
# num1 = 10
# num2 = 20
# num1 ,  num2 =  num2 , num1
# print("Num1 ",num1)
# print("Num2 ",num2 )


# Largest of Three Numbers

# num1 = int(input("Enter a fisr number "))
# num2 = int(input("Enter a second number "))
# num3 = int(input("Enter a third number "))
# if num1 >= num2:
#      print(num1 ,"is greter")
# elif num2 >= num3:
#      print(num2, " is greter")
# else: 
#      print(num3, " is greter")


# Sum of Digits
# num = int(input("Enter a numners "))


# num = 1234
# total = 0

# while num > 0:
#     digit = num % 10
#     total = total + digit
#     num = num // 10

# print("Sum of digits:", total)



# Reverse a Number

# num = int(input("Enter a number : "))
# revers = 0

# while num > 0:
#      digit = num % 10
#      revers = revers * 10 + digit
#      num = num // 10

# print("Reverce number : ", revers)


#Palindrome Number

# num = int(input("Enter a number : "))
# original = num
# reverse = 0

# while num > 0:
#      digit = num % 10
#      reverse = reverse * 10 + digit
#      num = num // 10

# if original == reverse:
#      print("Number is palinderom", original)
# else:
#      print("Number is not palinderom")


# Factorial

# num = int(input("Enter a number : "))
# factorial = 1
# i = 1

# while i <= num:
#      factorial = factorial * i
#      i = i + 1
#      print("Factorial : ", factorial)


# Multiplication Table

# num = int(input("Enter a number  : "))
# digit = 1
# while digit <= 10:
#      print(num, " x ", digit ," = ", num * digit)
#      digit = digit + 1



# Prime Number

# num = int(input("Enter number : "))

# if num <= 1:
#      print("Not a prime number")
# else:
#      for i in range(2, num):
#           if num % i == 0:
#                print("Not a prime number")
#                break
#           else:
#                print("prime number")


# Count Digits

# num = int(input("Enter a number : "))
# count = 0

# while num > 0:
#      num = num // 10
#      count = count + 1
#      print(count)
     

# 7. Armstrong Number — उदा. 153 → Armstrong

num = int(input("Enter a number : "))
total = 0
temp = num
power = len(str(num))

while temp > 0:
     digit = temp % 10 
     total = total + digit ** power
     temp = temp // 10
     if total == num:
          print("is Amstrong number")
     else:
          print("not a Amstrong number")