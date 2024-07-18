while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    if b/a == b//a:
        print ("factor")
    elif a/b == a//b:
        print ("multiple")
    else:
        print ("neither")
