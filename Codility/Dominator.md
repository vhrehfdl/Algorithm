def solution(A):
    if len(A) != 0:
        dic_id = {}
        for i in list(set(A)):
            dic_id[i] = [0,0]
        
        for i in range(0, len(A)):
            dic_id[A[i]][0] += 1
            dic_id[A[i]][1] = i
        
        max_val, max_id = 0, 0
        for key in dic_id.keys():
            if dic_id[key][0] > max_val:
                max_val = dic_id[key][0]
                max_id = dic_id[key][1]

        if max_val > int(len(A)/2):
            return max_id
        else:
            -1

    return -1
