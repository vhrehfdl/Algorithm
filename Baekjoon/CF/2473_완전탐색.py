# N = int(input())
# A = sorted(map(int, input().split()))
#
# print(N)
# print(A)

N = 5
A = [-97, -6, -2, 6, 98]

for i in range(0, len(A)-2):
    a = A[i]
    print("a", a)

    for j in range(i, len(A)-2):
        b = A[j+1]
        c = A[j+2]

        print("b", b)
        print("c", c)

    print()


