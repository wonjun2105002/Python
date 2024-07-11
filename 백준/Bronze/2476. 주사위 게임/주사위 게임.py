z = int(input())
res = 0 
for i in range(z):
    a, b, c = map(int, input().split())

    if a == b == c:
        res = max(res,10000+a *1000)

    elif (a == b and b != c) or (a == c and b != c):
        res = max(res, 1000 + a *100)

    elif c == b and a != c:
        res = max(res, 1000 + c *100)
        
    elif (a>b and b>c) or (a>c and c>b):
         res = max(res, a *100)
        
    elif (b>c and c>a) or (b>a and a>c):
        res = max(res, b *100)
        
    elif (c>a and a>b) or (c>b and b>a):
        res = max(res, c *100)
        
print (res)