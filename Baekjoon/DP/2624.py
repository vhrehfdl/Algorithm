

# list_a = [[0, 10, 20], [0, 5, 10, 15], [0, 1, 2, 3, 4, 5]]
# list_a = [[0, 1, 2, 3, 4, 5], [0, 5, 10, 15], [0, 10, 20]]
# list_a = [[1, 1, 1, 1, 1], [5, 5, 5], [10, 10]]
list_a = [1, 1, 1, 1, 1, 5, 5, 5, 10, 10]

# memo = [0] * 100
# cnt = 0
# for i in range(0, len(list_a)):
#     for j in range(0, len(list_a[i])):
#         print(list_a[i][j])
#         memo[cnt] = list_a[i][j]
#         cnt += 1
#
# print(memo)

print(len(list_a))

for i in range(0, len(list_a)):
    print(list_a[i])