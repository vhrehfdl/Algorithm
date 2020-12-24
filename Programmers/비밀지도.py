def convert(n, element):
    total = ""
    for i in range(n):
        total += str(element % 2)
        element = int(element / 2)

    return total[::-1]


def solution(n, arr1, arr2):
    answer = []
    for i in range(0, n):
        arr1_convert = convert(n, arr1[i])
        arr2_convert = convert(n, arr2[i])

        map = ""
        for j in range(0, len(arr1_convert)):
            if arr1_convert[j] == "1" or arr2_convert[j] == "1":
                map += "#"
            else:
                map += " "

        answer.append(map)

    return answer