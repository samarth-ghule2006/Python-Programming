import math_module                                   # import Module

def main():
    print("Enter first Number :")
    Value1 = int(input())
    
    print("Enter second Number :")
    Value2 = int(input())
    
    Ret = math_module.Addition(Value1,Value2)        # Module.Function_name
    
    print("Addition is :",Ret)

if __name__ == "__main__":      
    main()