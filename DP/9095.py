num = int(input())
n = 0

temp_list = []
while n < num:
    n += 1
    user_input = int(input())
    temp_list.append(user_input)


for user_num in temp_list:
    if user_num == 1:
        print(1)
    elif user_num == 2:
        print(2)
    else:
        dp = [0 for _ in range(user_num+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, user_num+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        print(dp[user_num])