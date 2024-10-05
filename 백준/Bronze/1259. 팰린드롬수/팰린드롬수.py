while True:
        a = int(input())
        a= str(a) 
        if a == "0":
                break
        
        
        elif a[::-1] == a:
                print ("yes")

        else:
                print ("no")
