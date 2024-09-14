l = []
z = []

for i in range (10):
    a = int(input())
    l.append(a)

for i in range (10):
    b = int(input())
    z.append(b)

l.sort()
z.sort()

print(l[7]+l[8]+l[9], z[7]+z[8]+z[9]) 




