# instance method
# instance has self parameter
# access the class and instance attribute

# class Laptop:
#      storage_type = "ssd"

#      def __init__(self, RAM, Storage):
#           self.RAM = RAM
#           self.Storage = Storage

#      def get_info(self):
#           print(f"laptop has {self.RAM} RAM and {self.Storage} {self.storage_type}")

# stu1 = Laptop("16gb", "512gb")
# stu2 = Laptop("8gb", "252gb")

# stu1.get_info()

#  ---------------class method--------------#

# class Laptop:
#      storage_typa = "ssd"

#      def __init__(self, RAM, Storage):
#           self.RAM = RAM
#           self.Storage = Storage

#      @classmethod
#      def get_storage_type(cls):
#           print(f"Storage Type ={cls.storage_typa}")

#      def get_info(self):
#           print(f"laptop has {self.RAM} RAM and {self.Storage} {self.storage_typa}")

# l1 = Laptop("16gb", "512gb")
# l1.get_storage_type()


# ____________________ Static Method _______________#
# class Laptop:
#      storage_typa = "ssd"

#      def __init__(self, RAM, Storage):
#           self.RAM = RAM
#           self.Storage = Storage

#      @classmethod
#      def get_storage_type(cls):
#           print(f"Storage Type ={cls.storage_typa}")

#      def get_info(self):
#           print(f"laptop has {self.RAM} RAM and {self.Storage} {self.storage_typa}")

#      @staticmethod
#      def calc_discount(price, discount):
#           final_price = price - (discount * price / 100)
#           print(f"discounted price = {final_price}")
     
# l1 = Laptop("16gb", "512gb")
# l1.calc_discount(40_000, 10)



# Practice

class Product:
     count = 0

     def __init__(self, name, price):
          self.name = name
          self.price = price
          Product.count += 1

     def get_info(self):
          print(f"price of {self.name} is Rs. {self.price}")

     @classmethod
     def get_count(cls):
          print(f"total products in store {cls.count}")

     @staticmethod
     def calc_discount(price, discount):
          print(f"discounted price = {price - (price * discount / 100)}")

p1 = Product("Phone", 10_000)
p2 = Product("Laptop", 50_000)
p3 = Product("Pen", 10)

# Product.get_count()
Product.calc_discount(50_000, 20)