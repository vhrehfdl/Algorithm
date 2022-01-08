def solution(record):
    convert_action = []
    uid_dic = {}
    for i in range(0, len(record)):
        split_str = record[i].split(" ")
        action = split_str[0]
        
        if action == "Enter":
            convert_action.append([split_str[1], "님이 들어왔습니다."])
            uid_dic[split_str[1]] = split_str[2]
        elif action == "Leave":
            convert_action.append([split_str[1], "님이 나갔습니다."])
        elif action == "Change":
            uid_dic[split_str[1]] = split_str[2]
    
    answer = []
    for sentence in convert_action:
        answer.append(uid_dic[sentence[0]]+sentence[1])
    
    return answer
