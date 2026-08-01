CheckEven = lambda No : (No % 2 == 0)

Value = int(input("Enter the Number : "))

Ret = CheckEven(Value)

if(Ret == True):
    print("It is Even Number")
else:
    print("It is Odd Number")