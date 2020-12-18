cnt = int(input())
total_list = input()
total_list = total_list.split(" ")

new_total = []

for element in total_list:
    new_total.append(int(element))

new_total.sort()

# # new_total = [-2, 4, -99, -1, 98]
# new_total = [0, 1, 2]

#case1 : 음수 최소 + 양수 최대
new_total.sort()

total_list = []

case1 = min(new_total) + max(new_total)
total_list.append(abs(case1))


#case2 : 음수 최소1 + 음소 최소2
#case3 : 양소 최소1 + 양수 최소2
plus_list, minus_list = [], []
for element in new_total:
    if element < 0:
        minus_list.append(element)
    else:
        plus_list.append(element)

case2 = case1+1
if len(minus_list) > 1:
    case2 = minus_list[-1] + minus_list[-2]
total_list.append(abs(case2))

case3 = case1+1
if len(plus_list) > 1:
    case3 = plus_list[0] + plus_list[1]
total_list.append(abs(case3))


case = total_list.index(min(total_list))

if case == 0:
    print(min(new_total), max(new_total))
elif case == 1:
    print(minus_list[-1], minus_list[-2])
elif case == 2:
    print(plus_list[0], plus_list[1])
