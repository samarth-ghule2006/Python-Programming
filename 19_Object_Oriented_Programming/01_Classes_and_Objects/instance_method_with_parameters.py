class Arithmetic:

    def Addition(self, No1, No2):
        Ans = No1 + No2
        return Ans

    def Subtraction(self, No1, No2):
        Ans = No1 - No2
        return Ans
    
aobj = Arithmetic()

print("Enter first number : ")
Value1 = int(input())

print("Enter first number : ")
Value2 = int(input())

# Ret = Addition(aobj, value1, value2)
Ret = aobj.Addition(Value1, Value2)            
print("Addition is : ",Ret)

Ret = aobj.Subtraction(Value1, Value2)         
print("Subtraction is : ",Ret)