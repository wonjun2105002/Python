a = int(input())
for i in range (a):
    p1 = 0
    p2 = 0  
    b = int(input())
    for j in range (b):
        c, d = input().split()
        if c == "R" and d == "P":
            p2 += 1
        if c == "P" and d == "S":
            p2 += 1
        if c == "S" and d == "R":
            p2 += 1
        if c == "P" and d == "R":
            p1 += 1
        if c == "S" and d == "P":
            p1 += 1
        if c == "R" and d == "S":
            p1 += 1

    if p1 > p2:
        print("Player 1")
    elif p2 > p1:
        print("Player 2")
    else : 
      print("TIE")