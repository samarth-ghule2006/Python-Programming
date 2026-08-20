class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass

#Explanation:

#self._age: Defined with a single underscore, marking it as protected.
#SubEmployee: Inherits from Employee and can access _age directly.
#Protected members should not be accessed outside the class hierarchy, but Python does not enforce this rule strictly.
