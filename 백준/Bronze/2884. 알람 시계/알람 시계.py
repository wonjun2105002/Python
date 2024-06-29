a, b = map(int, input().split())
if 45 <= b <= 59:
    print(a, b-45)

elif b < 45:
    if a == 0 :
        print (23, b+15)

    else :    
        print (a-1, 60-(45-b))