a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
g, h = map(int, input().split())

l = []

l.append(b)
l.append(b-c+d)
l.append(b-c+d-e+f)
l.append(b-c+d-e+f-g)

print(max(l))
