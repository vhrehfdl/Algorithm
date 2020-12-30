import math


def solution(progresses, speeds):
    remainder_list = []
    for i in range(0, len(progresses)):
        remainder_list.append(math.ceil((100 - progresses[i]) / speeds[i]))

    cnt = 1
    max_val = remainder_list[0]
    answer = []

    for i in range(1, len(remainder_list)):
        if max_val < remainder_list[i]:
            print(max_val, remainder_list[i])
            max_val = remainder_list[i]
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1

    answer.append(cnt)

    return answer