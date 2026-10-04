class student:
     college_name = "ABC college" ##class attribute

     def __init__(self, name, gpa):
          self.name = name   ## instance class
          self.gpa = gpa

stu1 = student("vaibhavi", 9.4)
print(stu1.name)
print(student.college_name)