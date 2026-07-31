print("----------------------------------")
print("------Ticket Pricing Software-----")
print("----------------------------------")

print("Enter you Age : ")
Age = int(input())

if(Age <= 5):
    print("Ticket is Free")
elif(Age > 5 and Age <= 18):
    print("Ticket price is Rs900")   
elif(Age > 18 and Age <= 40):
    print("Ticket price is Rs1200")
else:
    print("Ticket price is Rs500") 
