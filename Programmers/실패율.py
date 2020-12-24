import collections


def solution(N, stages):
    cnt_dic = collections.Counter(stages)
    user_num = len(stages)

    fail_dic = {}
    for i in range(1, N + 1):
        if user_num != 0:
            fail_val = (cnt_dic[i] / user_num)
            fail_dic[i] = fail_val
        else:
            fail_dic[i] = 0

        user_num -= cnt_dic[i]

    return sorted(fail_dic, key=lambda k: fail_dic[k], reverse=True)