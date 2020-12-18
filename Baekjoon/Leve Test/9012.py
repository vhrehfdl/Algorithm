N = int(input())
N_list = []
for i in range(0, N):
    N_list.append(input())



for i in range(0, len(N_list)):
    a = list(N_list[i])
    b = list(N_list[i])

    flag = "NO"

    for j in range(0, len(a)):
        try:
            if a[j] == "(":
                if b[0] == ")":
                    flag = "NO"
                    break
                else:
                    b.remove("(")
                    b.remove(")")


            if len(b) == 0:
                flag = "YES"
                break

        except:
            flag = "NO"

    print(flag)

