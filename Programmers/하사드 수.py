def solution(x):
    total = 0
    for c in str(x):
        total += int(c)

    if x % total == 0:
        answer = True
    else:
        answer = False

    return answer