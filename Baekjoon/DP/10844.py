memo = [0] * 10

memo[0] = 0
for i in range(1, 10):
    memo[i] = 1


iter = int(input())

n = 1

while n < iter:
    temp_memo = [0] * 10
    for i in range(0, 10):
        if i == 0:
            temp_memo[i] = memo[i+1]
        elif i == 9:
            temp_memo[i] = memo[i-1]
        else:
            temp_memo[i] = memo[i-1] + memo[i+1]

    memo = temp_memo
    n += 1

print(sum(memo) % 1000000000)

