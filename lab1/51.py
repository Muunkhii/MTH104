n = 5123
s = 1
while(n > 0):
    # print(n, n % 10)
    s= s * (n % 10)
    n = n // 10
    print (s)
