class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
        
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)
        
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
        
    def print_name(self):
        print("Grandfather name : ",self.grandfathername)
        print("Father name : ",self.fathername)
        print("Son name : ",self.sonname)
            
s1 = Son("Samarth", "Sandip", "Kerappa")
print(s1.grandfathername)
s1.print_name()

#Explanation:

#Son inherits from Father, and Father inherits from Grandfather.
#Each constructor passes values up the inheritance chain using explicit constructor calls.
#All ancestor class attributes are accessible from the bottom-most class (Son).
