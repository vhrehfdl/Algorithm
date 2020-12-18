import sys

input = sys.stdin.readline
from bisect import *

# N = int(input())
# A = sorted(map(int, input().split()))

N = 5
A = [-97, -6, -2, 6, 98]

if A[0] >= 0:
    print(A[0], A[1], A[2])
    exit()
if A[-1] <= 0:
    print(A[-3], A[-2], A[-1])
    exit()

s = 10 ** 12
ans = ()
for i in range(N - 1):
    a = A[i]
    start = i + 1
    end = N - 1

    while start < end:
        b, c = A[start], A[end]

        if abs(a + b + c) < s:
            s = abs(a + b + c)
            ans = (a, b, c)

        if a + b + c == 0:
            print(a, b, c)
            exit()
        elif a + b + c > 0:
            end -= 1
        else:
            start += 1

print(*ans)