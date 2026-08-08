def Addition(No1, No2):
    Ans = No1 + No2
    return Ans

def Subtraction(No1, No2):
    Ans = No1 - No2
    return Ans

print("Enter first number : ")
Value1 = int(input())

print("Enter first number : ")
Value2 = int(input())

Ret = Addition(Value1, Value2)
print("Addition is : ",Ret)

Ret = Subtraction(Value1, Value2)
print("Subtraction is : ",Ret)