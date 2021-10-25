# 입력 Flow
first_line = input()
n, m = first_line.split(" ")[0], first_line.split(" ")[1]
n, m = int(n), int(m)

second_line = input()
n_list = second_line.split(" ")
n_list = [int(n) for n in n_list]
n_list.sort()


def binary_search(start, end):
  candidates = list(range(start, end))

  while start <= end:  
    mid = (start + end) // 2

    total = 0
    for candidate in candidates:
      if (candidate - mid) > 0:
        total += (candidate - mid)

    if total == m:
      return mid
    elif total > m:
      start = mid + 1
    elif total < m:
      end = mid -1


start, end = n_list[0], n_list[-1]
binary_search(start, end)