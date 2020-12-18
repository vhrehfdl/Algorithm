# 문제 풀이
# 배열을 정렬한 다음 가장 큰 값부터 제거를 한다.
# 예산을 넘지 않는 값중 가장 큰 값을 선택한다.
# 그 후 임심 가장 큰 값으로 제거된 값을 채운 다음 더해 예산 값과 뺀다.
# 뺀 값에 나누기를 하여 최대 값을 출력한다.
# 최대값이 아예 없는 예외처리도 신경써야 한다.

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())

# N = 3
# A = [2, 3, 4]
# M = 5

anw = M//N
cnt = 0
while N > 0:
    N -= 1

    new_A = A
    if sum(A) <= M:
        temp_max_value = sum(new_A + [max(A)] * cnt)

        if temp_max_value <= M and cnt != 0:
            anw = max(A) + ((M - temp_max_value) // cnt)
            break

        elif temp_max_value <= M and cnt == 0:
            anw = max(A)
            break

    del A[N]
    cnt += 1

print(anw)

