n = int(input())
times = list(map(int, input().split()))

a = b = 0
left, right = 0, n - 1
total_time_a = total_time_b = 0

while left <= right:
    if total_time_a <= total_time_b:
        total_time_a += times[left]
        a += 1
        left += 1
    else:
        total_time_b += times[right]
        b += 1
        right -= 1

print(a, b)