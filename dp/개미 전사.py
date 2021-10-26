# 입력 Flow
n = input()
n_list = list(map(int, input().split(" ")))

d = [0] * (n)
d[0] = n_list[0]
d[1] = n_list[1]


for i in range(2, n):
  d[i] = n_list[i] + d[i-2]
print(max(d))