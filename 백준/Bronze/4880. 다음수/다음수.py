while True:
    a, b, c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break

    if b - a + b == c:
        print ("AP", c + (b - a))   
        
    elif (b // a)* b == c:
        print ("GP", c * (b // a))

    
        