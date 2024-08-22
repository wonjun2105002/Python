a = int(input())
for i in range (a):
    res = 0
    b , c = map(int, input().split())
    for x in range (1, b):
        for y in range (x+1, b):
            if (x**2+y**2+c)%(x*y) == 0:
                res +=1

    print(res)