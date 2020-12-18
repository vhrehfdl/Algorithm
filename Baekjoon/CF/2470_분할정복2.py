# 1. 리스트 안의 요소를 절대값을 씌운 후 정렬한다.
# ex) [ -1, 53, 2, -32 ] -> [ 1, 2, 32, 53 ]

# 2. 위의 리스트에서 서로 인접하는 두 값을 더해준다. (더해줄 때는 절대값이 원래 값을 더해준 후 최소 값을 선택한다)
# ex) 1이 가장 작은 값이니 -1, 2를 출력하게 한다.

# 3. 예외처리로 -1, 1과 같은 중복 된 값이 있으면 그 값이 출력하게 한다.

# %% 중요한게 이중 포문을 사용하면 안된다.

cnt = int(input())
total_list = input()
total_list = total_list.split(" ")

new_total = []
for element in total_list:
    new_total.append(int(element))


duplicate_list = []

dic_total = {}
for element in new_total:
    duplicate_list.append(abs(element))
    dic_total[abs(element)] = element

# - 중복 된 값 예외처리.
if len(duplicate_list) == len(set(duplicate_list)):
    abs_list = list(dic_total.keys())
    abs_list.sort()

    # - 인접한 리스트 두 값 더해주기
    min_list, index_list = [], []
    for i in range(1, len(abs_list)):
        min_list.append(dic_total[abs_list[i-1]] + dic_total[abs_list[i]])
        index_list.append((dic_total[abs_list[i-1]], dic_total[abs_list[i]]))

    # - 최소 값 구하기.
    new_abs_list = []
    for element in min_list:
        new_abs_list.append(abs(element))

    min_value = min(new_abs_list)
    min_value_index = new_abs_list.index(min_value)

    if index_list[min_value_index][0] < index_list[min_value_index][1]:
        print(index_list[min_value_index][0], index_list[min_value_index][1])
    else:
        print(index_list[min_value_index][1], index_list[min_value_index][0])

else:
    word_cnt = dict()
    for word in duplicate_list:
        if word not in word_cnt.keys():
            word_cnt[word] = 1
        else:
            print(-word, word)
            break
