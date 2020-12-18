for _ in range(int(input())):
    a=input()
    b=a[::-1]
    a=int(a)+int(b)
    print(["NO","YES"][a==int(str(a)[::-1])])