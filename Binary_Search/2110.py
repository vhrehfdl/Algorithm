def solution(total_list, C):
    left = 1
    right = total_list[-1] - total_list[0]

    while left <= right:
        mid = (left + right) // 2

        cnt = 1
        temp_mid = total_list[0]

        for i in range(1, len(total_list)):
            if mid <= (total_list[i] - temp_mid):
                cnt += 1
                temp_mid = total_list[i]

        if cnt < C:
            right = mid - 1
        elif cnt >= C:
            ans = mid
            left = mid + 1

    return ans


if __name__ == '__main__':
    first_line = input()
    N, C = first_line.split(" ")
    N, C = int(N), int(C)

    total_list = []
    for i in range(0, N):
        next_line = int(input())
        total_list.append(next_line)

    total_list.sort()

    print(solution(total_list, C))