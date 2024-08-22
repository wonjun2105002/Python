b = int(input())
while True:
    a = int(input())
    if a == 0: break
    elif a%b == 0:
        print (str(a) + " is a multiple of "+str(b)+".")
    else:
        print (str(a) + " is NOT a multiple of "+str(b)+".")