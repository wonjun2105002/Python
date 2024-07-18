list = [ ]
odd = [ ]
for i in range (0,7):
    a = int(input())
    list.append(a)
    if a%2 == 1:
        odd.append(a)
        
if len(odd) == 0:
    print("-1")

else:
    print (sum(odd))
    print (min(odd))