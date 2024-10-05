


while True:
        n = int(input())
        if n == -1 :
                break
        e = []
        for i in range (1,n):
                if  n % i == 0:
                        e.append(i)
        if sum(e) == n:
                print (n, "= " , end = "")
                print (*e, sep = " + ")

        else:
                print (n, "is NOT perfect.")
                