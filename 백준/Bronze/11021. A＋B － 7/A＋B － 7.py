n = int(input())
i = 1

while n > 0:
    a, b = map(int, input().split())

    print ("Case #"+str(i)+":", a+b )
    n = n-1
    i = i+1