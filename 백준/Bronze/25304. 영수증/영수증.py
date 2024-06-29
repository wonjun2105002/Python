a = int(input())
z = int(input())
sum = 0
for i in range (z):  
    b, c = map(int, input().split())
    sum = sum+b*c  

if sum==a:
    print ("Yes")

else:
    print ("No")