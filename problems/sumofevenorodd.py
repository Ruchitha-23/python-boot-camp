n=int(input())
sum=0
while n>0:
    r=n%10
    if(r%2==0):
        sum+=r**2
        n=n//10
        print(f"sum of even numbers {sum}")
    else:
        print(f"sum of odd numbers {sum}")

