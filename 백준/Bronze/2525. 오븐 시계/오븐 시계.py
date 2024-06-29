a, b = map(int, input().split())
c = int(input())

if c+b >= 60:
    if (c+b)//60 + a > 23:
        print (0+((c+b)//60 + a)-24, (c+b)%60)
    else :
        print ((c+b)//60 + a , (c+b)%60)
        
elif c+b < 60:
    print (a, c+b)