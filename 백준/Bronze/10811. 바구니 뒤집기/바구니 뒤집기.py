a, b = map(int, input().split())
l = []
for i in range (1, a+1):
    l.append(i)

for j in range (b) :
    x, y = map(int, input().split())
    l2 = l[x-1 : y]
    l2.reverse()
    l[x-1 : y] = l2

print (*l)