a, b, c = map(int, input().split())

if a==b and b==c:
    print( 10000+a*1000 )
elif (a==b and b!=c) or (a!=c and c==b):
    print(1000+b*100)
elif (a==c and b!=c):
    print(1000+a*100)
elif (a!=b and b!=c) and a>b>c:
    print (a*100)
elif (a!=b and b!=c) and a>c>b:
    print (a*100)
elif (a!=b and b!=c) and b>c>a:
    print (b*100)
elif (a!=b and b!=c) and b>a>c:
    print (b*100)
elif (a!=b and b!=c) and c>b>a:
    print (c*100)
elif (a!=b and b!=c) and c>a>b:
    print (c*100)
