class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible

#Explanation:

#self.name: Declared without underscores, so it is public.
#display_name(): Public method that prints the value of the public attribute.
#emp.name: Directly accessed from outside the class, showing public members are fully accessible.
