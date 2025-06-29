# https://codeforces.com/contest/2121/problem/A

t = int(input())

for test_case in range(t):

    n, s = map(int, input().split())

    x_arr = list(map(int, input().split()))

    d1 = abs(s - x_arr[0])

    d2 = abs(x_arr[-1] - s)

    x_len = x_arr[-1] - x_arr[0]

    if d1 > x_len or d2 > x_len:
        min_d = max(d1, d2)


    else:
        min_d = min(d1, d2) + x_len

    print(min_d)    