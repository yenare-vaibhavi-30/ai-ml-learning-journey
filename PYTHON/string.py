# world = "python"
# print(world[0])


# world = "I study from ApnaCollege"
# print(world[13:25])

# world = "python"
# print(world[-4: -2])

# a = 5
# b = 10
# sum = a + b

# # normal formationg

# print("language is {}".format("python"))
# print("sum of {} & {} is {}".format(a, b, sum))

# # index based formating
# print("sum of {1} & {0} is {2}".format(a, b, sum))


# a = 5
# b = 10
# print(f"sum of {a} & {b} is {a + b}")
# print(f"avg of {a} & {b} is {(a + b)/2}")

# List
# marks = [99, 75, 98, 67, 86, 85, 85, "uhehfu", 100.00]
# print(marks)
# print(marks[6])
# print(len(marks))
# print(type(marks))
# print(marks[0:5])

# nums = [1,2 ,3]
# nums.append(4)
# print(nums)

# nums.insert(2,10)
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# nums.reverse()
# print(nums)


# nums = [1,2,3,10,4]
# x = 10
# idx = 0

# for val in nums:
#      if (val == x):
#           print(f" x is found at idx = {idx}")
#           break
#      idx += 1


# tup = ("abc",)
# print(type(tup))

# tup = (1,2,3,4,5)
# sum = 0
# for val in tup:
#      sum += val
# print(f"Sum of value is {sum}")

# tup = (1,5,8,4,5,6)
# print(tup.index(5))


# info = {
#      "name" : "Vaibhavi",
#      "age" : 22,
#      "cgpa" : 9.4,
#      "subject" : ["python", "math"],
#      3.14 : "PI",
# }
# print(info)
# print(type(info))
# print(info[3.14])
# info["cgpa"] = 9.6
# print(info["cgpa"])
# dict_value = list(info.values())
# print(dict_value)
# print(info.get("cgpa2",))
# print("End of code")
# info.update({
#      "city": "Pune"
# })
# print(info)


# sets = {1,2,3,3,4,3,6}

# #add()
# sets.add(5)
# print(sets)

# empty_set = set()
# print(type(empty_set))

# # remove
# sets.remove(1)
# print(sets)

# #clear
# sets.clear()
# print(sets)

#pop
# print(sets)
# sets.pop()
# print(sets)


# s1 = {1,2,3,4,5}
# s2 = {4,5,6,8,9}

# #union
# print(s1.union(s2))

# #intersection
# print(s1.intersection(s2))


info = [
     ("Alice" , "Math"),
     ("Bob" , "Science"),
     ("Alice" , "Science"),
     ("Charlie" , "Math"),
     ("Bob" , "Math"),
     ("Alice" , "English"),
     ("Charlie" , "English"),
]

# unique_courses = set()
# for tup in info:
#      unique_courses.add(tup[1])
# print(unique_courses)

# for name,course in info:
#      if(course == "English"):
#           print(name)
      
dict = {}
for name,course in info:
     if(dict.get(name) == None):
          dict.update({name: set()})
          dict[name].add(course)
     else: 
          dict[name].add(course)
print(dict)