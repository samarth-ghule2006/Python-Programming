def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Enter first Number :")
    Value1 = int(input())
    
    print("Enter second Number :")
    Value2 = int(input())
    
    Ret = Addition(Value1,Value2)
    
    print("Addition is :",Ret)

if __name__ == "__main__":      # starter
    main()