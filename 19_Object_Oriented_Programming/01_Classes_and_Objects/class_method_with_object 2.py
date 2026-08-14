class Demo:
    # Class Variables
    Value1 = 10
    Value2 = 20
    
    def __init__(self):
        # Instance Variable
        self.No1 = 11
        self.No2 = 21
        
    # Instance Method
    def fun(self):
        print("Inside Instance Method named as fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)
        
    # Class Method
    @classmethod
    def gun(cls):       
        print("Inside Class Method named as gun")
        # print(Demo.No1)   Not allowed
        # print(Demo.No2)   Not allowed
        print(Demo.Value1)
        print(Demo.Value2)

# Call with object
dobj = Demo()
dobj.gun()