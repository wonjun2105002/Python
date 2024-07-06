a = int(input())

b, c, d = map(int, input().split())

r= 0

if a >= b:
    r += b
    
elif a < b:
    r += a

if a >= c:
    r += c

elif a < c:
    r += a

if a >= d:
    r += d

elif a < d:
    r += a

print (r)