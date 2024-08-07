a, b = map(int, input().split())
m1 = []
m2 = []


for i in range (a):
    m1.append(list(map(int,input().split())))
    
for i in range (a):
    m2.append(list(map(int,input().split())))

for i in range(a):
    for j in range(b):
        print(m1[i][j] + m2[i][j], end = " ")
    print()




