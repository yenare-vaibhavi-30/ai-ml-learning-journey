# instance method
# instance has self parameter
# access the class and instance attribute

class Laptop:
     storage_type = "ssd"

     def __init__(self, RAM, Storage):
          self.RAM = RAM
          self.Storage = Storage

     def get_info(self):
          print(f"laptop has {self.RAM} RAM and {self.Storage} {self.storage_type}")

stu1 = Laptop("16gb", "512gb")
stu2 = Laptop("8gb", "252gb")

stu1.get_info()