# n = int(input())
# k = int(input())

n = 3
k = 7

start = 1
end = k

while start <= end:
  mid = (start + end) // 2

  count = 0
  for i in range(1, n+1):
    count += min(mid//i, n)
  
  print(mid, count)

  if count >= k:
    answer = mid
    end = mid - 1
  else:
    start = mid + 1

print(answer)