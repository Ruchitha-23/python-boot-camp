money=int(input("given money"))
apples=int(input("enter no.of apples:"))
bananas=int(input("enter no.of bananas:"))
oranges=int(input("enter no.of oranges:"))
apples_price=(a*15)
bananas_price=(b*4)
oranges_price=(o*5)
sum=apples_price+bananas_price+oranges_price
if(sum>=money):
   print("not cheated")
else:
   print("cheated")   