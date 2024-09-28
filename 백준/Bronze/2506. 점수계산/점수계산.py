a = int(input())
l = list(map(int,input().split()))
plus = 0
b = 0
for i in range (a):
        if l[i] == 1:
                plus += 1
        else:
                plus = 0
        b += plus

print (b)
         
        