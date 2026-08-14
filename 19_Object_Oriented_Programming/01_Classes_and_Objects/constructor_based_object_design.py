class Arithmetic:
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B
        
    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Subtraction(self):
        Ans = self.No1 - self.No2
        return Ans

print("Enter first number : ")
Value1 = int(input())

print("Enter first number : ")
Value2 = int(input())

aobj = Arithmetic(Value1, Value2)

Ret = aobj.Addition()            
print("Addition is : ",Ret)

Ret = aobj.Subtraction()         
print("Subtraction is : ",Ret)