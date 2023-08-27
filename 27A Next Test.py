n = int(input())
tests = list(map(int, input().split()))
tests.sort()
default_index = 1
for index in tests:
    if index == default_index:
        default_index += 1

print(default_index)