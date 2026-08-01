import math_module as MM                                 

def main():
    print("Enter first Number :")
    Value1 = int(input())
    
    print("Enter second Number :")
    Value2 = int(input())
    
    Ret = MM.Addition(Value1,Value2)      
    
    print("Addition is :",Ret)

if __name__ == "__main__":      
    main()