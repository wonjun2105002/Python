while True:
    a, b ,c = map(int,input().split())
    t = [a, b, c]
    t.sort()
   
    if a == 0 and b == 0 and c == 0:
        break
    elif t[0]+t[1] <= t[2]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif (a == b and c != a) or (a == c and b != c) or (c == b and a != b ):
        print ("Isosceles")
    elif a != b != c:
        print ("Scalene")