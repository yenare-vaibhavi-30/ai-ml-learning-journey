# class Employee:
#      start_time = "10am"
#      end_time = "6pm"

#      def chenge_end_time(self, new_end_time):
#           self.end_time = new_end_time

# class Teacher(Employee):
#      def __init__(self,subject):
#           self.subject = subject

# class AdminStaff(Employee):
#      def __init__(self, role):
#           self.role = role

# staff1 = AdminStaff("Manager")
# print(staff1.role, staff1.start_time, staff1.end_time)

# # t1 = Teacher("Math")
# # t1.chenge_end_time("5pm")
# # print(t1.subject, t1.start_time, t1.end_time)


# class Employee:
#      start_time = "10am"
#      end_time = "6pm"

# class AdminStaff(Employee):
#      def __init__(self, role):
#           self.role = role

# class Accountant(AdminStaff):
#      def __init__(self, salary, role):
#           super().__init__(role)
#           self.salary = salary

# acc1 = Accountant("CA", 40_000)
# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)


# class Teacher:
#      def __init__(self, salary):
#           self.salary = salary

# class Student:
#      def __init__(self, cgpa):
#           self.cgpa = cgpa

# class TA(Teacher, Student):
#      def __init__(self, salary, cgpa, name):
#           super().__init__(self, salary)
#           Student.__init__(cgpa)
#           self.name = name 

# info = TA(30_000, 9.2, "Vaibhavi")
# print(info.salary, info.cgpa, info.name)

