def solution(dartResult):
    score_list = []
    flag = False
    for i in range(0, len(dartResult)):
        if dartResult[i].isdigit() and dartResult[i + 1].isdigit():
            score_list.append(dartResult[i:i + 2])
            flag = True
        else:
            if flag != True:
                score_list.append(dartResult[i])
            else:
                flag = False

    update_score_list = []
    for i in range(0, len(score_list)):
        if score_list[i] == "S":
            update_score_list.append(int(score_list[i - 1]))
        elif score_list[i] == "D":
            update_score_list.append(int(score_list[i - 1]) ** 2)
        elif score_list[i] == "T":
            update_score_list.append(int(score_list[i - 1]) ** 3)
        elif score_list[i] == "#" or score_list[i] == "*":
            update_score_list.append(score_list[i])

    for i in range(0, len(update_score_list)):
        if update_score_list[i] == "*":
            update_score_list[i - 1] *= 2

            if (update_score_list[i - 2] == "#" or update_score_list[i - 2] == "*") and i - 3 >= 0:
                update_score_list[i - 3] *= 2
            elif update_score_list[i - 2] != "#" and update_score_list[i - 2] != "*" and i - 2 >= 0:
                update_score_list[i - 2] *= 2

        elif update_score_list[i] == "#":
            update_score_list[i - 1] *= -1

    print(update_score_list)

    answer = 0
    for i in range(0, len(update_score_list)):
        if str(update_score_list[i]) != "#" and str(update_score_list[i]) != "*":
            answer += update_score_list[i]

    print(answer)
    return answer