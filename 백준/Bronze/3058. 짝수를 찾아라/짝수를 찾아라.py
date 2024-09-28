a = int(input())

for i in range (a):
        l = list(map(int,input().split()))
        b = []
        for j in range (7) :
                if l[j] % 2 == 0:
                        b.append(l[j])
        print(sum(b),min(b))