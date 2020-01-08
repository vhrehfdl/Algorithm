def sol(tree, max_num):
    for j in range(0, max_num):
        for i in range(0, len(tree[j])-1):
            tree[j+1][i] += max(tree[j][i], tree[j][i+1])

    print(tree[-1][-1])


def main():
    tree = []
    max_num = int(input())

    for i in range(0, max_num):
        user_tree = input()
        tree.append(user_tree.split(" "))

    total_tree = []
    for i in range(0, len(tree)):
        temp_tree = []
        for j in range(0, len(tree[len(tree)-i-1])):
            temp_tree.append(int(tree[len(tree)-i-1][j]))
        total_tree.append(temp_tree)

    sol(total_tree, max_num=max_num)


if __name__ == '__main__':
    main()