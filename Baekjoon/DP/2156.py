n = int(input())
a = [0]

for i in range(n):
    a.append(int(input()))

if n == 1:
    print(a[1])
else:
    d = [0, a[1], a[1]+a[2]]

    for i in range(3, n+1):
        d.append(max(d[i-1], d[i-2] + a[i], d[i-3] + a[i-1] + a[i]))
        
    print(d[n])