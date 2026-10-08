# from abc import ABC, abstractmethod

# class Animal(ABC):
#      @abstractmethod 
#      def make_sound(self):
#           pass

# class Lion(Animal):
#      def make_sound(self):
#           print("Roar!")

# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")

# lion = Lion()
# lion.make_sound()

# cow = Cow()
# cow.make_sound()




# from abc import ABC, abstractmethod

# class Bank(ABC):
#      def withdrow(self, amount):
#           pass

# class SBI(Bank):
#      def withdrow(self, amount):
#       print(f"withdrowing Rs {amount} for SBI account")

# class HDFC(Bank):
#     def withdrow(self, amount):
#         print(f"withdrowing Rs {amount} for HDFC account")

# sbi = SBI()
# sbi.withdrow(2000)

# hdfc = HDFC()
# hdfc.withdrow(5000)


from abc import ABC, abstractmethod

class Vehicle(ABC):
     def start(self):
          pass

class Car(Vehicle):
     def start(self):
          print(f"Car is start")

class Bike(Vehicle):
     def start(self):
          print(f"bike is start")

car = Car()
car.start()

bike = Bike()
bike.start()
