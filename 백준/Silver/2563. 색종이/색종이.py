


arr = []
for i in range (100):
        for i in range (100):
                arr.append([0]*100)
                
a = int(input())               
for i in range (a):
        b,c = map(int, input().split())
        for j in range (b, b+10):
                for y in range (c, c+10):
                        arr[j][y] = 1
count = 0
for i in range (100):
        for j in range (100):
                if arr[i][j] :
                        count +=1
print (count)
                        
        

