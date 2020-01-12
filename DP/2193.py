n = int(input())

memo = [0] * (n + 3)
memo[1] = 1
memo[2] = 1

if n == 1 or n == 2:
    print(1)
else:
    for i in range(2, n):
        memo[i+1] = memo[i] + memo [i-1]

    print(memo[n])

