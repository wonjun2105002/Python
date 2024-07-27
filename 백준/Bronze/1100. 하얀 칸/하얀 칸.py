 
a = list()
for i in range (8):
    b = list(input())
    a.append(b)
c = 0
for i in range (8):
    for j in range (8):
        if i%2 == 0 and j%2 == 0 and a[i][j] == "F":
            c = c+1
        if i%2 == 1 and j%2 == 1 and a[i][j] == "F":
            c = c+1
        
print(c)

