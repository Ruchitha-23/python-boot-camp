a=int(input("enter number\n"))
if(a%2==0 and a>0):
    print(f"{a} is positive even number")
elif(a%2==0 and a<0):
    print(f"{a} is negitive even number")
elif(a>0):
    print(f"{a} is positive odd number")
else:
    print(f"{a} is negitive odd number")