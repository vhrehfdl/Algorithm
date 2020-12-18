num = int(input())

memo = [0] * (num + 3)
memo[1] = 1
memo[2] = 2


for i in range(1, num+1):
    memo[i+2] = memo[i+1] + memo[i]

print(memo[num] % 10007)