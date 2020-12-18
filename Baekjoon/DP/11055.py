user_num = int(input())
user_input = input()

total_list = user_input.split()
memo = [0] * (user_num + 1)
memo_update = [0] * (user_num + 1)


for i in range(0, user_num):
    memo[i] = int(total_list[i])
    memo_update[i] = int(total_list[i])


for i in range(0, user_num):
    temp_list = []
    for j in range(0, i):
        if memo[i] > memo[j]:
            temp_list.append(memo_update[j])

    if len(temp_list) > 0:
        memo_update[i] = memo[i] + max(temp_list)

print(max(memo_update))
