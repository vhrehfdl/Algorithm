def solution(A):

    count = 0

    right_dict = {}
    right_len = len(A)
    for a in A:
        if a in right_dict:
            right_dict[a] += 1
        else:
            right_dict[a] = 1
    
    left_leader = 0
    left_leader_count = 0
    left_dict = {}
    left_len = 0

    for a in A:
 
        right_dict[a] -= 1
        right_len -= 1

        if a in left_dict:
            left_dict[a] += 1
        else:
            left_dict[a] = 1
        left_len += 1
        
        if left_dict[a] > left_leader_count:
            left_leader = a
            left_leader_count = left_dict[a]
        
        if left_leader_count > left_len/2 and right_dict[left_leader] > right_len/2:
            count += 1

    return count
