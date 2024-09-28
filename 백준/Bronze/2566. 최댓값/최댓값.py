a = []
for i in range (9):
        a.append(list(map(int, input().split())))
b = 0
c = 0
d = 0
for i in range (9):
        for j in range (9):
                if b < a[i][j]:
                        b = a[i][j]
                        c = i
                        d = j

print (b)
print (c+1, d+1)
                        


