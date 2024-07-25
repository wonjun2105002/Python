
word = input()
word =word.upper()
alp= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
alpcount = []

for i in alp:
    alpcount.append(word.count(i))
a = max(alpcount)
b = alpcount.count(a)

if b >= 2:
    print("?")
else :
    print(alp[alpcount.index(a)])