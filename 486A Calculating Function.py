def solve(n):
    if n % 2 == 0:
        return n/2
    else:
        prev = (n-1)/2
        return prev-n


if __name__ == "__main__":
    n = int(input())
    print(int(solve(n)))