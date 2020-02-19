N = int(input())
A = list(map(int,input().split()))
A.sort()
s, e = 0, N-1
m = abs(A[s]+A[e])
p, q = s, e
print(m)

while s != e:
    if abs(A[s+1]+A[e]) < abs(A[s]+A[e-1]):
        s += 1
    else:
        e -= 1

    if m > abs(A[s]+A[e]) and s != e:
        m = abs(A[s]+A[e])
        p, q = s, e

    print(p, q)

print(A[p], A[q])