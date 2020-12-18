# N = int(input())
# A = sorted(map(int, input().split()))

N = 5
A = [-97, -6, -2, 6, 98]

mid = 10**7
for i in range(0, len(A)-1):
    a = A[i]
    start = i+1
    end = N-1

    while start < end:
        b, c = A[start], A[end]

        if abs(a+b+c) < mid:
            mid = a+b+c
            ans = (a, b, c)

        if a+b+c == 0:
            print(a, b, c)
            exit()
        elif a+b+c < 0:
            start += 1
        else:
            end -= 1

print(*ans)