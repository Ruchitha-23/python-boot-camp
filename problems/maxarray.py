arr=list(map(int,input().split(" ")))
max=arr[0]
for i in range(len(arr)):
    if(max<arr[i]):
        max=arr[i]
print(max)