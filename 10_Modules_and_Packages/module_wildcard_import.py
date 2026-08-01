from math_module import *

def main():
    print("Enter first Number :")
    Value1 = int(input())
    
    print("Enter second Number :")
    Value2 = int(input())
    
    Ret = Addition(Value1,Value2)    
    print("Addition is :",Ret)
    
    Ret = Subtraction(Value1,Value2)
    print("Subtraction is :",Ret)

if __name__ == "__main__":      
    main()