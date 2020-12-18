target = 37
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
print(m_list)
left = 0
right = length-1

cnt = 1
while left <= right:
    print(cnt)
    cnt += 1
    mid = (left + right) // 2
    if m_list[mid] == target:
        print("중간 값", mid+1)
        break
    elif m_list[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
