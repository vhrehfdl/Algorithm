def solution(board, moves):
    new_board_list = []
    for i in range(0, len(board)):
        temp_list = []
        for j in range(0, len(board)):
            if board[j][i] != 0:
                temp_list.append(board[j][i])
        new_board_list.append(temp_list)

    moves_result = []
    for i in range(0, len(moves)):
        if len(new_board_list[moves[i] - 1]) != 0:
            moves_result.append(new_board_list[moves[i] - 1][0])
            del new_board_list[moves[i] - 1][0]

    answer = 0

    i = 1
    while i < len(moves_result):
        try:
            if moves_result[i] == moves_result[i - 1]:
                del moves_result[i]
                del moves_result[i - 1]

                i = i - 2
                answer += 1
        except:
            break
        i = i + 1

    answer *= 2
    return answer