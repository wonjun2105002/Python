a = int(input())
l = []
u = []
for i in range (a):
    z, y = map(int,input().split())
    l.append(y)
    u.append(z)
print((max(l) - min(l))*(max(u)-min(u)))
    
