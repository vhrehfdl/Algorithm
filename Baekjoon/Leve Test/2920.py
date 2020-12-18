N_list = input()
N_list = list(map(int, N_list.split(" ")))

Flag = "mixed"
for i in range(1, len(N_list)):
    if N_list[0] + i == N_list[i]:
        Flag = "ascending"
    elif N_list[0] - i == N_list[i]:
        Flag = "descending"
    else:
        Flag = "mixed"
        break

print(Flag)