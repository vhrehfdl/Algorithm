def reverse_num(n_list):
    sum_list = []

    for i in range(0, len(n_list)):
        reverse_num = ""
        for j in range(1, len(n_list[i])+1):
            reverse_num += n_list[i][len(n_list[i])-j]

        sum_num = int(n_list[i]) + int(reverse_num)
        sum_list.append(sum_num)

    return sum_list


def same_check(sum_list):
    for i in range(0, len(sum_list)):
        num = str(sum_list[i])

        for j in range(0, int(len(num)/2)):
            flag = "YES"

            if num[j] != num[len(num)-1-j]:
                flag = "NO"
                break

        print(flag)


def main():
    N = int(input())

    n_list = []
    for i in range(0, N):
        n_list.append(input())

    sum_list = reverse_num(n_list)
    same_check(sum_list)


if __name__ == '__main__':
    main()