a, b ,c, d = map(int, input().split())
list = []
list.append (a)
list.append (b)
list.append (d-b)
list.append (c-a)
print(min(list))
