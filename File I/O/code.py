
# f = open("File I\\O/sample.txt", "r")
# data = f.read()
# print(data)
# f.close()



# f = open("File I\\O/sample.txt", "r")

# data = f.readline()
# print(data)

# data = f.readline()
# print(data)

# f.close()


# f = open("File I\\O/sample.txt", "w")
# f.write("Text to overwrite \n the complete data.")
# f.close()


# ------------------  File Operations Modes -------------------

# 1) reading [default]

# f = open("File I\\O/sample.txt")
# print(f.read())
# f.close()


# writing, appends at end
# f = open("File I\\O/sample.txt", "a")
# f.write(" New text being appended \n to the file ")
# f.close()


# # create a new & open for writing
# f = open("File I\\O/sample2.txt", "x")
# f.write("Some random text")
# f.close()



# f = open("File I\\O/sample2.txt", "r+")
# f.write("123")
# print(f.read())
# f.close()




# f = open("File I\\O/sample2.txt", "a+")
# f.write("123")
# print(f.read())
# f.close()






data = True
line = 1
world = "store"

with open("File I\\O/sample.txt", "r") as f:
     while data: 
          data = f.readline()

          if(world in data):
               print(f"word found at line {line}")
               break
          print(data)
          line += 1