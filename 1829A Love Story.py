t = int(input())
for _ in range(t):
    s = input()
    diff_count = 0
    for i in range(len(s)):
        if s[i] != "codeforces"[i]:
            diff_count += 1
    print(diff_count)