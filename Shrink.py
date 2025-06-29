# https://codeforces.com/contest/2117/problem/B

t = int(input())

for test_case in range(t):
    n = int(input())

    p = [0] * n

    if n % 2 == 0:
        middle = n//2 - 1
        for i in range(middle + 1):
            p[middle - i] = n - 2*i
            p[middle + i + 1] = n -1 - 2*i

    else:
        middle = n//2 
        for i in range(middle + 1):
            p[middle - i] = n - 2*i

            if (middle + i + 1) < n:
                p[middle + i + 1] = n -1 - 2*i

    for pi in p:
        print(pi, end = ' ')

    print()