a, b = map(int, input().split())

l = []
for i in range (1, a+1):
    l.append(i)
    
for j in range (b):
    x, y = map(int, input().split())
    l[x-1], l[y-1] = l[y-1], l[x-1]
    
print(*l)