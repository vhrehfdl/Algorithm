N = 9
paper = [[0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 1, -1, 0, 1, -1], [0, -1, 1, 0, 1, -1, 0, 1, -1], [0, 1, -1, 1, 0, -1, 0, 1, -1]]
#
# for i in range(0, 3):
#     width = i*3
#     height = i*3

# N = int(input())
#
# paper = [list(map(int, input().split())) for _ in range(N)]
# print(paper)
neg = 0
neut = 0
pos = 0


def clip_paper(x, y, n):
    global neg, neut, pos

    num_check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (paper[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        clip_paper(x + k * n // 3, y + l * n // 3, n // 3)
                return

    print(num_check)
    print()

    if (num_check == -1):
        neg += 1
    elif (num_check == 0):
        neut += 1
    else:
        pos += 1


clip_paper(0, 0, N)
# print(f'{neg}\n{neut}\n{pos}')