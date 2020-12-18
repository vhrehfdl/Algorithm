cnt = int(input())
total_list = input()
total_list = total_list.split(" ")

new_total = []

for element in total_list:
    new_total.append(int(element))

new_total.sort()

min_list = []
index_list = []
element_list = []
for i in range(0, len(new_total)):
    for j in range(1, len(new_total)):
        result = new_total[i] + new_total[j]
        min_list.append(result)
        index_list.append(abs(result))
        element_list.append((new_total[i], new_total[j]))

min_index = index_list.index(min(index_list))

print(element_list[min_index][0], element_list[min_index][1])