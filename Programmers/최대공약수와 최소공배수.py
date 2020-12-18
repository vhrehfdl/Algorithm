def solution(n, m):
    answer = []

    min_val = min(n, m)
    for i in range(min_val, 0, -1):
        if (n % i == 0) and (m % i == 0):
            answer.append(i)
            break

    max_val = n * m
    for i in range(min_val, max_val + 1):
        if (i % n == 0) and (i % m == 0):
            answer.append(i)
            break

    return answer