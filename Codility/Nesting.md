def solution(S):
    total_list = []
    for i in range(0, len(S)):
        if S[i] == "(":
            total_list.append(S[i])
        else:
            if len(total_list) > 0:
                del total_list[-1]
            else:
                return 0
    
    if len(total_list) == 0:
        return 1
    else:
        return 0
