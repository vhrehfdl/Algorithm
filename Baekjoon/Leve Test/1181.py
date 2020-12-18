N = int(input())
N_list = []

for i in range(0, N):
    N_list.append(input())

# N_list = ["but", "i",  "wont", "hesitate", "no", "more", "no", "more", "it", "cannot", "wait", "im", "yours"]
N_list = list(set(N_list))
N_list.sort()

len_list = []
for i in range(0, len(N_list)):
    len_list.append(len(N_list[i]))

for i in range(0, max(len_list)+1):
    for j in range(0, len(N_list)):
        if i == len(N_list[j]):
            print(N_list[j])
