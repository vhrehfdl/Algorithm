def solution(total_list, N):
    total_list.sort()

    left = 0
    right = total_list[-1]
    result = 0

    while left <= right:
        mid = (left + right) // 2
        cnt = 0

        if mid == 0:
            return 1

        for element in total_list:
            cnt += element // mid

            if cnt >= N and mid > result:
                result = mid
                break

        if cnt < N:
            right = mid - 1
        else:
            left = mid + 1

    return result


if __name__ == '__main__':
    one_line = input()
    K, N = one_line.split()
    K, N = int(K), int(N)

    total_list = []
    for i in range(0, K):
        ran_line = int(input())
        total_list.append(ran_line)

    print(solution(total_list, N))
