import math


def solution(s):
    total_list = []
    for i in range(1, math.ceil(len(s) // 2) + 1):
        cnt = 1
        start_val = s[0:1 * i]
        temp_text = ""

        for j in range(1, math.ceil(len(s) / i)):
            next_val = s[j * i:(j + 1) * i]

            if start_val == next_val:
                cnt += 1
            else:
                if cnt == 1:
                    temp_text += start_val
                else:
                    temp_text += str(cnt) + start_val
                start_val = next_val
                cnt = 1

        if cnt == 1:
            temp_text += start_val
        else:
            temp_text += str(cnt) + start_val

        total_list.append(len(temp_text))

    if len(total_list) == 0:
        answer = 1
    else:
        answer = min(total_list)
    return answer