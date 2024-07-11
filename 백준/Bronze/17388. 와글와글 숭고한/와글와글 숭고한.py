s, k, h = map(int, input().split())
if s + k + h >= 100:
    print ("OK")
elif (s + k + h < 100) and (s<k<h or s<h<k):
    print ("Soongsil")
elif (s + k + h < 100) and (h<k<s or h<s<k):
    print ("Hanyang")
elif (s + k + h < 100) and (k<s<h or k<h<s):
    print ("Korea")