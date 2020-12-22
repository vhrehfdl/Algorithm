def solution(d, budget):
    d.sort()

    answer = 0
    total = 0
    for i in range(0, len(d)):
        total += d[i]
        if total <= budget:
            answer += 1
    return answer