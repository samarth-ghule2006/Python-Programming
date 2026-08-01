# 1) Function which accepts nothing and returns nothing

def Function1():
    print("Inside Function1")
    
# 2) Function which accepts value and returns nothing

def Function2(value):
    print("Inside Function2")
    print("Accepted value is : " ,value)
    
# 3) Function which accepts value and returns value

def Function3(value):
    print("Inside Function3")
    print("Accepted value is : " ,value)
    return value + 1
    
# 4) Function which accepts multiple values and returns multiple values

def Function4(value1, value2):
    print("Inside Function4")
    add = value1 + value2
    sub = value1 - value2
    return add, sub

# 5) Function which calls another function defined outside it

def Function5():
    print("Inside Function5")
    Function1()     # calling another function
    
# 6) Function which contains another nested function inside it

def Function6():
    print("Inside Function6")
    
    def InnerFun():
        print("Inside InnerFun")
        
    InnerFun()      # call nested function
    
# Function calls for above functions
no = 11

Function1()

Function2(no)

Ret = Function3(no)
print("Return value is : ",Ret)

ret1, ret2 = Function4(10,4)
print("Addition is : ",ret1)
print("Subtraction is : ",ret2)

Function5()

Function6()