user_first = int(input())
user_second = input()

temp_list = user_second.split(" ")
total_list = []
for i in temp_list:
    total_list.append(int(i))

memo = [0] * user_first

temp_list = []

memo[0] = total_list[0]
for j in range(1, user_first):
    memo[j] = max(memo[j-1] + total_list[j], total_list[j])

print(max(memo))
