a = int(input())
for i in range (a):
    string = ""
    b, c = input().split()
    for j in range(len(c)):
        string += c[j] * int(b)
    print(string)