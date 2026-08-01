def CheckEven(No):
    if (No % 2 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter the number :")
    Value = int(input())
    
    Ret = CheckEven(Value)
    
    if(Ret == True):
        print("It is Even Number")
    else:
        print("It is Odd Number")
        
if __name__ == "__main__":
    main()